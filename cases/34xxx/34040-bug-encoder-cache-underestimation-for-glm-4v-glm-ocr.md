# vllm-project/vllm#34040: [Bug]: Encoder cache underestimation for GLM-4V/GLM-OCR

| 字段 | 值 |
| --- | --- |
| Issue | [#34040](https://github.com/vllm-project/vllm/issues/34040) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Encoder cache underestimation for GLM-4V/GLM-OCR

### Issue 正文摘录

## Overview Attempting to run `zai-org/GLM-OCR` from Hugging Face with vLLM for OCR on images extracted from PDF pages. Inference fails due to an encoder cache limit error. ## Environment * Model: zai-org/GLM-OCR * Runtime: vLLM ## Issue Requests with image inputs fail with a multimodal encoder cache overflow when the image token length exceeds the configured encoder cache size in vLLM. ## Error ``` { "error": "All variants failed with errors: glm_ocr: All model providers failed to infer with errors: vllm: Error 400 Bad Request from vllm client: {\"error\":{\"message\":\"The decoder prompt contains a(n) image item with length 6042, which exceeds the pre-allocated encoder cache size 4800. Please reduce the input size or increase the encoder cache size by setting --limit-mm-per-prompt at startup.\",\"type\":\"BadRequestError\",\"code\":400}}" } ``` ## Observed Values * Image token length: 6042 * Encoder cache limit: 4800 ## Suspected Cause Multimodal embeddings generated from the image exceed the encoder cache size allocated by vLLM. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, an...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Inference fails due to an encoder cache limit error. ## Environment * Model: zai-org/GLM-OCR * Runtime: vLLM ## Issue Requests with image inputs fail with a multimodal encoder cache overflow when the image token length...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: or. ## Environment * Model: zai-org/GLM-OCR * Runtime: vLLM ## Issue Requests with image inputs fail with a multimodal encoder cache overflow when the image token length exceeds the configured encoder cache size in vLLM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
