# vllm-project/vllm#13340: [Bug]: vllm server bad

| 字段 | 值 |
| --- | --- |
| Issue | [#13340](https://github.com/vllm-project/vllm/issues/13340) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm server bad

### Issue 正文摘录

### Your current environment vllm 0.7.2 torch 2.4 cuda 12.1 ### 🐛 Describe the bug OpenAI-Compatible Server in chat window call by url base_url="http://localhost:8000/v1" when call api，why 200 OK only the first time and then always 400 Bad Request： log 阿斯follows： INFO: 127.0.0.1:59042 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 02-15 22:09:59 engine.py:275] Added request chatcmpl-803293759b1e415caefd7845b3fa8352. INFO 02-15 22:10:03 metrics.py:455] Avg prompt throughput: 33.4 tokens/s, Avg generation throughput: 37.8 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0%. INFO 02-15 22:10:08 metrics.py:455] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 43.2 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0%. INFO: 127.0.0.1:59042 - "POST /v1/chat/completions HTTP/1.1" 400 Bad Request ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questi...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: server bad bug;stale ### Your current environment vllm 0.7.2 torch 2.4 cuda 12.1 ### 🐛 Describe the bug OpenAI-Compatible Server in chat window call by url base_url="http://localhost:8000/v1" when call api，why 200 OK on...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm server bad bug;stale ### Your current environment vllm 0.7.2 torch 2.4 cuda 12.1 ### 🐛 Describe the bug OpenAI-Compatible Server in chat window call by url base_url="http://localhost:8000/v1" when call api，w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 9b1e415caefd7845b3fa8352. INFO 02-15 22:10:03 metrics.py:455] Avg prompt throughput: 33.4 tokens/s, Avg generation throughput: 37.8 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ons. performance attention_kv_cache;frontend_api cache;cuda slowdown env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t: 37.8 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0%. INFO 02-15 22:10:08 metrics.py:455] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
