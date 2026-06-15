# vllm-project/vllm#19590: [Feature]: moe_align_block_size optimization opportunity for Expert Parallel case

| 字段 | 值 |
| --- | --- |
| Issue | [#19590](https://github.com/vllm-project/vllm/issues/19590) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: moe_align_block_size optimization opportunity for Expert Parallel case

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In the case of expert_parallel, `moe_align_block_size` initially considers all experts as valid and aligns all tokens appropriately. Before the function returns it marks the experts_ids that are not in the current GPU rank as `-1` so the MoE matmuls could skip those blocks. This is sub-optimal in memory and performance. The solution is to recognize/apply expert_map before or inside `moe_align_block_size` so we allocate less memory do less work. ### Alternatives _No response_ ### Additional context Related bugfix PR - https://github.com/vllm-project/vllm/pull/19515 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: moe_align_block_size optimization opportunity for Expert Parallel case feature request;stale ### 🚀 The feature, motivation and pitch In the case of expert_parallel, `moe_align_block_size` initially considers...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ign_block_size optimization opportunity for Expert Parallel case feature request;stale ### 🚀 The feature, motivation and pitch In the case of expert_parallel, `moe_align_block_size` initially considers all experts as va...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 15 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: moe_align_block_size optimization opportunity for Expert Parallel case feature request;stale ### 🚀 The feature, motivation and pitch In the case of expert_parallel, `moe_align_block_size` initially considers...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
