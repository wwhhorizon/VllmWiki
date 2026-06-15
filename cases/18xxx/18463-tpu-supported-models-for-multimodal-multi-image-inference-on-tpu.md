# vllm-project/vllm#18463: [TPU] Supported models for multimodal multi-image inference on TPU?

| 字段 | 值 |
| --- | --- |
| Issue | [#18463](https://github.com/vllm-project/vllm/issues/18463) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [TPU] Supported models for multimodal multi-image inference on TPU?

### Issue 正文摘录

### Describe your question I would like to know which model(s) are currently supported by vLLM for multimodal, multi-image inference on TPU (Tensor Processing Unit). Specifically, I am interested in models that can handle multiple images per request in a multimodal setting (e.g., vision-language models) and are deployable on TPU hardware. ### What have you tried? I have tried most of the models from the official multi-image example, but most of them do not work as expected. For example, Qwen has known M-ROPE issues, Gemma doesn't work, and for several other models, issues have already been raised. However, I still couldn't find a model that works reliably for multimodal multi-image inference on TPU. ### Have you checked for similar issues? Yes, I have checked all relevant existing issues and could not find a clear answer to this question. ### Additional context If there are any specific model requirements, limitations, or configuration guidelines for running such workloads on TPU, please provide details or documentation references.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [TPU] Supported models for multimodal multi-image inference on TPU? stale ### Describe your question I would like to know which model(s) are currently supported by vLLM for multimodal, multi-image inference on TPU (Tens...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [TPU] Supported models for multimodal multi-image inference on TPU? stale ### Describe your question I would like to know which model(s) are currently supported by vLLM for multimodal, multi-image inference on TPU (Tens...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: or multimodal, multi-image inference on TPU (Tensor Processing Unit). Specifically, I am interested in models that can handle multiple images per request in a multimodal setting (e.g., vision-language models) and are de...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: them do not work as expected. For example, Qwen has known M-ROPE issues, Gemma doesn't work, and for several other models, issues have already been raised. However, I still couldn't find a model that works reliably for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
