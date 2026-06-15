# vllm-project/vllm#19739: [Feature]: Logging details about incorrect requests

| 字段 | 值 |
| --- | --- |
| Issue | [#19739](https://github.com/vllm-project/vllm/issues/19739) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Logging details about incorrect requests

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, when doing vibecoding sometimes AI prepares code to call API /chat/completions, which is not correct. But this is not even a problem of my code. I am trying to run Google ADK library to use local model served by vLLM. The problem I am encountering is that either I only get this information: INFO: 10.147.81.70:62614 - "POST /v1/chat/completions HTTP/1.1" 400 Bad Request if e.g. top_p=0 ​​has been set or nothing appears in logs (like for Google ADK). And I know that the message reaches vLLM, because it did just moment ago, but I added something new like e.g. tool calling and it stops working and there is no information in logs. Please provide a more detailed dump if the message cannot be parsed. Especially adding logging in the initial stages where an error occurs causes nothing to appear in the logs. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: a problem of my code. I am trying to run Google ADK library to use local model served by vLLM. The problem I am encountering is that either I only get this information: INFO: 10.147.81.70:62614 - "POST /v1/chat/completi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Logging details about incorrect requests feature request;stale ### 🚀 The feature, motivation and pitch Hi, when doing vibecoding sometimes AI prepares code to call API /chat/completions, which is not correct....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Please provide a more detailed dump if the message cannot be parsed. Especially adding logging in the initial stages where an error occurs causes nothing to appear in the logs. ### Alternatives _No response_ ### Additio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
