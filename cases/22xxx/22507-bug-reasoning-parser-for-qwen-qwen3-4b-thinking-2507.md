# vllm-project/vllm#22507: [Bug]: reasoning parser for Qwen/Qwen3-4B-Thinking-2507

| 字段 | 值 |
| --- | --- |
| Issue | [#22507](https://github.com/vllm-project/vllm/issues/22507) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: reasoning parser for Qwen/Qwen3-4B-Thinking-2507

### Issue 正文摘录

### Your current environment vllm/vllm-openai:v0.10.0 ``` args: - "--model" - "Qwen/Qwen3-4B-Thinking-2507" - "--gpu-memory-utilization" - "0.95" - "--revision" - "main" - "--tensor-parallel-size" - "1" - --disable-log-requests - "--tool-call-parser" - "hermes" - "--reasoning-parser" - "qwen3" - "--enable-prompt-tokens-details" ``` ### 🐛 Describe the bug [Qwen/Qwen3-4B-Thinking-2507 doesn't output \ ](https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507#model-overview) and then reasoning parser doesn't work ``` curl -sv http://10.150.255.192:30095/v1/chat/completions \ -X POST \ -H 'Content-Type: application/json' \ -d \ '{ "model": "Qwen/Qwen3-4B-Thinking-2507", "messages": [ { "role": "user", "content": "Hello!" } ] }' * Trying 10.150.255.192:30095... * Connected to 10.150.255.192 (10.150.255.192) port 30095 (#0) > POST /v1/chat/completions HTTP/1.1 > Host: 10.150.255.192:30095 > User-Agent: curl/7.76.1 > Accept: */* > Content-Type: application/json > Content-Length: 125 > * Mark bundle as not supporting multiuse \n\nHello! 😊 How can I assist you today?","refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning_content":null},"logprobs":null,"f...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: reasoning parser for Qwen/Qwen3-4B-Thinking-2507 bug ### Your current environment vllm/vllm-openai:v0.10.0 ``` args: - "--model" - "Qwen/Qwen3-4B-Thinking-2507" - "--gpu-memory-utilization" -
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: - "--tensor-parallel-size" - "1" - --disable-log-requests - "--tool-call-parser" - "hermes" - "--reasoning-parser" - "qwen3" - "--enable-prompt-tokens-details" ``` ### 🐛 Describe the bug [Qwen/Qwen3-4B-Thinking-2507 d
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
