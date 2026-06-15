# vllm-project/vllm#5193: [Usage]: How can I deploy llama3-70b on a server with 8 3090 GPUs with lora and CUDA graph.

| 字段 | 值 |
| --- | --- |
| Issue | [#5193](https://github.com/vllm-project/vllm/issues/5193) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How can I deploy llama3-70b on a server with 8 3090 GPUs with lora and CUDA graph.

### Issue 正文摘录

### Your current environment None ### How would you like to use vllm I hope to deploy the llama3-70b model on a server with 8 3090 GPUs. When I enable the enable_lora switch, the system will definitely exceed the memory limit (even if the context length is reduced to 128) as long as I do not enable the enforce_eager flag. However, when I disable enable_lora, it takes about 85% of the memory to run. I would like to know the difference in memory consumption of CUDA graph when lora is enabled and when it is not. In this situation, how can I enable CUDA graph acceleration for the model without exceeding the memory limit?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How can I deploy llama3-70b on a server with 8 3090 GPUs with lora and CUDA graph. usage;stale ### Your current environment None ### How would you like to use vllm I hope to deploy the llama3-70b model on a ser...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: : How can I deploy llama3-70b on a server with 8 3090 GPUs with lora and CUDA graph. usage;stale ### Your current environment None ### How would you like to use vllm I hope to deploy the llama3-70b model on a server wit...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: llama3-70b on a server with 8 3090 GPUs with lora and CUDA graph. usage;stale ### Your current environment None ### How would you like to use vllm I hope to deploy the llama3-70b model on a server with 8 3090 GPUs. When...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
