# vllm-project/vllm#28160: [Feature]: Supporting tiny / base other variants through mm-processor-kwargs for deepseek-OCR

| 字段 | 值 |
| --- | --- |
| Issue | [#28160](https://github.com/vllm-project/vllm/issues/28160) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Supporting tiny / base other variants through mm-processor-kwargs for deepseek-OCR

### Issue 正文摘录

### 🚀 The feature, motivation and pitch If i understand correctly, the default is gundam mode. https://github.com/vllm-project/vllm/blob/ffb08379d8870a1a81ba82b72797f196838d0c86/vllm/transformers_utils/processors/deepseek_ocr.py#L12-L21 for faster inference, if the user wants to enable tiny mode, right now, there isn't an option.. Sidenote, based on the tweet here https://x.com/vanstriendaniel/status/1981077499137155140 it seems like `resolution-mode=base` and others are supported however I'm not sure if they're passed to vLLM ever ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: base other variants through mm-processor-kwargs for deepseek-OCR feature request;stale ### 🚀 The feature, motivation and pitch If i understand correctly, the default is gundam mode. https://github.com/vllm-project/vllm/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
