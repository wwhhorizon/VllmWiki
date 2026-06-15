# vllm-project/vllm#9118: [Bug]: Issue Running VLLM Open AI using nonroot user in K8s

| 字段 | 值 |
| --- | --- |
| Issue | [#9118](https://github.com/vllm-project/vllm/issues/9118) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Issue Running VLLM Open AI using nonroot user in K8s

### Issue 正文摘录

### Your current environment We run it on k8s. ### Model Input Dumps _No response_ ### 🐛 Describe the bug We are running vllm-openai:latest on two different clusters: the first cluster using the root user, and the second using a non-root user. Both services are running and accessible via /v1/models, but when we try to hit /v1/chat/completions on the non-root cluster, it keeps returning a 500 error, as shown in the logs below, without any detailed error message (it's working fine in the other cluster). ``` GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. DEBUG 10-07 01:48:03 engine.py:212] Waiting for new requests in engine loop. DEBUG 10-07 01:48:03 client.py:164] Waiting for output from MQLLMEngine. DEBUG 10-07 01:48:03 client.py:148] Heartbeat successful. DEBUG 10-07 01:48:05 client.py:148] Heartbeat successful. DEBUG 10-07 01:48:07 client.py:148] Heartbeat successful. DEBUG 10-07 01:48:09 client.py:148] Heartbeat successful. DEBUG 10-07 01:48:11 client.py:148] Heartbeat successful. INFO: 192.168.10.69:34084 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error INFO 10-07 01:48:13 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: oot user in K8s bug ### Your current environment We run it on k8s. ### Model Input Dumps _No response_ ### 🐛 Describe the bug We are running vllm-openai:latest on two different clusters: the first cluster using the root...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: age: 0.0%, CPU KV cache usage: 0.0%. DEBUG 10-07 01:48:03 engine.py:212] Waiting for new requests in engine loop. DEBUG 10-07 01:48:03 client.py:164] Waiting for output from MQLLMEngine. DEBUG 10-07 01:48:03 client.py:1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: mps _No response_ ### 🐛 Describe the bug We are running vllm-openai:latest on two different clusters: the first cluster using the root user, and the second using a non-root user. Both services are running and accessible...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: riables, but we are still not getting much information. is there any specific configuration that we miss? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ss? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
