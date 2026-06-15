# vllm-project/vllm#34355: [Feature]: Detect langue for Whisper

| 字段 | 值 |
| --- | --- |
| Issue | [#34355](https://github.com/vllm-project/vllm/issues/34355) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;multimodal_vlm |
| 子分类 | cold_start |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Detect langue for Whisper

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **Motivation** The addition of a language detection feature to the Whisper model will enhance its usability by automatically identifying the language of the audio input before transcription. This is especially useful for multilingual environments where the language of the input audio might not always be known in advance. By integrating language detection directly into the transcription pipeline, we can streamline the process and make it more efficient for users who work with diverse languages. **Code Summary:** The code introduces a language detection feature in the WhisperForConditionalGeneration class, specifically modifying the transcription pipeline to automatically detect the language of the input audio. **Key Changes:** **Modification of the forward method:** The forward method in the WhisperForConditionalGeneration class has been updated to incorporate language detection before proceeding with the transcription. It now includes additional logic to detect the language token at the start of the input sequence. This change ensures that the model processes the Start-of-Transcription (SOT) token to predict the language before running the f...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ost likely language token. The method is designed to be used outside the CUDA graph capture, ensuring it doesn’t interfere with the graph execution. It takes in encoder_outputs and determines the most likely language ba...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Motivation** The addition of a language detection feature to the Whisper model will enhance its usability by automatically identifying the language of the audio input before transcription. This is especially useful for...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ontext A warmup mechanism is planned to be added in order to reduce the latency of the first request after model initialization. Currently, when the model is first loaded, it may take some time to initialize, especially...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ifying the language of the audio input before transcription. This is especially useful for multilingual environments where the language of the input audio might not always be known in advance. By integrating language de...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Detect langue for Whisper feature request ### 🚀 The feature, motivation and pitch **Motivation** The addition of a language detection feature to the Whisper model will enhance its usability by automatically i...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
