# vllm-project/vllm#28016: [Usage]: How to recognize PDFs in DeepSeek-OCR with openai

| 字段 | 值 |
| --- | --- |
| Issue | [#28016](https://github.com/vllm-project/vllm/issues/28016) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to recognize PDFs in DeepSeek-OCR with openai

### Issue 正文摘录

### Your current environment ``` vllm serve deepseek-ai/DeepSeek-OCR --logits_processors vllm.model_executor.models.deepseek_ocr.NGramPerReqLogitsProcessor --no-enable-prefix-caching --mm-processor-cache-gb 0 ``` ### How would you like to use vllm How to recognize PDFs and convert PDFs to Markdown with DeepSeek-OCR via an OpenAI-compatible API? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: PI? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ronment ``` vllm serve deepseek-ai/DeepSeek-OCR --logits_processors vllm.model_executor.models.deepseek_ocr.NGramPerReqLogitsProcessor --no-enable-prefix-caching --mm-processor-cache-gb 0 ``` ### How would you like to u...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
