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

`#39146/#43741` 说明 recycled-block zeroing 不是一个布尔开关能解决的单点问题：cache config 要声明该 spec family 需要 zeroing，allocator/manager 还要持续收集新分配或复用的 block id。前者遗漏 FullAttention 会让标准 attention 完全不走 zeroing；后者用精确 `type` 判断会让 FullAttentionSpec 子类悄悄绕开 zeroing 队列。issue `#39146` 在 2026-06-04 收到一条新复现评论：用户在 NVIDIA A10 (GDDR6) + vLLM v0.18.1 + V1 engine + `--enable-prefix-caching` + `--enable-chunked-prefill` + `temperature=0` + `batch_size=10000` 下也遇到 KV block corruption，禁用 prefix caching 能减少失败，而 A100 不复现。这说明 recycled-block zeroing 的适用范围可能超出 `#35219` 的 hybrid Mamba scope：非 hybrid 模型在 prefix-caching + chunked-prefill 组合下也可能因 recycled block 携带 stale data 而产生 nondeterministic output，只是触发条件更苛刻（大 batch、特定 GPU 架构）。

`#35219` 补充了 cross-dtype block reuse 的根因：同一 block pool 里，Mamba state 与 attention KV 对同一字节序列的 dtype 解释不同。attention kernel 即使用 mask 忽略未用位置，也可能通过 `0 * NaN` 把旧 Mamba bit pattern 传播到所有共享该 KV block 的请求。因此修复点不是 sampler，也不是某个请求的 NaN 过滤，而是“新分配给 attention 的 block 在使用前必须处于零态”。

`#42125` 把 adapter identity 进一步推进到 runtime version 层：即使 `lora_name` 不变，adapter 权重内容也可能已经被热替换。此时仅按 adapter name、复用旧 `lora_int_id`，甚至只按 path 建 cache key，都会让新 adapter 读取旧 adapter 权重产生的 prefix KV。`cache_salt`、first-block 变化和 unique-name control 能恢复正确输出，说明问题集中在 cache namespace/invalidating，而不是 sampler 随机性。更细一点说，它要求的不是“reload 时粗暴清空 prefix cache”，而是“把本地 prefix-cache key 版本化成 loader-effective adapter identity”，让真正影响加载结果的 config、weight source 和 weight bytes 进入 hash。

`#31210/#31341` 则说明 offload/restore 也有自己的身份契约。哪怕 block ownership 没错，只要 GPU->CPU offload 在 compute 尚未结束时开始，或者和 sample-token copy 在异步调度下争抢 copy engine，最终写到 CPU 侧的 KV 就可能已经是错误内容。这里的问题不是“读错旧块”，而是“正确块在错误时间被搬运”。

`#37076/#37152` 把 prefix sharing 的可见性问题暴露成一个很有力、但仍被上游质疑的假说：如果 `cache_full_blocks()` 在 GPU forward 真正把 KV 写好之前，就把 freshly allocated block 注册到前缀缓存哈希表，那么同一步后续请求可能会经 `get_cached_block()` 命中尚未初始化完成的块，读到别的请求的 token 边界或未完成内容。`#37152` 在 `BlockPool` 层用 `_blocks_registered_this_step` 提出 same-step miss gate；随后 `#38715` 曾尝试把同类 guard 推到 `SingleTypeKVCacheManager` 并补回归测试。但 maintainer 在 `#37152` 与 `#38715` 的讨论中明确指出 same-step KV sharing 按设计是允许的，因为写 KV 发生在 attention 之前；`#38715` 作者也据此主动撤回 blanket guard，转而认为真正根因可能在 LoRA namespace、chunked prefill 或更底层 runtime/kernel。更稳妥的结论因此不是“same-step miss gate 已基本锁定根因”，而是“same-step registration visibility / block lifecycle 仍是值得跟踪的调试方向，但 guard 本身尚未获得上游接受，不能直接当作稳定机制”。 

