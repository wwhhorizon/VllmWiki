# 并发下的 KV Cache Identity

状态：curated。
父页：[Bitwise 确定性与数值等价](README.md)。
范围：并发、offload、prefix sharing、LoRA/external KV、block reuse 和 metadata cleanup 下的 KV 身份一致性。

## TL;DR

KV cache block 必须只代表它真实对应的 prompt、token range、model、adapter、dtype、layout、backend、cache group 和请求状态。任何请求读取到其他请求、其他 adapter 或旧生命周期的 KV，都是 correctness bug。KV identity 不只包括 key，还包括 block table tail、offload copy 时序、adapter version、metadata pointer 和 allocation 生命周期。external KV / LoRA identity 的未闭环项见 [next.md](next.md)。

## 机制解释

KV identity 失败通常来自状态身份建模不完整。cache key 少一个维度、metadata tail 没清理、block reuse 没 zero、offload ownership 混淆，都会让下游 attention 读取错误语义的 K/V。由于 KV 参与后续所有 decode step，这类错误常表现为 nondeterministic token，而不是局部 tensor mismatch。

runtime LoRA 与 external KV 把问题推进到 version/schema 层。本地 prefix cache 可以使用 loader-effective content identity；跨仓 external KV 还需要决定 adapter 维度到底落在统一 key schema 的哪一层。

## 稳定证据

- upstream id: [#39589](https://github.com/vllm-project/vllm/issues/39589), [#39591](https://github.com/vllm-project/vllm/pull/39591)
- upstream status: issue plus open PR
- claim level: include with boundary
- direct evidence: variable-length concurrent prefill 在 `temperature=0` 下不稳定；patch 指向 stale block_table tail。
- mechanism: block table tail / row move 是 KV read/write identity 的一部分。
- boundary: PR 仍 open；move_row 整行复制是性能/简化建议，不是 correctness 阻塞。

- upstream id: [#35219](https://github.com/vllm-project/vllm/pull/35219)
- upstream status: merged PR
- claim level: stable
- direct evidence: hybrid Mamba/attention 共享 block pool 中，fp32 Mamba state 复用为 fp8/fp16 attention KV 会传播 stale NaN；PR 跟踪新分配 FullAttentionSpec block 并清零。
- mechanism: KV block identity 包括上一生命周期的 dtype 解释。
- boundary: hybrid-scoped zeroing，不是所有 attention block 的通用 zeroing policy。

- upstream id: [#30931](https://github.com/vllm-project/vllm/issues/30931), [#31069](https://github.com/vllm-project/vllm/pull/31069)
- upstream status: issue plus PR evidence
- claim level: stable
- direct evidence: LoRA prefix cache hash 使用 `lora_name` 而非全局唯一 `lora_int_id`，同名不同 ID adapter 错误共享 cache block。
- mechanism: adapter identity 是 KV cache key 的必填维度。
- boundary: `lora_int_id` 解决本地 identity，不等于 external KV 的跨进程 stable version schema。

- upstream id: [#31210](https://github.com/vllm-project/vllm/issues/31210), [#31341](https://github.com/vllm-project/vllm/pull/31341)
- upstream status: merged PR
- claim level: stable
- direct evidence: PR 让 offload stream 等待 compute stream，并把 store job 延后到下一 engine step。
- mechanism: offload identity 包括 copy 时序和 DMA 争用。
- boundary: 后续 copy stream / ForwardContext 改动仍需复核。

- upstream id: [#42125](https://github.com/vllm-project/vllm/issues/42125), [#45981](https://github.com/vllm-project/vllm/pull/45981)
- upstream status: issue plus open PR
- claim level: defer / mainline gap
- direct evidence: PR 将 local LoRA prefix-cache key 收敛为 loader-effective content identity，并在 request 传播和 block-hash extra keys 中消费。
- mechanism: same-name reload 需要内容派生 adapter identity，不能只看 name、path 或进程内 counter。
- boundary: PR 仍 open，source/部署边界和 upstream 接受度未闭环。

## 边界与反例

- `#44250/#45549` 与 LMCache `#2962` 仍是跨仓 schema 缺口：vLLM MP connector internal salt 只是局部层，single source of truth 尚未定案。
- `#37076/#37152/#42359` 是 same-step registration visibility 的 contested hypothesis；open PR 可作为 patch 方向，不能写成 landed mechanism。
- `#39146/#43741` 提示 recycled-block zeroing scope 可能超出 hybrid Mamba，但 PR 仍 open，不能覆盖为已发布 fix。
- `#44395`、`#42903`、`#41995` 分别是 allocation lifecycle、offload dedup、metadata pointer width 的 open 边界。

## Evidence appendix

长证据表、KV identity matrix 和补证记录见 [evidence_appendix/kv_cache_identity_concurrency.md](evidence_appendix/kv_cache_identity_concurrency.md)。
