# vllm-project/vllm#30105: [Feature]: Extend Dual Batch Overlap (DBO) to Multi-Batch Overlap (XBO)

| 字段 | 值 |
| --- | --- |
| Issue | [#30105](https://github.com/vllm-project/vllm/issues/30105) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Extend Dual Batch Overlap (DBO) to Multi-Batch Overlap (XBO)

### Issue 正文摘录

## Description Currently, the Dual Batch Overlap (DBO) implementation in vLLM hardcodes the number of microbatches to 2, which limits its applicability to only dual-batch overlap scenarios (e.g., wide EP use cases). The core microbatch slicing capabilities (e.g., `UBatchSlice`, `UBatchWrapper`) underlying DBO are generic and reusable for **multi-microbatch overlap scenarios** (beyond 2 microbatches). For example: - AF (Attention/Feed-forward) Disaggregation #22799 #29772 scenarios may require 3, 4, or more microbatches to be sliced and overlapped. - Other emerging multi-batch overlap use cases would benefit from a generalized microbatch slicing framework. Extending DBO to a flexible Multi-Batch Overlap (XBO) design (where "X" represents a configurable number of microbatches) will: 1. Unlock support for multi-microbatch overlap scenarios 2. Decouple microbatch slicing logic from hardcoded batch counts 3. Make the core slicing capabilities a shared, reusable component in the codebase ## Proposed Solution I plan to refactor the existing DBO code to: - Replace hardcoded references to "2 microbatches" with a configurable parameter (e.g., `num_microbatches`) - Generalize `UBatchSlice`,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ch overlap scenarios (e.g., wide EP use cases). The core microbatch slicing capabilities (e.g., `UBatchSlice`, `UBatchWrapper`) underlying DBO are generic and reusable for **multi-microbatch overlap scenarios** (beyond...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: O to a flexible Multi-Batch Overlap (XBO) design (where "X" represents a configurable number of microbatches) will: 1. Unlock support for multi-microbatch overlap scenarios 2. Decouple microbatch slicing logic from hard...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e]: Extend Dual Batch Overlap (DBO) to Multi-Batch Overlap (XBO) feature request ## Description Currently, the Dual Batch Overlap (DBO) implementation in vLLM hardcodes the number of microbatches to 2, which limits its...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
