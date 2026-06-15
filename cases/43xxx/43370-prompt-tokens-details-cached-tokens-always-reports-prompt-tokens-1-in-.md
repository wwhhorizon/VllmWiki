# vllm-project/vllm#43370: prompt_tokens_details.cached_tokens always reports prompt_tokens - 1 in disaggregated prefill/decode mode

| 字段 | 值 |
| --- | --- |
| Issue | [#43370](https://github.com/vllm-project/vllm/issues/43370) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> prompt_tokens_details.cached_tokens always reports prompt_tokens - 1 in disaggregated prefill/decode mode

### Issue 正文摘录

### Your current environment Deployment: disaggregated prefill/decode (PD) ### 🐛 Describe the bug ```markdown ## Summary When running vLLM in disaggregated prefill/decode mode with `--enable-prompt-tokens-details`, the `usage.prompt_tokens_details.cached_tokens` value is always reported as `prompt_tokens - 1`, regardless of whether any prefix cache hit actually occurred. This happens even on the very first request with a unique prompt that cannot possibly have a prefix cache hit. ## Expected behavior `cached_tokens` should reflect actual **prefix cache hits from prior requests** — matching the OpenAI API semantics for this field. For a cold request with no prior matching prefix, `cached_tokens` should be `0` (or at most a small constant if the cache contains a system-prompt prefix). ``` Reproduction 1. Deploy vLLM in disaggregated PD mode (one prefill instance, one decode instance, KV-transfer enabled). 2. Pass --enable-prompt-tokens-details to both instances. 3. Send a chat/completions request with a fresh, unique prompt directly to the decode worker (bypassing any router/proxy). 4. Inspect usage.prompt_tokens_details.cached_tokens in the response. Observed: cached_tokens == prom...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: _details.cached_tokens always reports prompt_tokens - 1 in disaggregated prefill/decode mode bug ### Your current environment Deployment: disaggregated prefill/decode (PD) ### 🐛 Describe the bug ```markdown ## Summary
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: no prior matching prefix, `cached_tokens` should be `0` (or at most a small constant if the cache contains a system-prompt prefix). ``` Reproduction 1. Deploy vLLM in disaggregated PD mode (one prefill instance, one dec...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ported as `prompt_tokens - 1`, regardless of whether any prefix cache hit actually occurred. This happens even on the very first request with a unique prompt that cannot possibly have a prefix cache hit.
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ways reported as `prompt_tokens - 1`, regardless of whether any prefix cache hit actually occurred. This happens even on the very first request with a unique prompt that cannot possibly have a prefix cache hit.
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: th a fresh, unique prompt directly to the decode worker (bypassing any router/proxy). 4. Inspect usage.prompt_tokens_details.cached_tokens in the response.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
