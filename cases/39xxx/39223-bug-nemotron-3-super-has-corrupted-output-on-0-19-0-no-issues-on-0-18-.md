# vllm-project/vllm#39223: [Bug]: Nemotron 3 super has corrupted output on 0.19.0, no issues on 0.18.1

| 字段 | 值 |
| --- | --- |
| Issue | [#39223](https://github.com/vllm-project/vllm/issues/39223) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Nemotron 3 super has corrupted output on 0.19.0, no issues on 0.18.1

### Issue 正文摘录

### Your current environment Chatting with nemotron 3 super at all in any way on 0.19.0 results in corrupted/garbled output such as infinite loops and endless system prompt repetition. This is with the NVFP4 quant on 2 H100s (so emulated via MARLIN). Completely fine on 0.18.1. Settings: ### 🐛 Describe the bug No crashes directly but infinite loops and failures with structured output that we weren't receiving on 0.18.1. Example of one of the infinitely repeating requests: (APIServer pid=1) INFO 04-07 19:58:51 [loggers.py:259] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 133.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 37.7% (APIServer pid=1) INFO: 10.39.171.227:42706 - "POST /v1/chat/completions HTTP/1.1" 200 OK (APIServer pid=1) INFO 04-07 19:59:01 [loggers.py:259] Engine 000: Avg prompt throughput: 201.5 tokens/s, Avg generation throughput: 60.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 34.5% (APIServer pid=1) INFO: 10.39.171.227:44524 - "POST /v1/chat/completions HTTP/1.1" 200 OK (APIServer pid=1) INFO 04-07 19:59:11 [loggers.py:259] Engine 000: Avg...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: as infinite loops and endless system prompt repetition. This is with the NVFP4 quant on 2 H100s (so emulated via MARLIN). Completely fine on 0.18.1. Settings: ### 🐛 Describe the bug No crashes directly but infinite loop...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: and endless system prompt repetition. This is with the NVFP4 quant on 2 H100s (so emulated via MARLIN). Completely fine on 0.18.1. Settings: ### 🐛 Describe the bug No crashes directly but infinite loops and failures wit...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ration throughput: 133.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 37.7% (APIServer pid=1) INFO: 10.39.171.227:42706 - "POST /v1/chat/completions HTTP/1.1" 200 OK (APIS...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: weren't receiving on 0.18.1. Example of one of the infinitely repeating requests: (APIServer pid=1) INFO 04-07 19:58:51 [loggers.py:259] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 133.0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: erver pid=1) INFO 04-07 19:58:51 [loggers.py:259] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 133.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
