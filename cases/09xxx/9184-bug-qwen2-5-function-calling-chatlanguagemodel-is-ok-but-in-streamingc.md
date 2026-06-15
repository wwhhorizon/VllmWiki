# vllm-project/vllm#9184: [Bug]: qwen2.5 function calling,ChatLanguageModel is ok, but in StreamingChatLanguageModel,the logger report error

| 字段 | 值 |
| --- | --- |
| Issue | [#9184](https://github.com/vllm-project/vllm/issues/9184) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen2.5 function calling,ChatLanguageModel is ok, but in StreamingChatLanguageModel,the logger report error

### Issue 正文摘录

### Your current environment ### Model Input Dumps ![image](https://github.com/user-attachments/assets/039317df-453c-47e2-a449-297df451503b) ### 🐛 Describe the bug qwen2.5 function calling,ChatLanguageModel is ok, but in StreamingChatLanguageModel,the logger report error ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen2.5 function calling,ChatLanguageModel is ok, but in StreamingChatLanguageModel,the logger report error bug;stale ### Your current environment ### Model Input Dumps ![image](https://github.com/user-attachment...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ror ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: del is ok, but in StreamingChatLanguageModel,the logger report error bug;stale ### Your current environment ### Model Input Dumps ![image](https://github.com/user-attachments/assets/039317df-453c-47e2-a449-297df451503b)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
