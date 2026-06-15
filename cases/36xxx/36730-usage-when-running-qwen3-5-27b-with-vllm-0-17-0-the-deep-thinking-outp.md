# vllm-project/vllm#36730: [Usage]: When running qwen3.5-27b with vllm 0.17.0, the Deep Thinking output is under "reasoning" and not under "reasoning_content".

| 字段 | 值 |
| --- | --- |
| Issue | [#36730](https://github.com/vllm-project/vllm/issues/36730) |
| 状态 | open |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: When running qwen3.5-27b with vllm 0.17.0, the Deep Thinking output is under "reasoning" and not under "reasoning_content".

### Issue 正文摘录

### Your current environment ```text vllm /Qwen/Qwen3.5-27B --port 40023 --host 10.0.30.105 --served-model-name local-qwen3.5-27b --tensor-parallel-size 2 --tool-call-parser=qwen3_coder --gpu-memory-utilization=0.8 --enable-auto-tool-choice --max-model-len=262144 --skip-mm-profiling --reasoning-parser=qwen3 ``` ### How would you like to use vllm When I run the request test ``` curl --location 'http://10.0.30.105:40023/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data '{ "model": "local-qwen3.5-27b", "messages": [ { "role": "user", "content": "你好" } ], "stream": true }' ``` then output ``` data: {"id":"chatcmpl-740c22ad-c984-49a4-9a78-b7bbdc69b3d2","object":"chat.completion.chunk","created":1773161262,"model":"local-qwen3.5-27b","choices":[{"index":0,"delta":{"reasoning":"Thinking"},"logprobs":null,"finish_reason":null,"token_ids":null}]} data: {"id":"chatcmpl-740c22ad-c984-49a4-9a78-b7bbdc69b3d2","object":"chat.completion.chunk","created":1773161262,"model":"local-qwen3.5-27b","choices":[{"index":0,"delta":{"reasoning":" Process"},"logprobs":null,"finish_reason":null,"token_ids":null}]} ``` I expect the output to be in the following format. ``` data: {"id":...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: When running qwen3.5-27b with vllm 0.17.0, the Deep Thinking output is under "reasoning" and not under "reasoning_content". usage ### Your current environment ```text vllm /Qwen/Qwen3.5-27B --port 40023 --host...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ilization=0.8 --enable-auto-tool-choice --max-model-len=262144 --skip-mm-profiling --reasoning-parser=qwen3 ``` ### How would you like to use vllm When I run the request test ``` curl --location 'http://10.0.30.105:4002...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: up? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ing-parser=qwen3 ``` ### How would you like to use vllm When I run the request test ``` curl --location 'http://10.0.30.105:40023/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data '{ "model": "lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
