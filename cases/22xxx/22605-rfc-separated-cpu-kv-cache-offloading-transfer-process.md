# vllm-project/vllm#22605: [RFC]: Separated CPU KV Cache Offloading/Transfer Process

| 字段 | 值 |
| --- | --- |
| Issue | [#22605](https://github.com/vllm-project/vllm/issues/22605) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 36; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Separated CPU KV Cache Offloading/Transfer Process

### Issue 正文摘录

### Motivation. CPU KV cache offloading and CPU-based KV cache transmission are always very important to vLLM. There are already some existing solutions, such as [KV-connector-based offloading](https://github.com/vllm-project/vllm/blob/main/vllm/distributed/kv_transfer/kv_connector/v1/lmcache_connector.py), [KV-connector-based KV transmissions](https://github.com/vllm-project/vllm/blob/main/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py). Quite a few RFCs are also proposing new solutions for CPU KV cache offloading (#16144, #19854). However, the current implementations and proposals have several inefficiencies and complexity issues: 1. CPU overhead in workers – memcpy kernel launches and other CPU KV tasks run in worker processes, impacting inference performance. 2. Extra cross-worker IPC – CPU KV metadata gathering requires additional IPC, adding latency and complexity. 3. Coupling with inference loop – Transmission logic is only triggered when a worker is invoked, adding unnecessary latency. 4. Fragmented code paths – CPU offloading, eviction, and CPU-based prefill/disaggregated paths are handled separately, resulting in duplicated h2d/d2h calls. 5. Scheduler com...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: KV cache offloading and CPU-based KV cache transmission are always very important to vLLM. There are already some existing solutions, such as [KV-connector-based offloading](https://github.com/vllm-project/vllm/blob/mai...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: Separated CPU KV Cache Offloading/Transfer Process RFC;stale ### Motivation. CPU KV cache offloading and CPU-based KV cache transmission are always very important to vLLM. There are already some existing solution...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: s-worker IPC – CPU KV metadata gathering requires additional IPC, adding latency and complexity. 3. Coupling with inference loop – Transmission logic is only triggered when a worker is invoked, adding unnecessary latenc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tale ### Motivation. CPU KV cache offloading and CPU-based KV cache transmission are always very important to vLLM. There are already some existing solutions, such as [KV-connector-based offloading](https://github.com/v...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [RFC]: Separated CPU KV Cache Offloading/Transfer Process RFC;stale ### Motivation. CPU KV cache offloading and CPU-based KV cache transmission are always very important to vLLM. There are already some existing solution...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
