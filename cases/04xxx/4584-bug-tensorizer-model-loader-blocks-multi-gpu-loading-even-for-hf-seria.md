# vllm-project/vllm#4584: [Bug]: Tensorizer model loader blocks multi-GPU loading even for HF serialized models

| 字段 | 值 |
| --- | --- |
| Issue | [#4584](https://github.com/vllm-project/vllm/issues/4584) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Tensorizer model loader blocks multi-GPU loading even for HF serialized models

### Issue 正文摘录

### Your current environment Running inside an OpenShift cluster, but not directly relevant for the issue in question. ### 🐛 Describe the bug At https://github.com/vllm-project/vllm/blob/2d7bce9cd5981db146b18a8a95c5a7e0480687bd/vllm/model_executor/model_loader/tensorizer.py#L74-L80 the tensorizer loader checks if `tensor_parallel_size` is greater than 1 and if `tensorizer_uri` is set and if so raises an error. However, the error description indicates that this should work for non-vLLM serialized models, such as using the tensorizer library directly to serialize a HuggingFace model. If the error message is correct, and multiple GPUs isn't supported only for vLLM-serialized tensorizer loads, then it should be checking if the `vllm_tensorized` boolean is set to `true` instead of the `tensorizer_uri` string in the check. That would enable using multiple GPUs with the tensorized model loader, as long as the tensors weren't serialized by vLLM itself.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Tensorizer model loader blocks multi-GPU loading even for HF serialized models bug;stale ### Your current environment Running inside an OpenShift cluster, but not directly relevant for the issue in question. ###...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: Tensorizer model loader blocks multi-GPU loading even for HF serialized models bug;stale ### Your current environment Running inside an OpenShift cluster, but not directly relevant for the issue in question. ###...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: model loader blocks multi-GPU loading even for HF serialized models bug;stale ### Your current environment Running inside an OpenShift cluster, but not directly relevant for the issue in question. ### 🐛 Describe the bug...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
