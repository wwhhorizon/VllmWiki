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
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | PR 修复 `BlockTable` row tail 未清零：row 被较短请求复用或成为 `move_row` target 时，旧 block id 留在 tail；changed files 增加 concurrent prefill determinism test 和 700 行 block table unit tests。issue 评论确认该 PR 修复了 #39589。review comment 进一步指出：一旦 tail-zero invariant 成立，`move_row` 可以整行复制并在 `src == tgt` 时跳过。 | row reuse / `move_row` 必须清理 `num_blocks_per_row` 之外的 tail；KV metadata 的核心契约是“逻辑长度之后必须为零”。`move_row` 整行复制是性能/简化建议，不是未修复 correctness 缺口。 |
| [#39146](https://github.com/vllm-project/vllm/issues/39146), [#39283](https://github.com/vllm-project/vllm/pull/39283), [#43741](https://github.com/vllm-project/vllm/pull/43741) | FullAttentionSpec 的 recycled KV cache blocks 未清零，导致标准 attention 在 `temperature=0` 下非确定。`#39283` 先把 `needs_kv_cache_zeroing` 从 Mamba-only 扩展到 FullAttention，但 review 指出 `type(...) is FullAttentionSpec` 会漏掉 MLA/Sink/TQ 等子类。`#43741` 把问题拆成两个 gate：`kv_cache_interface.py` 必须让所有 FullAttentionSpec group 需要 zeroing，`single_type_kv_cache_manager.py` 必须用 `isinstance` 把所有子类的新 block id 送入 zeroing pipeline。 | block reuse 前必须清理 stale data，不只 Mamba 路径需要 zeroing；而且“需要 zeroing”和“把新分配 block id 交给 zeroing pipeline”是两个不同契约，缺任意一个都会读到旧生命周期的 K/V。 |
| [#35219](https://github.com/vllm-project/vllm/pull/35219) | merged PR 修复 hybrid Mamba/attention 共享 block pool 的 NaN 污染：Qwen3.5 类模型中，fp32 Mamba/SSM state block 被重新分配给 fp8/fp16 full-attention KV 时，旧 bit pattern 可被解释成 NaN/Inf；FlashAttention3、FlashInfer-TRTLLM 等 attention kernel 用 multiply-by-zero mask 处理未用位置，但 `0 * NaN` 仍是 NaN。PR 在 scheduler 侧跟踪本 step 新分配的 `FullAttentionSpec` block id，在 worker `_update_states()` 中用单个 Triton kernel 清零对应 GPU memory；该路径只在 `has_mamba_layers` 的 hybrid 模型下启用，prefix-cache hit block 不清零。 | KV block 的 identity 还包括“上一生命周期的 dtype 解释方式”。当同一物理 block 可在 Mamba fp32 state 与 attention fp8/fp16 KV 间复用时，block reuse 前必须清除跨 dtype stale bits；但当前结论是 hybrid-scoped zeroing，不是所有 attention block 的通用 zeroing policy。 |
| [#30931](https://github.com/vllm-project/vllm/issues/30931), [#31069](https://github.com/vllm-project/vllm/pull/31069) | LoRA prefix cache hash 使用 `lora_name` 而非全局唯一 `lora_int_id`，同名不同 ID adapter 会错误共享 cache block。 | adapter identity 是 KV cache key 的必填维度。 |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) | LMCache external KV key 包含 base model、token IDs/chunk hashes、token range、rank/world、`cache_salt`，但缺少 LoRA adapter identity/version；issue body 明确列出 `LMCacheMPRequestTracker` 和 `IPCCacheEngineKey` 都没有 adapter 字段。评论给出 unpatched vs patched connector 对照：unpatched 下 adapter B 首次请求命中 adapter A 的 chunks，patched connector 将 `lora_name` 折入 key 后不再 cross-hit。评论还指出 LMCache 的 LoRA-aware keying POC 可能只覆盖 V1 path，未覆盖 `LMCacheMPConnector` 和 vLLM vendored copy。 | external KV connector 不能只按 token/salt 复用 KV；复现证据很强，但仍缺上游 MP connector fix、vLLM vendored connector patch 和 regression test，保持 defer。 |
| [#42125](https://github.com/vllm-project/vllm/issues/42125) | same-name runtime LoRA reload 下，adapter A warmed prefix cache 后用 `/v1/load_lora_adapter load_inplace=true` 或 unload/reload 替换成 adapter B，同 prompt 返回 `BETA_VERSION_B` 而不是 cold B 的 `BETA_ADAPTER_VERSION_B`；禁用 prefix cache、改变 `cache_salt`、修改第一 prompt block、重启后 cold B、或用 unique adapter name 都恢复正确输出。issue 还指出 runtime path 可能复用 `lora_int_id` 且 prefix-cache key 只含 `lora_name`，缺 adapter path/content hash/runtime generation。 | 这是 adapter-version cache identity 的强 defer：复现矩阵足以支持“same-name reload 没有让 adapter-dependent KV 失效或 versioned”的方向，但本地证据缺 linked PR、changed files、maintainer resolution 和 regression test，不能 promotion 为已修复机制。 |

## 根因机制

KV identity 失败通常来自状态身份建模不完整。cache key 少一个维度、metadata tail 没清理、block reuse 没 zero、offload ownership 混淆，都会让下游 attention 读取错误语义的 K/V。由于 KV 会参与后续所有 decode step，这类错误常表现为 nondeterministic token，而不是局部 tensor mismatch。

`#39146/#43741` 说明 recycled-block zeroing 不是一个布尔开关能解决的单点问题：cache config 要声明该 spec family 需要 zeroing，allocator/manager 还要持续收集新分配或复用的 block id。前者遗漏 FullAttention 会让标准 attention 完全不走 zeroing；后者用精确 `type` 判断会让 FullAttentionSpec 子类悄悄绕开 zeroing 队列。

`#35219` 补充了 cross-dtype block reuse 的根因：同一 block pool 里，Mamba state 与 attention KV 对同一字节序列的 dtype 解释不同。attention kernel 即使用 mask 忽略未用位置，也可能通过 `0 * NaN` 把旧 Mamba bit pattern 传播到所有共享该 KV block 的请求。因此修复点不是 sampler，也不是某个请求的 NaN 过滤，而是“新分配给 attention 的 block 在使用前必须处于零态”。

`#42125` 把 adapter identity 进一步推进到 runtime version 层：即使 `lora_name` 不变，adapter 权重内容也可能已经被热替换。此时仅按 adapter name 或复用旧 `lora_int_id` 建 cache key，都会让新 adapter 读取旧 adapter 权重产生的 prefix KV。`cache_salt`、first-block 变化和 unique-name control 能恢复正确输出，说明问题集中在 cache namespace/invalidating，而不是 sampler 随机性。

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

## 验证契约

- metadata 层：block table tail、row move、clear row、append row 必须有 unit tests。
- 系统层：concurrent variable-length prefill 在 `temperature=0` 下输出 token 稳定。
- block-table invariant 层：一旦证明所有 row tail 恒为零，`move_row` 的整行复制与 slice+tail-zero 在 correctness 上等价；review 优化建议不能被误读成仍有 KV identity 漏洞。
- adapter 层：同 base model、同 token、同 `cache_salt`、不同 LoRA/adapters 不能共享 KV 命中；同 adapter 第二次请求仍应命中，证明修复没有禁用正常复用。patched/unpatched connector 对照是有力证据，但不能替代上游 regression test。
- runtime adapter 层：同名 A->B 热替换、unload/reload same name、unique-name control、changed `cache_salt`、changed first prompt block、no-prefix-cache control 都应覆盖；若 claim 是 version-aware key，还要证明同 adapter 仍可正常复用。
- recycled-block 层：对 FullAttentionSpec、TQFullAttentionSpec、MLAAttentionSpec、SinkFullAttentionSpec 都要断言需要 zeroing，并断言 allocator/manager 会记录新 block id；SlidingWindow/CrossAttention 等不共享同一风险的 spec 不应被误纳入。
- hybrid Mamba/attention 层：覆盖 fp32 SSM state 与 fp8/fp16 KV cache dtype 组合、prefix-cache hit 不被清零、fresh allocation 被清零、FlashAttention/FlashInfer 类 mask kernel 不再传播 stale NaN；性能验证要记录 prefill/decode zeroing 开销。
- KV identity 测试优先使用 exact equality 或 token equality，不能只用宽松 `allclose`。

## 适用边界

- [#39591](https://github.com/vllm-project/vllm/pull/39591) 直接覆盖 V1 + FlashInfer + variable-length concurrent prefill 的 row tail 问题；当前本地证据中 PR 仍 open/unmerged，因此只能说机制和 patch 证据闭环，不能说已 landed。其他 backend 仍需复核相同 metadata invariant。
- [#43741](https://github.com/vllm-project/vllm/pull/43741) 当前本地证据仍 open/unmerged；PR body 的 fuzzer traces 证明 unpatched v0.19.0 可复现，unit tests 覆盖 spec gate 与 manager tracking，但 patched end-to-end validation 需要从源码 build 才能完全闭环。因此结论应写成 include-with-boundary，而不是已 landed fix。
- [#35219](https://github.com/vllm-project/vllm/pull/35219) 已 merged，适用范围是有 Mamba layers 的 hybrid 模型、freshly allocated `FullAttentionSpec` block、以及 Mamba fp32 state 可能污染 attention KV 的共享 pool。本地 targeted evidence 缺少被修复 issue `#35138` 的 JSON，因此该条依赖 PR body、patch、review 和测试结果闭环，而不是 issue body 闭环。它不清 Mamba/SSM blocks，不清 prefix-cache hit blocks，也不是对非 hybrid 部署的默认行为改变。patch 中 `type(self.kv_cache_spec) is FullAttentionSpec` 的精确类型判断符合该 PR 的窄范围，但不要把它外推成覆盖所有 FullAttentionSpec 子类的通用 zeroing fix。
- [#44250](https://github.com/vllm-project/vllm/issues/44250) 已有端到端复现和 patched connector 对照，但没有上游 MP connector fix PR。评论提到的 LoRA-aware POC 若只覆盖 V1 path，仍不能证明 MP connector 路径已修复；评论中的 `lora_name` patch 只能证明“缺 adapter 维度”这个 root-cause 方向，不能证明最终 key schema 已稳定。因此只能作为强 defer，不作为已修复结论。
- [#42125](https://github.com/vllm-project/vllm/issues/42125) 是 open issue，只有 issue body 和一条待复现评论；虽然复现矩阵很强，但没有上游 patch/test 前，不能把“加入 adapter version 或 cache invalidation”写成已落地 fix。
- LoRA identity 与 external KV identity 应同时检查本地 cache key 和远端/cache connector key。

## 仍需补证

- 继续等待或寻找 `#44250` 的 linked fix PR、LMCache MP key schema patch、vLLM vendored connector patch 和 regression test。
- 复核 external KV cache 与 LoRA/adapter version 的边界：adapter reload、同名不同内容、同名不同 ID、cache_salt 复用、multi-rank chunk hash。
- 对 `#42125` 寻找 linked fix PR；重点看 runtime load/unload 是否触发 prefix-cache eviction、cache key 是否纳入 adapter content/version/generation、以及 same-name reload 的 negative regression test。
- 追踪 `#43741` 是否合并；若出现最终 patch，确认 `CrossAttentionSpec`、`SlidingWindowSpec` 等非目标 spec 没被过度 zeroing，避免把性能成本扩大到无风险路径。
- 继续复核 Mamba/hybrid 相关 open 问题时，区分 `#35219` 的 cross-dtype stale NaN、`#34874` 的 prefix metadata buffer、以及 MTP/spec decode 的 kernel-selection 问题。
