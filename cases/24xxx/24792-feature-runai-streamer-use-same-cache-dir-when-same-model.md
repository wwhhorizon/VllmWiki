# vllm-project/vllm#24792: [Feature]: runai_streamer use same cache dir when same model

| 字段 | 值 |
| --- | --- |
| Issue | [#24792](https://github.com/vllm-project/vllm/issues/24792) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: runai_streamer use same cache dir when same model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Current use runai_streamer load_format, we can save model config.json and other config file to local tmp dir, but every running will use new tmp director, we whether can use same tmp dir in same model. this path like we can use `/tmp/qwen3/qwen3-0.6`. And we can use ENV to customer define this path prefix. https://github.com/vllm-project/vllm/blob/7f2ea7074e4c2ee75278623a02007fc1b6bb9639/vllm/transformers_utils/runai_utils.py#L61-L66 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: runai_streamer use same cache dir when same model feature request ### 🚀 The feature, motivation and pitch Current use runai_streamer load_format, we can save model config.json and other config file to local t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: runai_streamer use same cache dir when same model feature request ### 🚀 The feature, motivation and pitch Current use runai_streamer load_format, we can save model config.json and other config file to local t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
