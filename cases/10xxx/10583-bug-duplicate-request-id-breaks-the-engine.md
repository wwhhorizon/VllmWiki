# vllm-project/vllm#10583: [Bug]: Duplicate request_id breaks the engine

| 字段 | 值 |
| --- | --- |
| Issue | [#10583](https://github.com/vllm-project/vllm/issues/10583) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Duplicate request_id breaks the engine

### Issue 正文摘录

### Your current environment The environment is not relevant. ### Model Input Dumps _No response_ ### 🐛 Describe the bug The `request_id` field used in the LLM Engine is assumed to be unique, but it is a parameter that can be set by the caller. After https://github.com/vllm-project/vllm/pull/9550, the `request_id` is configurable even by a caller to the OpenAI Server. I originally encountered this issue while investigating the cause of negative metrics in https://github.com/vllm-project/vllm/pull/10430. I found that sending two requests concurrently with the same request id can cause the negative metric error. Example bash using `curl`: ``` curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "meta-llama/Llama-3.2-3B-Instruct", "request_id": "id", "messages": [{"role": "user", "content": "Tell me a long story:"}], "max_tokens": 1024, "min_tokens": 1024, "temperature": 0 }' & sleep 0.5 curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "meta-llama/Llama-3.2-3B-Instruct", "request_id": "id", "messages": [{"role": "user", "content": "Tell me a long story:"}], "max_tokens": 1024, "min_t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: bug ### Your current environment The environment is not relevant. ### Model Input Dumps _No response_ ### 🐛 Describe the bug The `request_id` field used in the LLM Engine is assumed to be unique, but it is a parameter t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 642 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Duplicate request_id breaks the engine bug ### Your current environment The environment is not relevant. ### Model Input Dumps _No response_ ### 🐛 Describe the bug The `request_id` field used in the LLM Engine is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
