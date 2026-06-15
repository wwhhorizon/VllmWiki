# vllm-project/vllm#16771: [Usage]: How to configure the server parameters for THUDM/GLM-4-32B-0414 to support Function call using vllm-0.8.4?

| 字段 | 值 |
| --- | --- |
| Issue | [#16771](https://github.com/vllm-project/vllm/issues/16771) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to configure the server parameters for THUDM/GLM-4-32B-0414 to support Function call using vllm-0.8.4?

### Issue 正文摘录

### Your current environment ```text I launch a server with : `python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8080 --model THUDM/GLM-4-32B-0414 --served-model-name glm-4-32b-0414 --enable-auto-tool-choice --tool-call-parser pythonic` But the tool_calls is empty in the response, `{"id":"chatcmpl-aeb3eb3ab7ab4aa59c5ab8658c68560d","object":"chat.completion","created":1744881899,"model":"glm-z1-9b-0414", "choices":[{"index":0,"message":{"role":"assistant","reasoning_content":null,"content":"Okay, the user is asking about the temperature","tool_calls":[]},"logprobs":null,"finish_reason":"stop","stop_reason":151338}],"usage":{"prompt_tokens":180,"total_tokens":403,"completion_tokens":223,"prompt_tokens_details":null},"prompt_logprobs":null}` ``` ### How would you like to use vllm I want to run inference of a [THUDM/GLM-4-32B-0414](https://huggingface.co/THUDM/GLM-4-32B-0414), and it need to support Function Call, I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/),...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: How to configure the server parameters for THUDM/GLM-4-32B-0414 to support Function call using vllm-0.8.4? usage;stale ### Your current environment ```text I launch a server with : `python3 -m vllm.entrypoints....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: or THUDM/GLM-4-32B-0414 to support Function call using vllm-0.8.4? usage;stale ### Your current environment ```text I launch a server with : `python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8080 --mo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
