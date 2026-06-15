# vllm-project/vllm#29603: [Bug]: vllm gets internal server error when set tool_choice='required' for kimi-k2-thinking

| 字段 | 值 |
| --- | --- |
| Issue | [#29603](https://github.com/vllm-project/vllm/issues/29603) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm gets internal server error when set tool_choice='required' for kimi-k2-thinking

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug in latest release or maybe also in previous few versions, using kimi-k2-think with tool_choice='required' gets internal server error without any log. serve log: ``` (APIServer pid=9050) INFO: 172.24.240.206:6122 - "GET /v1/models HTTP/1.1" 200 OK (APIServer pid=9050) INFO: 10.65.84.211:55174 - "POST /v1/chat/completions HTTP/1.1" 200 OK (APIServer pid=9050) INFO: 10.65.86.10:43264 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error (APIServer pid=9050) INFO: 10.65.86.9:55074 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error (APIServer pid=9050) INFO: 172.24.52.126:45902 - "GET /v1/models HTTP/1.1" 200 OK (APIServer pid=9050) INFO 11-26 22:03:50 [loggers.py:236] Engine 000: Avg prompt throughput: 76.4 tokens/s, Avg generation throughput: 8.6 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 63.0% (APIServer pid=9050) INFO: 10.65.86.8:59288 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error (APIServer pid=9050) INFO: 10.66.21.205:42584 - "GET /metrics HTTP/1.1" 200 OK (APIServer pid=9050) INFO: 10.99.112.21:49266 - "GET /metrics HTTP/1.1" 200 OK ``...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: neration throughput: 8.6 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 63.0% (APIServer pid=9050) INFO: 10.65.86.8:59288 - "POST /v1/chat/completions HTTP/1.1" 500 Internal...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: al server error when set tool_choice='required' for kimi-k2-thinking bug;stale ### Your current environment ### 🐛 Describe the bug in latest release or maybe also in previous few versions, using kimi-k2-think with tool_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: bug;stale ### Your current environment ### 🐛 Describe the bug in latest release or maybe also in previous few versions, using kimi-k2-think with tool_choice='required' gets internal server error without any log. serve l...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ns/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 63.0% (APIServer pid=9050) INFO: 10.65.86.8:59288 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error (APIServer pid=...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### 🐛 Describe the bug in latest release or maybe also in previous few versions, using kimi-k2-think with tool_choice='required' gets internal server error without any log. serve log: ``` (APIServer pid=9050) INFO: 172....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