`#44250/#45549` 和 `#42125/#45981` 组合起来，把 adapter identity 又往前推了一层：本地 prefix cache 与 external KV connector 都不能只看 `lora_name`。但两条线的成熟度已经明显分叉。runtime same-name reload 这边，`#45981` 已经把修法收敛到内容派生的 `lora_cache_key`，并显式拆成 `("lora", name) + ("lora_identity", id)` 两层 extra keys；更关键的是，这个 identity 不是拍脑袋版本号，而是 loader-effective content identity：读取 loader 实际会选中的权重文件，规范化 `adapter_config.json`，再把 `is_3d_lora_weight`、tensorizer config 等 loader-affecting 字段一起进 hash。patch 还在 serving load path 和 `InputProcessor.process_inputs` 两侧调用 `ensure_lora_cache_key`，避免只有 API load path 被修而 offline/direct/resolver-built `LoRARequest` 漏掉。测试也不只验证“不同 adapter 不同 key”，而是覆盖 same-name different-path、same-path different-cache-key、same-content same-key、config/weight change 改 key、safetensors 优先于 `.bin`、长度前缀避免拼接碰撞、relative path 退化为 path-only 等细边界。更值得注意的是，`#45981` 和早先 self-closed 的 `#42495` 不同：它主动把 claim 缩到“本地可 content-version 的 source”，明确承认 HF Hub、remote path、tensorizer/shared-nothing、external KV、rolling-upgrade 和 TOCTOU 仍是边界。结合当前 live state，这条线其实已经形成了更完整的三层闭环：identity 计算落在新文件 `vllm/lora/cache_identity.py`，request 传播落在 serving load path 与 `InputProcessor.process_inputs` backstop，命名空间消费落在 `kv_cache_utils.py` 的 block-hash extra keys。它现在缺的主要不是 patch 内部机制，而是 merge 和 source/deployment 边界能否被上游接受。

external KV 这边则还停留在跨仓 schema 对齐阶段：vLLM PR `#45549` 只是在 vendored `LMCacheMPConnector` 里把 `lora_name` 折进 internal salt，先阻止 MP connector 的跨 adapter 命中；它的 patch 只改了两处文件，证明的是“MP connector 内部 salt 这一层必须带 adapter 维度”。LMCache draft PR `#2962` 已经进一步扩到 MP connector、multi-process adapter、chunk-hash / `CacheEngineKey.tags` / L2 object key 等多层 key schema，但它当前仍 open/dirty，review 也把争论点收得更具体了：不是要不要带 LoRA 维度，而是应该由哪一层 key 充当 single source of truth。已有 review 直接建议把 LoRA 维度统一收进 `CacheEngineKey.tags`，避免 `lmcache.lora_id` 与 `lmcache.tag.lora` 这种双轨字段继续并存。换句话说，`#42125` 当前更像“局部修法已成型但未合并”，`#44250` 更像“系统级 schema 还在决定主键落点”。

## Source-Adjacent 摘要

- `#39589` 的复现条件很纯：variable-length concurrent prefill 在 `temperature=0` 下产生非确定输出，而且 `VLLM_BATCH_INVARIANT=1`、禁用 prefix cache、已有 recycled-block fix 都不能解释。这说明它不是 batch geometry 数值漂移，而是 KV read/write identity 问题：某个请求读到了其他请求的 KV。`#39591` 的 patch 证实 stale block_table tail 是直接机制，但 move_row 整行复制只是 reviewer 基于 tail-zero invariant 的性能/简化建议，不是 correctness 阻塞。
- `#35219` 的 patch 落点很明确：它在 scheduler 侧跟踪本 step 新分配的 `FullAttentionSpec` block id，在 worker `_update_states()` 中用单个 Triton kernel 清零对应 GPU memory；该路径只在 `has_mamba_layers` 的 hybrid 模型下启用，prefix-cache hit block 不清零。这说明 cross-dtype block reuse 的修复是 hybrid-scoped zeroing，不是所有 attention block 的通用 zeroing policy。
- `#31069/#31341` 的三层修复点很具体：GPU->CPU offload stream 先 `wait_stream(torch.cuda.current_stream())` 避免在 compute 未完成时搬走 KV；store job 改为在下一 engine step 统一提交，避免和 `sample_tokens` 的 GPU->CPU copy 争抢 copy engine；同时去掉 stream priority 这一无效控制。这说明 KV offload identity 不只是 key/ownership，还包括 copy 的时序和 DMA 争用。
- `#42125/#45981` 已经把 adapter identity 从抽象版本号推进到 loader-effective content identity：`#45981` 读取 loader 实际会选中的权重文件、规范化 `adapter_config.json`、`is_3d_lora_weight`、tensorizer config 一起进 hash，并在 serving load path 与 `InputProcessor.process_inputs` backstop 两侧调用 `ensure_lora_cache_key`。但这条线仍 open，剩余不确定性主要是 source/部署边界能否被上游接受，而不是 patch 内部机制。

