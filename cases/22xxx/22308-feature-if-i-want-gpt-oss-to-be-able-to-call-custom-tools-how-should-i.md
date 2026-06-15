# vllm-project/vllm#22308: [Feature]: If I want gpt-oss to be able to call custom tools, how should I set the --tool-call-parser parameter during deployment?

| 字段 | 值 |
| --- | --- |
| Issue | [#22308](https://github.com/vllm-project/vllm/issues/22308) |
| 状态 | closed |
| 标签 | feature request;stale;gpt-oss |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: If I want gpt-oss to be able to call custom tools, how should I set the --tool-call-parser parameter during deployment?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, gpt-oss supports built-in tools. But does it also support Agent tool calls? If so, do I still need to configure the `--tool-call-parser` parameter? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: If I want gpt-oss to be able to call custom tools, how should I set the --tool-call-parser parameter during deployment? feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch Currently, gpt-oss...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: should I set the --tool-call-parser parameter during deployment? feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch Currently, gpt-oss supports built-in tools. But does it also support Agent tool call...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
