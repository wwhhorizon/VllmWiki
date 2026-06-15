# vllm-project/vllm#8566: [Feature]: Offline quantization for Pixtral-12B

| 字段 | 值 |
| --- | --- |
| Issue | [#8566](https://github.com/vllm-project/vllm/issues/8566) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 |  |
| Operator 关键词 | fp8;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Offline quantization for Pixtral-12B

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In Linux, nvidia driver doesn't provide "shared memory" like windows, which make it impossible to load Pixtral 12B into 3090 or 4090. And since it looks like we don't have any transformers implementation of pixtral, we can only use vllm codebase to load the model. Is it possible that vllm provide an option/API to create offline FP8 quantization through vllm model loader? ### Alternatives Although I suggest a new feature like "making offline quantize through vllm library" If vllm/mistral team can provide offline fp8 ckpt directly it is also good for me. ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#9036 [Model] Support Pixtral models in the HF Transformers format

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ers implementation of pixtral, we can only use vllm codebase to load the model. Is it possible that vllm provide an option/API to create offline FP8 quantization through vllm model loader? ### Alternatives Although I su...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Offline quantization for Pixtral-12B feature request ### 🚀 The feature, motivation and pitch In Linux, nvidia driver doesn't provide "shared memory" like windows, which make it impossible to load Pixtral 12B...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: api;model_support;multimodal_vlm;quantization fp8;quantization dtype;env_dependency #9036 [Model] Support Pixtral models in the HF Transformers format 🚀 The feature, motivation and pitch
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Offline quantization for Pixtral-12B feature request ### 🚀 The feature, motivation and pitch In Linux, nvidia driver doesn't provide "shared memory" like windows, which make it impossible to load Pixtral 12B...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9036](https://github.com/vllm-project/vllm/pull/9036) | closes_keyword | 0.95 | [Model] Support Pixtral models in the HF Transformers format | FIX #8566 FIX #8685 FIX #9069 Introduces `PixtralHF`, which is a model implementing HF's format of Pixtral. Based off https://github.com/huggingface/transformers/blob/main/src |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
