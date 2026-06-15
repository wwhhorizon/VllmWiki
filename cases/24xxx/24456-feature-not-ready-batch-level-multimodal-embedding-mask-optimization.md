# vllm-project/vllm#24456: [Feature][not ready]: Batch-Level Multimodal Embedding Mask Optimization

| 字段 | 值 |
| --- | --- |
| Issue | [#24456](https://github.com/vllm-project/vllm/issues/24456) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][not ready]: Batch-Level Multimodal Embedding Mask Optimization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # 1. Motivation Currently, merge_multimodal_embeddings scans input_ids individually for each request to find placeholder tokens. This is inefficient because the scheduler already has mm_positions data for all requests. We should pre-compute a batch-level mask (like grammar_bitmask) instead of scanning at runtime. [The Problem](https://github.com/ywang96/vllm/blob/60f0843ef8fb4b0c4e6788acc042873a0a2ea2a1/vllm/model_executor/models/utils.py#L478C2-L478C32) 1. torch.isin(input_ids, placeholder_token_id) - Scans entire input_ids tensor to find multiple placeholder tokens 2. (input_ids == placeholder_token_id) - Scans entire input_ids tensor to find single placeholder token # 2. Proposed Changes Phase 1: Core Function + Test - [ ] Add merge_multimodal_embeddings_with_mask() function to utils (/vllm/model_executor/models/utils.py) - [ ] Add unit test Phase 2: Integration - [ ] Add mask generation from mm_positions to scheduler - [ ] Replace scanning calls with mask version #23891 #16229 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: individually for each request to find placeholder tokens. This is inefficient because the scheduler already has mm_positions data for all requests. We should pre-compute a batch-level mask (like grammar_bitmask) instead...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature][not ready]: Batch-Level Multimodal Embedding Mask Optimization feature request ### 🚀 The feature, motivation and pitch # 1. Motivation Currently, merge_multimodal_embeddings scans input_ids individually for ea...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ][not ready]: Batch-Level Multimodal Embedding Mask Optimization feature request ### 🚀 The feature, motivation and pitch # 1. Motivation Currently, merge_multimodal_embeddings scans input_ids individually for each reque...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: placeholder token # 2. Proposed Changes Phase 1: Core Function + Test - [ ] Add merge_multimodal_embeddings_with_mask() function to utils (/vllm/model_executor/models/utils.py) - [ ] Add unit test Phase 2: Integration -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
