# vllm-project/vllm#27936: [Feature]: Add as an online service endpoint for the OCR model like "/ocr"

| 字段 | 值 |
| --- | --- |
| Issue | [#27936](https://github.com/vllm-project/vllm/issues/27936) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add as an online service endpoint for the OCR model like "/ocr"

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Add an online service endpoint for the OCR model to provide simple online services with dedicated OCR interfaces for LLM based ocr models, such as DeepSeek-OCR, PaddleOCR-VL, LightOnOCR, and GOTOCR, just like the speech-to-text endpoint, rather than only providing offline OCR interfaces ### Alternatives Request just like ```python class OCRRequest(OpenAIBaseModel): model: str image: str prompt: str ``` Response just like ```python class OCRResponse(OpenAIBaseModel): text: str model: str usage: dict ``` ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Add as an online service endpoint for the OCR model like "/ocr" feature request ### 🚀 The feature, motivation and pitch Add an online service endpoint for the OCR model to provide simple online services with...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Add as an online service endpoint for the OCR model like "/ocr" feature request ### 🚀 The feature, motivation and pitch Add an online service endpoint for the OCR model to provide simple online services with dedicated O...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
