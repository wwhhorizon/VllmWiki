# vllm-project/vllm#5128: [Feature]: How to Enable VLLM to Work with PreTrainedModel Objects in my MOE-LoRA?  THX

| 字段 | 值 |
| --- | --- |
| Issue | [#5128](https://github.com/vllm-project/vllm/issues/5128) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: How to Enable VLLM to Work with PreTrainedModel Objects in my MOE-LoRA?  THX

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I have fine-tuned multiple LoRA models to act as expert layers within an MOE architecture. How can I leverage a VLLM to accelerate this? Currently, VLLM acceleration, such as LLM(model_path), only supports model paths. However, my MOE constitutes an architecture itself. How can I adapt VLLM, for instance, to support loading a model object with LLM(model_obj), where the object type could be PreTrainedModel? ### Alternatives Train a custom MOE model and configure it as a new model type, custom model within VLLM, enabling acceleration through parameter settings. ### Additional context base model is llama/bloomz/qwen ，etc.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: How to Enable VLLM to Work with PreTrainedModel Objects in my MOE-LoRA? THX feature request;stale ### 🚀 The feature, motivation and pitch I have fine-tuned multiple LoRA models to act as expert layers within...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: How to Enable VLLM to Work with PreTrainedModel Objects in my MOE-LoRA? THX feature request;stale ### 🚀 The feature, motivation and pitch I have fine-tuned multiple LoRA models to act as expert layers within...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e VLLM to Work with PreTrainedModel Objects in my MOE-LoRA? THX feature request;stale ### 🚀 The feature, motivation and pitch I have fine-tuned multiple LoRA models to act as expert layers within an MOE architecture. Ho...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ve fine-tuned multiple LoRA models to act as expert layers within an MOE architecture. How can I leverage a VLLM to accelerate this? Currently, VLLM acceleration, such as LLM(model_path), only supports model paths. Howe...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: rough parameter settings. ### Additional context base model is llama/bloomz/qwen ，etc.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
