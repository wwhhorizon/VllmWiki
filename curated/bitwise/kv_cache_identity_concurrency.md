# 并发下的 KV Cache Identity

状态：curated。  
父页：[Bitwise 确定性与数值等价](README.md)。
范围：并发、offload、prefix sharing、LoRA/external KV、block reuse 和 metadata cleanup 下的 KV 身份一致性。

## 问题定义

KV cache block 必须只代表它真实对应的 prompt、token range、model、adapter、dtype、layout、backend、cache group 和请求状态。任何请求读取到其他请求、其他 adapter 或旧生命周期的 KV，都不是数值误差，而是 correctness bug。

## 典型触发条件

- concurrent prefill 中不同 prompt length 复用同一个 persistent row slot。
- block table、slot mapping 或 page indices 的尾部未清理。
- recycled KV block 或 offload/restore 路径保留旧数据。
- hybrid Mamba/attention 模型共享 block pool，fp32 SSM state block 被复用成 fp8/fp16 attention KV block。
- LoRA、adapter、external KV cache 的 key 缺少 adapter identity/version。
- prefix sharing 或 LMCache 命中跨越了语义不同的请求状态。

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#39589](https://github.com/vllm-project/vllm/issues/39589) | variable-length concurrent prefill 在 `temperature=0` 下产生非确定输出；`VLLM_BATCH_INVARIANT=1`、禁用 prefix cache、已有 recycled-block fix 都不能解释。 | 这是 KV read/write identity 问题。 |
| [#35219](https://github.com/vllm-project/vllm/pull/35219) | merged PR 修复 hybrid Mamba/attention 共享 block pool 的 NaN 污染：Qwen3.5 类模型中，fp32 Mamba/SSM state block 被重新分配给 fp8/fp16 full-attention KV 时，旧 bit pattern 可被解释成 NaN/Inf；FlashAttention3、FlashInfer-TRTLLM 等 attention kernel 用 multiply-by-zero mask 处理未用位置，但 `0 * NaN` 仍是 NaN。PR 在 scheduler 侧跟踪本 step 新分配的 `FullAttentionSpec` block id，在 worker `_update_states()` 中用单个 Triton kernel 清零对应 GPU memory；该路径只在 `has_mamba_layers` 的 hybrid 模型下启用，prefix-cache hit block 不清零。 | KV block 的 identity 还包括“上一生命周期的 dtype 解释方式”。当同一物理 block 可在 Mamba fp32 state 与 attention fp8/fp16 KV 间复用时，block reuse 前必须清除跨 dtype stale bits；但当前结论是 hybrid-scoped zeroing，不是所有 attention block 的通用 zeroing policy。 |
| [#30931](https://github.com/vllm-project/vllm/issues/30931), [#31069](https://github.com/vllm-project/vllm/pull/31069) | LoRA prefix cache hash 使用 `lora_name` 而非全局唯一 `lora_int_id`，同名不同 ID adapter 会错误共享 cache block。 | adapter identity 是 KV cache key 的必填维度。 |
| [#31210](https://github.com/vllm-project/vllm/issues/31210), [#31341](https://github.com/vllm-project/vllm/pull/31341) | high-concurrency CPU KV offload 下，同 prompt 会生成错误/乱码。maintainer 在 issue 评论中明确说 `#31341` 能稳定复现并解决问题，用户随后确认 production 不再发生。补抓后的 merged PR 证实修复点有三层：GPU->CPU offload stream 先 `wait_stream(torch.cuda.current_stream())`，避免在 compute 尚未完成时搬走 KV；store job 改为在下一 engine step 统一提交，避免和 `sample_tokens` 的 GPU->CPU copy 争抢 copy engine；同时去掉 stream priority 这一无效控制，并更新 unit tests 追踪 deferred store bookkeeping。 | KV offload identity 不只是 key/ownership，还包括 copy 的时序和 DMA 争用。offload store 必须晚于本 step compute，并与 sample-token copy 的流序关系明确；否则 restore 回来的 KV 本身就已经不对应正确内容。 |

## 根因机制

KV identity 失败通常来自状态身份建模不完整。cache key 少一个维度、metadata tail 没清理、block reuse 没 zero、offload ownership 混淆，都会让下游 attention 读取错误语义的 K/V。由于 KV 会参与后续所有 decode step，这类错误常表现为 nondeterministic token，而不是局部 tensor mismatch。

`#39146/#43741` 说明 recycled-block zeroing 不是一个布尔开关能解决的单点问题：cache config 要声明该 spec family 需要 zeroing，allocator/manager 还要持续收集新分配或复用的 block id。前者遗漏 FullAttention 会让标准 attention 完全不走 zeroing；后者用精确 `type` 判断会让 FullAttentionSpec 子类悄悄绕开 zeroing 队列。

`#35219` 补充了 cross-dtype block reuse 的根因：同一 block pool 里，Mamba state 与 attention KV 对同一字节序列的 dtype 解释不同。attention kernel 即使用 mask 忽略未用位置，也可能通过 `0 * NaN` 把旧 Mamba bit pattern 传播到所有共享该 KV block 的请求。因此修复点不是 sampler，也不是某个请求的 NaN 过滤，而是“新分配给 attention 的 block 在使用前必须处于零态”。

`#42125` 把 adapter identity 进一步推进到 runtime version 层：即使 `lora_name` 不变，adapter 权重内容也可能已经被热替换。此时仅按 adapter name 或复用旧 `lora_int_id` 建 cache key，都会让新 adapter 读取旧 adapter 权重产生的 prefix KV。`cache_salt`、first-block 变化和 unique-name control 能恢复正确输出，说明问题集中在 cache namespace/invalidating，而不是 sampler 随机性。

`#31210/#31341` 则说明 offload/restore 也有自己的身份契约。哪怕 block ownership 没错，只要 GPU->CPU offload 在 compute 尚未结束时开始，或者和 sample-token copy 在异步调度下争抢 copy engine，最终写到 CPU 侧的 KV 就可能已经是错误内容。这里的问题不是“读错旧块”，而是“正确块在错误时间被搬运”。

`#37076/#37152` 把 prefix sharing 再往前推了一步：prefix cache 的 identity 不只取决于 hash 和 block 内容，还取决于“该 block 何时开始对后续请求可见”。如果 `cache_full_blocks()` 在 GPU forward 真正把 KV 写好之前，就把 freshly allocated block 注册到前缀缓存哈希表，那么同一步后续请求可能会经 `get_cached_block()` 命中尚未初始化完成的块，读到别的请求的 token 边界或未完成内容。现有 `#37152` patch 用 `_blocks_registered_this_step` 把这类 block 暂时屏蔽到下一调度步；closed/unmerged 的 `#38715` 则在 `SingleTypeKVCacheManager` 层把同类 guard 推广到更上层的 prefix allocation path，并补了直接 regression tests。两条未合并 patch 线独立收敛到同一契约，说明“same-step registration visibility”很可能确实是 KV identity 问题的核心。

`#44250/#45549` 和 `#42125/#45981` 组合起来，把 adapter identity 又往前推了一层：本地 prefix cache 与 external KV connector 都不能只看 `lora_name`。但两条线的“稳定 identity”并不相同。external KV/LMCache MP 当前最直接的修法是把 LoRA name 折进外部 key salt，先阻止跨 adapter 命中；runtime same-name reload 则已经明确指出 `lora_name` 和 `lora_int_id` 都不够，因为 `load_inplace=true` 下它们可以保持不变，而 adapter bytes 已经变了，所以 prefix-cache key 需要内容派生的 version identity。换句话说，`#44250` 要补的是“不同 adapter 绝不能命中同一 external KV entry”，`#42125` 要补的是“同名同路径但内容已变的 adapter 也必须获得新的本地 prefix-cache identity”。两者相关，但不是同一闭环。

## 修复方式

1. 显式建模 cache identity：prompt/token range、base model、adapter/LoRA id、dtype、layout、backend、cache group、rank/world、salt。
2. block reuse、row move、offload restore 前后清理 stale block id、stale data 和 metadata tail。
3. 对 concurrent prefill、不同 prompt length、prefix sharing、LoRA 切换、external KV 命中写 negative tests。
4. LMCache/external KV key 若不复用 vLLM 已含 adapter identity 的 block hash，就必须显式纳入 adapter identity/version。
5. 对 external KV connector，不能只修通用或 V1 adapter path；lookup/store key 的 schema 必须在实际 MP connector 和 vLLM vendored connector 中同时闭环。
6. 对 block-table 类结构，定义并测试“逻辑长度之后必须为零”的 invariant，而不是只测试当前 append 的 slice。
7. external KV 的 adapter key 不能机械照搬本地 prefix cache：本地 runtime 可用 `lora_int_id` 区分同名 adapter，但跨进程/持久化 external cache 还需要稳定的 adapter identity/version，避免 adapter reload 或同名不同内容继续污染。
8. 对 recycled KV blocks，同时测试 `needs_kv_cache_zeroing` 的 spec-family gate 和 `new_block_ids` tracking；使用 `isinstance` 覆盖 FullAttentionSpec 子类，避免新 attention spec 默认跳过 zeroing。
9. 对 runtime LoRA load/unload/reload，若允许同名 adapter 被替换，必须引入 adapter content/version/generation identity，或在 replacement 时精确失效 adapter-dependent prefix blocks。
10. 对 hybrid Mamba/attention 共享 pool，在 scheduler 输出中传递本 step 新分配的 attention block id，并在 GPU model runner 的正确 stream order 内清零；不要在 ref count 归零时清 prefix-cached block，否则会破坏 cache hit。
11. 对 CPU/GPU offload，offload stream 必须等待 compute stream 完成，再在合适的 engine-step 边界统一提交 store；如果 sample-token copy 也走 GPU->CPU，必须把 copy-engine 次序纳入契约，而不是仅依赖 stream priority。
12. 对 external KV connector，至少要把 adapter identity 纳入 lookup/store key；对 same-name runtime reload，本地 prefix-cache key 还必须进一步版本化为内容派生 identity，不能只依赖名字、路径或进程内计数器。
13. 对 prefix cache 注册流程，fresh block 只有在对应 GPU forward 完成后才能对后续请求可见；若注册发生在同一步的 forward 之前，需要显式 same-step miss gate，而不是依赖哈希命中后“内容已经写好”的隐含假设。

## 验证契约

- metadata 层：block table tail、row move、clear row、append row 必须有 unit tests。
- 系统层：concurrent variable-length prefill 在 `temperature=0` 下输出 token 稳定。
- block-table invariant 层：一旦证明所有 row tail 恒为零，`move_row` 的整行复制与 slice+tail-zero 在 correctness 上等价；review 优化建议不能被误读成仍有 KV identity 漏洞。
- offload 层：覆盖高并发同 prompt、async scheduling on/off、store/load bookkeeping、以及 deferred store 提交前后的行为；不仅要证明错误消失，还要证明正常 offload/reuse 没被破坏。
- external adapter 层：同 base model、同 token、同 `cache_salt`、不同 LoRA/adapters 不能共享 KV 命中；同 adapter 第二次请求仍应命中，证明修复没有禁用正常复用。patched/unpatched connector 对照是有力证据，但不能替代上游 regression test。
- runtime adapter 层：同名 A->B 热替换、unload/reload same name、unique-name control、changed `cache_salt`、changed first prompt block、no-prefix-cache control 都应覆盖；若 claim 是 version-aware key，还要证明同 adapter 仍可正常复用。
- recycled-block 层：对 FullAttentionSpec、TQFullAttentionSpec、MLAAttentionSpec、SinkFullAttentionSpec 都要断言需要 zeroing，并断言 allocator/manager 会记录新 block id；SlidingWindow/CrossAttention 等不共享同一风险的 spec 不应被误纳入。
- hybrid Mamba/attention 层：覆盖 fp32 SSM state 与 fp8/fp16 KV cache dtype 组合、prefix-cache hit 不被清零、fresh allocation 被清零、FlashAttention/FlashInfer 类 mask kernel 不再传播 stale NaN；性能验证要记录 prefill/decode zeroing 开销。
- KV identity 测试优先使用 exact equality 或 token equality，不能只用宽松 `allclose`。

## 适用边界

- [#39591](https://github.com/vllm-project/vllm/pull/39591) 直接覆盖 V1 + FlashInfer + variable-length concurrent prefill 的 row tail 问题；当前本地证据中 PR 仍 open/unmerged，因此只能说机制和 patch 证据闭环，不能说已 landed。其他 backend 仍需复核相同 metadata invariant。
- [#43741](https://github.com/vllm-project/vllm/pull/43741) 当前本地证据仍 open/unmerged；PR body 的 fuzzer traces 证明 unpatched v0.19.0 可复现，unit tests 覆盖 spec gate 与 manager tracking，但 patched end-to-end validation 需要从源码 build 才能完全闭环。因此结论应写成 include-with-boundary，而不是已 landed fix。
- [#35219](https://github.com/vllm-project/vllm/pull/35219) 已 merged，适用范围是有 Mamba layers 的 hybrid 模型、freshly allocated `FullAttentionSpec` block、以及 Mamba fp32 state 可能污染 attention KV 的共享 pool。本地 targeted evidence 缺少被修复 issue `#35138` 的 JSON，因此该条依赖 PR body、patch、review 和测试结果闭环，而不是 issue body 闭环。它不清 Mamba/SSM blocks，不清 prefix-cache hit blocks，也不是对非 hybrid 部署的默认行为改变。patch 中 `type(self.kv_cache_spec) is FullAttentionSpec` 的精确类型判断符合该 PR 的窄范围，但不要把它外推成覆盖所有 FullAttentionSpec 子类的通用 zeroing fix。
- [#31341](https://github.com/vllm-project/vllm/pull/31341) 已 merged，结论覆盖 OffloadingConnector 的 GPU->CPU offload 时序、deferred store 提交和 unit-test bookkeeping 更新；issue 评论还有关于 sample-token copy stream 的后续讨论，但不影响“先等 compute、再在下一 step 提交 store”这条主修复成立。
- [#37076](https://github.com/vllm-project/vllm/issues/37076) 现已抓到两条同向 patch 线：open PR [#37152](https://github.com/vllm-project/vllm/pull/37152) 在 `BlockPool` 层用 `_blocks_registered_this_step` 阻止同一步 freshly registered block 被命中；closed/unmerged 的 [#38715](https://github.com/vllm-project/vllm/pull/38715) 则把 guard 推到 `SingleTypeKVCacheManager`，并新增 `test_no_intra_step_prefix_reuse` 与 LoRA 变体回归测试。它们共同强化了“same-step registration visibility 是 KV identity 契约”这条 insight；但 `#37152` 仍 open，`#38715` 虽有测试却未合并，而且 `#37152` 里还存在 maintainer 对 reporter 前提的公开质疑，因此目前仍保持 defer，不能写成 landed fix。
- [#44250](https://github.com/vllm-project/vllm/issues/44250) 现已抓到直接 linked PR [#45549](https://github.com/vllm-project/vllm/pull/45549)。它把 `lora_name` 折进 `LMCacheMPConnector` 的 internal cache salt，并补了 unit test，PR body 也明确写 `Fixes #44250`。这足以支持“external KV key 至少需要 adapter 维度”这条方向判断，但该 PR 仍 open/unmerged，且当前 schema 仍停留在 `lora_name` 级 identity；上游 LMCache 的 MP 路径和最终 version-aware schema 还未闭环，因此仍保持 defer。
- [#42125](https://github.com/vllm-project/vllm/issues/42125) 现已抓到两个相关 PR：closed 的 [#42495](https://github.com/vllm-project/vllm/pull/42495) 用 per-load cache key 解决 same-name reload stale reuse，但靠进程内计数器和 path fallback，边界太宽；更新的 [#45981](https://github.com/vllm-project/vllm/pull/45981) 改为 content-derived `lora_cache_key`，并在测试里直接覆盖 “same name、same path、不同权重内容 -> cache key 必须变化” 的性质，但 PR body 也明确只“部分解决” issue，仍不覆盖 HF Hub、remote path、shared-nothing 多机、external KV connector 和 worker load 前的 TOCTOU 窗口。由于 `#45981` 仍 open，当前只能把它写成最可信的修复方向，而不是 landed 结论。
- LoRA identity 与 external KV identity 应同时检查本地 cache key 和远端/cache connector key。

## 仍需补证

- 继续追踪 `#45549` 是否合并，并确认它与上游 LMCache MP 路径修复同步落地；仅 vLLM vendored connector 合并还不够，LMCache MP 的 lookup/store key schema 也必须闭环。
- 继续追踪 `#37152` 是否合并；同时复核 `#38715` 这条带 regression tests 的 manager-level guard 线是否被后续 patch 吸收。当前同类 patch 已不止一条，但 maintainer 仍未明确接受“同一步 newly registered prefix block 不能被复用”这一契约前提。
- 复核 external KV cache 与 LoRA/adapter version 的边界：adapter reload、同名不同内容、同名不同 ID、cache_salt 复用、multi-rank chunk hash。特别注意 `lora_name` 只证明“有 adapter 维度”，未必等于最终稳定 version identity。
- 继续追踪 `#45981` 是否合并；重点看 runtime load/unload 是否触发 prefix-cache eviction、`lora_cache_key` 是否真的纳入 block hash、以及 same-name reload 的 negative regression test 是否覆盖 unload/reload 与 same-path content change。
- 追踪 `#43741` 是否合并；若出现最终 patch，确认 `CrossAttentionSpec`、`SlidingWindowSpec` 等非目标 spec 没被过度 zeroing，避免把性能成本扩大到无风险路径。
- 继续复核 Mamba/hybrid 相关 open 问题时，区分 `#35219` 的 cross-dtype stale NaN、`#34874` 的 prefix metadata buffer、以及 MTP/spec decode 的 kernel-selection 问题。
- 对 `#31341` 后续 review 里提到的 `async_output_copy_stream` / `ForwardContext` 传播方案保持关注；若后续再改 hook 位置或等待流，需要确认不会破坏当前 merged 的时序保证。
