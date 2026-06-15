# vllm-project/vllm#16994: [Feature]: Automatically Enable Modality Specific Loras

| 字段 | 值 |
| --- | --- |
| Issue | [#16994](https://github.com/vllm-project/vllm/issues/16994) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Automatically Enable Modality Specific Loras

### Issue 正文摘录

### 🚀 The feature, motivation and pitch There are a few models that have Loras bundled as part of the model which are to be used when processing specific modalities, e.g., - phi4mm (supported in vLLM), which has vision and audio specific Loras - granite speech (contribution to vLLM ongoing), which has an audio specific Lora Currently, users need to explicitly pass a `LoraRequest` with the modality like what is shown [here](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/audio_language.py#L76). This is an awkward experience if the lora is expected to always be enabled when processing specific modalities, and can be error prone if they accidentally forget to pass the lora request, since it'll just seem like the model isn't working well. It would be nice to be able to pass a dictionary mapping modality keys to one or more `LoraRequests` to automatically enable such lora adapters when a given modality is present in the request to avoid this issue. ### Alternatives We continue to pass the lora with each request! ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Automatically Enable Modality Specific Loras feature request ### 🚀 The feature, motivation and pitch There are a few models that have Loras bundled as part of the model which are to be used when processing sp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: el isn't working well. It would be nice to be able to pass a dictionary mapping modality keys to one or more `LoraRequests` to automatically enable such lora adapters when a given modality is present in the request to a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: feature request ### 🚀 The feature, motivation and pitch There are a few models that have Loras bundled as part of the model which are to be used when processing specific modalities, e.g., - phi4mm (supported in vLLM), w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Automatically Enable Modality Specific Loras feature request ### 🚀 The feature, motivation and pitch There are a few models that have Loras bundled as part of the model which are to be used when processing sp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
