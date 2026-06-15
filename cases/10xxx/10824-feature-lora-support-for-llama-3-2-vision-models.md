# vllm-project/vllm#10824: [Feature]: LoRA support for LLama 3.2 Vision Models

| 字段 | 值 |
| --- | --- |
| Issue | [#10824](https://github.com/vllm-project/vllm/issues/10824) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: LoRA support for LLama 3.2 Vision Models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I tried loading finetuned LoRA for llama 3.2 11B vision instruct using the serve command (OpenAI client) and get this error message. ```shell ERROR 12-02 00:02:57 engine.py:366] NotImplementedError: LoRA is currently not currently supported with encoder/decoder models. ``` I finetuned the LoRA using unsloth's implementation. It would be great if we can have the support for LoRA for multimodal models as our team wants to use multiple LoRAs and merging the LoRA adapters to original model weights is not feasible for us. We are short on time for this project and as far as I can tell no other framework supports LoRA in this way. Also we need outlines for structured generation so vLLM (being the most user friendly, stable and mature framework ) is our best bet now. Can we get a timeline when will this be supported ? Also are there any workarounds possible until this feature is officially supported ? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: LoRA support for LLama 3.2 Vision Models feature request;stale ### 🚀 The feature, motivation and pitch I tried loading finetuned LoRA for llama 3.2 11B vision instruct using the serve command (OpenAI client)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: LoRA support for LLama 3.2 Vision Models feature request;stale ### 🚀 The feature, motivation and pitch I tried loading finetuned LoRA for llama 3.2 11B vision instruct using the serve command (OpenAI client)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rted ? Also are there any workarounds possible until this feature is officially supported ? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you al...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: supported with encoder/decoder models. ``` I finetuned the LoRA using unsloth's implementation. It would be great if we can have the support for LoRA for multimodal models as our team wants to use multiple LoRAs and mer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