## 修复方式

1. 显式建模 cache identity：prompt/token range、base model、adapter/LoRA id、dtype、layout、backend、cache group、rank/world、salt。
2. block reuse、row move、offload restore 前后清理 stale block id、stale data 和 metadata tail。
3. 对 concurrent prefill、不同 prompt length、prefix sharing、LoRA 切换、external KV 命中写 negative tests。
4. LMCache/external KV key 若不复用 vLLM 已含 adapter identity 的 block hash，就必须显式纳入 adapter identity/version。
5. 对 external KV connector，不能只修通用或 V1 adapter path；lookup/store key 的 schema 必须在实际 MP connector 和 vLLM vendored connector 中同时闭环。
6. 对 block-table 类结构，定义并测试“逻辑长度之后必须为零”的 invariant，而不是只测试当前 append 的 slice。
7. external KV 的 adapter key 不能机械照搬本地 prefix cache：本地 runtime 可用 `lora_int_id` 区分同名 adapter，但跨进程/持久化 external cache 还需要稳定的 adapter identity/version，避免 adapter reload 或同名不同内容继续污染。
8. 对 recycled KV blocks，同时测试 `needs_kv_cache_zeroing` 的 spec-family gate 和 `new_block_ids` tracking；使用 `isinstance` 覆盖 FullAttentionSpec 子类，避免新 attention spec 默认跳过 zeroing。
9. 对 runtime LoRA load/unload/reload，若允许同名 adapter 被替换，必须引入 adapter content/version/generation identity，或在 replacement 时精确失效 adapter-dependent prefix blocks；优先用 loader-effective content identity，而不是进程内计数器。
10. 对 hybrid Mamba/attention 共享 pool，在 scheduler 输出中传递本 step 新分配的 attention block id，并在 GPU model runner 的正确 stream order 内清零；不要在 ref count 归零时清 prefix-cached block，否则会破坏 cache hit。
11. 对 CPU/GPU offload，offload stream 必须等待 compute stream 完成，再在合适的 engine-step 边界统一提交 store；如果 sample-token copy 也走 GPU->CPU，必须把 copy-engine 次序纳入契约，而不是仅依赖 stream priority。
12. 对 external KV connector，至少要把 adapter identity 纳入 lookup/store key；对 same-name runtime reload，本地 prefix-cache key 还必须进一步版本化为内容派生 identity，不能只依赖名字、路径或进程内计数器。若 source 无法在当前节点读取实际 adapter 文件，只能退化为 path-only identity，并显式告警其 same-path content swap 边界。
13. 对 prefix cache 注册流程，fresh block 只有在对应 GPU forward 完成后才能对后续请求可见；若注册发生在同一步的 forward 之前，需要显式 same-step miss gate，而不是依赖哈希命中后“内容已经写好”的隐含假设。

## 验证契约

- metadata 层：block table tail、row move、clear row、append row 必须有 unit tests。
- 系统层：concurrent variable-length prefill 在 `temperature=0` 下输出 token 稳定。
- block-table invariant 层：一旦证明所有 row tail 恒为零，`move_row` 的整行复制与 slice+tail-zero 在 correctness 上等价；review 优化建议不能被误读成仍有 KV identity 漏洞。
- offload 层：覆盖高并发同 prompt、async scheduling on/off、store/load bookkeeping、以及 deferred store 提交前后的行为；不仅要证明错误消失，还要证明正常 offload/reuse 没被破坏。
- external adapter 层：同 base model、同 token、同 `cache_salt`、不同 LoRA/adapters 不能共享 KV 命中；同 adapter 第二次请求仍应命中，证明修复没有禁用正常复用。patched/unpatched connector 对照是有力证据，但不能替代上游 regression test。
- runtime adapter 层：同名 A->B 热替换、unload/reload same name、unique-name control、changed `cache_salt`、changed first prompt block、no-prefix-cache control 都应覆盖；若 claim 是 version-aware key，还要证明同 adapter 仍可正常复用，而且 same-content 不会无端产生新 key。
- content-identity 层：要覆盖 selected weight source precedence、canonicalized config、tensorizer config、length-framing collision、relative path path-only fallback，以及 serving load path 和 `process_inputs` backstop 会得到同一 `lora_cache_key`。
- recycled-block 层：对 FullAttentionSpec、TQFullAttentionSpec、MLAAttentionSpec、SinkFullAttentionSpec 都要断言需要 zeroing，并断言 allocator/manager 会记录新 block id；SlidingWindow/CrossAttention 等不共享同一风险的 spec 不应被误纳入。
- hybrid Mamba/attention 层：覆盖 fp32 SSM state 与 fp8/fp16 KV cache dtype 组合、prefix-cache hit 不被清零、fresh allocation 被清零、FlashAttention/FlashInfer 类 mask kernel 不再传播 stale NaN；性能验证要记录 prefill/decode zeroing 开销。
- KV identity 测试优先使用 exact equality 或 token equality，不能只用宽松 `allclose`。

