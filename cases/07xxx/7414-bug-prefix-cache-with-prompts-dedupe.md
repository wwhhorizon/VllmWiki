# vllm-project/vllm#7414: [Bug]: Prefix cache with prompts dedupe

| 字段 | 值 |
| --- | --- |
| Issue | [#7414](https://github.com/vllm-project/vllm/issues/7414) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Prefix cache with prompts dedupe

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi vLLM experts, This might not be a bug unless I miss something. If two identical new prompts are input at the same time, no preceding same prompt has been given so far and 0 cache hit. BlockSpaceManagerV1 will allocate the same blocks because of the same hashing. Then where is the logic to dedupe the computation, if not, will `reshape_and_cache` update the same kv cache slots simultaneously and lead to concurrent issue?

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: Prefix cache with prompts dedupe bug;stale ### Your current environment ### 🐛 Describe the bug Hi vLLM experts, This might not be a bug unless I miss something. If two identical new prompts are input at the same t
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: me time, no preceding same prompt has been given so far and 0 cache hit. BlockSpaceManagerV1 will allocate the same blocks because of the same hashing. Then where is the logic to dedupe the computation, if not, will `re...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t at the same time, no preceding same prompt has been given so far and 0 cache hit. BlockSpaceManagerV1 will allocate the same blocks because of the same hashing. Then where is the logic to dedupe the computation, if no...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: g;stale ### Your current environment ### 🐛 Describe the bug Hi vLLM experts, This might not be a bug unless I miss something. If two identical new prompts are input at the same time, no preceding same prompt has been gi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Prefix cache with prompts dedupe bug;stale ### Your current environment ### 🐛 Describe the bug Hi vLLM experts, This might not be a bug unless I miss something. If two identical new prompts are input at the same...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
