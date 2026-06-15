# vllm-project/vllm#8458: [Bug]: How can I run VLLM serving without an internet connection?  I tried setting the global variable but it still trying to connect to huggingface

| 字段 | 值 |
| --- | --- |
| Issue | [#8458](https://github.com/vllm-project/vllm/issues/8458) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: How can I run VLLM serving without an internet connection?  I tried setting the global variable but it still trying to connect to huggingface

### Issue 正文摘录

### Your current environment as title ### Model Input Dumps _No response_ ### 🐛 Describe the bug can't run without internet ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ? I tried setting the global variable but it still trying to connect to huggingface bug;stale ### Your current environment as title ### Model Input Dumps _No response_ ### 🐛 Describe the bug can't run without internet #...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: net ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ng the global variable but it still trying to connect to huggingface bug;stale ### Your current environment as title ### Model Input Dumps _No response_ ### 🐛 Describe the bug can't run without internet ### Before submi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