### KV Cache Identity 最小验证矩阵

| Source | 保护对象 | 最小验证矩阵 | 合格契约 | 不能被什么替代 |
| --- | --- | --- | --- | --- |
| [#39589](https://github.com/vllm-project/vllm/issues/39589), [#39591](https://github.com/vllm-project/vllm/pull/39591) | block-table tail / concurrent prefill KV identity | variable-length concurrent prefill、tail-zero invariant、patched/unpatched 对照、move-row correctness 对照 | token equality + metadata tail invariant | 只测 append slice；把 reviewer 的性能建议当 correctness 阻塞 |
| [#35219](https://github.com/vllm-project/vllm/pull/35219) | hybrid Mamba/attention 的 cross-dtype block reuse | Mamba fp32 state 复用为 attention fp8/fp16 KV、`0 * NaN` 传播、hybrid-scoped zeroing 前后对照、prefix-cache hit block 不被清零 | attention block 复用前处于零态；无 NaN 污染 | 只测单 dtype；把 hybrid zeroing 外推成所有 attention block 通用 zeroing |
| [#30931](https://github.com/vllm-project/vllm/issues/30931), [#31069](https://github.com/vllm-project/vllm/pull/31069) | LoRA prefix cache 的 adapter identity | 同名不同 ID adapter、same-name different-path、adapter reload、unique-name control | 同名不同 ID 不共享 cache block；同 adapter 仍可命中 | 只看 `lora_name`；不测 reload |
| [#31210](https://github.com/vllm-project/vllm/issues/31210), [#31341](https://github.com/vllm-project/vllm/pull/31341) | CPU/GPU KV offload 的 copy 时序与 DMA 争用 | 高并发同 prompt、async scheduling on/off、deferred store 前后对照、store/load bookkeeping | offload 内容正确；正常 offload/reuse 未被破坏 | 只证明错误消失；不检查正常 reuse |
| [#42125](https://github.com/vllm-project/vllm/issues/42125), [#45981](https://github.com/vllm-project/vllm/pull/45981) | runtime LoRA reload 的 loader-effective content identity | same-name different-path、same-path different-cache-key、same-content same-key、config/weight change 改 key、unload/reload negative regression | content-derived key 稳定；same-content 不产生新 key | 只看 `lora_int_id`；只测 name 不测 content；用进程内计数器 |

## 适用边界

- [#39591](https://github.com/vllm-project/vllm/pull/39591) 直接覆盖 V1 + FlashInfer + variable-length concurrent prefill 的 row tail 问题；当前本地证据中 PR 仍 open/unmerged，因此只能说机制和 patch 证据闭环，不能说已 landed。其他 backend 仍需复核相同 metadata invariant。
- [#43741](https://github.com/vllm-project/vllm/pull/43741) 当前仍 open/unmerged，截至 2026-06-22 最后更新 2026-06-15，review comments 为 0（尚未收到任何代码审查）。PR body 的 fuzzer traces 证明 unpatched v0.19.0 可复现，unit tests 覆盖 spec gate 与 manager tracking，但 patched end-to-end validation 需要从源码 build 才能完全闭环。issue `#39146` 在 2026-06-04 收到新复现评论（A10 + prefix-caching + chunked-prefill），说明该 bug 的 scope 可能超出 hybrid Mamba 场景。因此结论应写成 include-with-boundary，而不是已 landed fix。
- [#35219](https://github.com/vllm-project/vllm/pull/35219) 已 merged，适用范围是有 Mamba layers 的 hybrid 模型、freshly allocated `FullAttentionSpec` block、以及 Mamba fp32 state 可能污染 attention KV 的共享 pool。本地 targeted evidence 缺少被修复 issue `#35138` 的 JSON，因此该条依赖 PR body、patch、review 和测试结果闭环，而不是 issue body 闭环。它不清 Mamba/SSM blocks，不清 prefix-cache hit blocks，也不是对非 hybrid 部署的默认行为改变。patch 中 `type(self.kv_cache_spec) is FullAttentionSpec` 的精确类型判断符合该 PR 的窄范围，但不要把它外推成覆盖所有 FullAttentionSpec 子类的通用 zeroing fix。
- [#31341](https://github.com/vllm-project/vllm/pull/31341) 已 merged，结论覆盖 OffloadingConnector 的 GPU->CPU offload 时序、deferred store 提交和 unit-test bookkeeping 更新；issue 评论还有关于 sample-token copy stream 的后续讨论，但不影响“先等 compute、再在下一 step 提交 store”这条主修复成立。
- [#37076](https://github.com/vllm-project/vllm/issues/37076) 现已抓到一条仍 open 的 BlockPool guard 线 [#37152](https://github.com/vllm-project/vllm/pull/37152) 和一条后来被作者主动撤回的 manager-level guard 线 [#38715](https://github.com/vllm-project/vllm/pull/38715)。前者提供了 same-step miss gate 与最小复现实验；后者虽补了 `test_no_intra_step_prefix_reuse` 与 LoRA 变体回归测试，但在 maintainer 明确说明 same-step KV sharing 按设计允许之后被作者关闭。因此当前更准确的定位是“生命周期/可见性调试方向”，而不是“已有两条同向 patch 收敛的主机制”。 
- [#44250](https://github.com/vllm-project/vllm/issues/44250) 现已抓到直接 linked PR [#45549](https://github.com/vllm-project/vllm/pull/45549)。它把 `lora_name` 折进 `LMCacheMPConnector` 的 internal cache salt，并补了 unit test，PR body 也明确写 `Fixes #44250`。这足以支持“external KV key 至少需要 adapter 维度”这条方向判断，但该 PR 仍 open/unmerged，且当前只证明了 vLLM MP connector 的 internal salt 层；上游 LMCache draft PR [#2962](https://github.com/LMCache/LMCache/pull/2962) 现已同时覆盖 MP connector、multi-process adapter、chunk-hash、`CacheEngineKey.tags` 与 L2 object key，说明它不再只是 V1 path，而是在尝试做跨层 schema 闭环。根据当前 review，争论点已经进一步收敛到 schema 设计本身：LoRA 维度究竟应由 `CacheEngineKey.tags` 这样的统一标签层承载，还是继续分散在多处 request config / token database / cache engine 字段里。当前更准确的定位仍是“跨仓 schema 仍未统一，而且 single source of truth 仍未定案”，而不是单个 vLLM PR 即将完成闭环；截至 2026-06-21，`#45549` 与 LMCache `#2962` 都仍 open，也没有新的 maintainer/reviewer acceptance signal。
- [#42125](https://github.com/vllm-project/vllm/issues/42125) 现已抓到两个相关 PR：closed 的 [#42495](https://github.com/vllm-project/vllm/pull/42495) 用 per-load cache key 解决 same-name reload stale reuse，但靠进程内计数器和 path fallback，边界太宽；更新的 [#45981](https://github.com/vllm-project/vllm/pull/45981) 改为 content-derived `lora_cache_key`，并把 `("lora", name) + ("lora_identity", id)` 直接纳入 block-hash extra keys。更重要的是，它把 identity 定义成 loader-effective content identity，而不是抽象“版本号”：选中的 weight file、规范化 `adapter_config.json`、`is_3d_lora_weight` 和 tensorizer config 都进入 hash；serving load path 与 `InputProcessor.process_inputs` backstop 共用 `ensure_lora_cache_key`，避免只有 API load path 被修。测试不仅覆盖 same-name different-path、same-path different-cache-key、same-content same-key 与 config/weight 变化改 key，还补了 safetensors 优先级、relative path path-only fallback、length framing collision 等细边界。结合当前 live patch 形态，这条线已经不是单点补丁，而是 identity 计算、request 传播、block-hash 消费三层闭环；`#45981` 目前仍 open，且截至 2026-06-21 仍只有作者正文与 bot 活动，reviewers 仍在 awaiting requested review，没有 substantive maintainer review。但它自己已经把 claim 缩到“本地可读 source 的 content identity”，因此剩余不确定性主要是 source/部署边界能否被上游接受，而不是 patch 内部机制是否还站不住。和 `#44250` 相比，它已经更像一条技术机制成熟、只差 merge 与部署边界补齐的主线。
- LoRA identity 与 external KV identity 应同时检查本地 cache key 和远端/cache connector key。
- [#44395](https://github.com/vllm-project/vllm/issues/44395) 是 open issue，有清晰根因方向但无 linked fix：`wake_up(tags=["weights"])` 只恢复权重，KV cache 仍处于 released 状态，但 engine 仍可执行 forward（DP idle rank 的 `execute_dummy_batch()` 或显式请求），访问已释放的 KV cache 导致 illegal memory access。这和 KV cache identity 的生命周期维度交叉：KV block 的 identity 包括它的 allocation 生命周期，partial wake_up 会破坏"forward 执行时 KV 必须处于 allocated 状态"这一隐含前提。截至 2026-06-22 仅有贡献者认领评论，无 maintainer 回应或 linked PR，因此暂不 promotion，只作为边界索引。


## 仍需补证

- 继续追踪 `#45549` 是否合并，并确认它与上游 LMCache MP 路径修复同步落地；仅 vLLM vendored connector 的 internal salt 合并还不够，LMCache MP 的 chunk-hash / `CacheEngineKey.tags` / L2 object key schema 也必须闭环。优先关注 `#2962` 是否把 LoRA 维度真正收敛成单一 schema 入口，而不是继续多处镜像字段并存。
- 继续追踪 `#37152` 是否获得 maintainer 接受或被新 patch 替代；同时将 `#38715` 视为被回撤的探索线，而不是独立正证。若后续要把这条线升回主机制，需要 runtime instrumentation、lifecycle trace 或 maintainer-accepted patch 明确证明 same-step sharing 的设计前提在某条路径上失效。
- 复核 external KV cache 与 LoRA/adapter version 的边界：adapter reload、同名不同内容、同名不同 ID、cache_salt 复用、multi-rank chunk hash。特别注意 `lora_name` 只证明“有 adapter 维度”，未必等于最终稳定 version identity。
- 继续追踪 `#45981` 是否合并；重点看 runtime load/unload 是否触发 prefix-cache eviction、`lora_cache_key` 是否继续稳定地落在 block-hash extra keys 上，以及 same-name reload 的 negative regression test 是否覆盖 unload/reload 与 same-path content change。若后续 reviewer 要求简化方案，需要特别防止“回退到 per-process counter”这种降低跨进程可复现性的替代案。
- 追踪 `#43741` 是否合并（当前 review comments 为 0，尚无代码审查）；若出现最终 patch，确认 `CrossAttentionSpec`、`SlidingWindowSpec` 等非目标 spec 没被过度 zeroing，避免把性能成本扩大到无风险路径。同时追踪 A10 + prefix-caching + chunked-prefill 复现是否需要扩展 zeroing scope 到非 hybrid 模型：当前 `#35219` 只在 `has_mamba_layers` 时启用 zeroing，但 `#39146` 的新复现评论表明非 hybrid 场景也可能需要 recycled-block zeroing。
- 继续复核 Mamba/hybrid 相关 open 问题时，区分 `#35219` 的 cross-dtype stale NaN、`#34874` 的 prefix metadata buffer、以及 MTP/spec decode 的 kernel-selection 问题。
- 对 `#31341` 后续 review 里提到的 `async_output_copy_stream` / `ForwardContext` 传播方案保持关注；若后续再改 hook 位置或等待流，需要确认不会破坏当前 merged 的时序保证。
- 追踪 `#44395` 是否出现 linked fix；若后续有 patch，确认 partial wake_up 后 engine 是否拒绝 forward，或 KV cache allocation 生命周期是否被显式 gate。
