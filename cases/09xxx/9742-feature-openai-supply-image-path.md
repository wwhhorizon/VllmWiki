# vllm-project/vllm#9742: [Feature]: OpenAI supply image path

| 字段 | 值 |
| --- | --- |
| Issue | [#9742](https://github.com/vllm-project/vllm/issues/9742) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: OpenAI supply image path

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi! I need a low-latency vision API endpoint. The current vLLM endpoint takes about 200ms (100ms for smaller images) to process a base64 image (provided via `image_url` as base64). I need to cut that number down to almost zero (I checked it against cached web URL images which have almost no latency) Would it be possible to implement that one can also supply an absolute path to an image? All my images are local anyways. ### Alternatives The alternative would be to somehow optimize the base64 parsing, but I don't know if that's possible ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ion API endpoint. The current vLLM endpoint takes about 200ms (100ms for smaller images) to process a base64 image (provided via `image_url` as base64). I need to cut that number down to almost zero (I checked it agains...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: eature request ### 🚀 The feature, motivation and pitch Hi! I need a low-latency vision API endpoint. The current vLLM endpoint takes about 200ms (100ms for smaller images) to process a base64 image (provided via `image_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: OpenAI supply image path feature request ### 🚀 The feature, motivation and pitch Hi! I need a low-latency vision API endpoint. The current vLLM endpoint takes about 200ms (100ms for smaller images) to process...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
