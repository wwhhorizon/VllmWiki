# vllm-project/vllm#36623: [Bug]: OOM when --kv-offloading-size>1024

| 字段 | 值 |
| --- | --- |
| Issue | [#36623](https://github.com/vllm-project/vllm/issues/36623) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: OOM when --kv-offloading-size>1024

### Issue 正文摘录

### Your current environment - vLLM: 0.15.0 - TP: 8 - Memory Limit of Pod: 1872 GB - GPU: 8 x H200 ### 🐛 Describe the bug We are testing the KV Offloading to CPU using vLLM native backend, we found that when kv_offloading_size > 1024GB (here 1025 is used), it will result in memory leak and causing OOM finally. From the memory profile, the memory keeps growing until OOM. [vllm.log](https://github.com/user-attachments/files/25865157/vllm.log) [memory_profile_tp8-oom.csv](https://github.com/user-attachments/files/25865190/memory_profile_tp8-oom.csv) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: OOM when --kv-offloading-size>1024 bug ### Your current environment - vLLM: 0.15.0 - TP: 8 - Memory Limit of Pod: 1872 GB - GPU: 8 x H200 ### 🐛 Describe the bug We are testing the KV Offloading to CPU using vLLM...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: y Limit of Pod: 1872 GB - GPU: 8 x H200 ### 🐛 Describe the bug We are testing the KV Offloading to CPU using vLLM native backend, we found that when kv_offloading_size > 1024GB (here 1025 is used), it will result in mem...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: cribe the bug We are testing the KV Offloading to CPU using vLLM native backend, we found that when kv_offloading_size > 1024GB (here 1025 is used), it will result in memory leak and causing OOM finally. From the memory...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: sv) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
