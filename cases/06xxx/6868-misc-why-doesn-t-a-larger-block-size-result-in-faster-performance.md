# vllm-project/vllm#6868: [Misc]: Why doesn't a larger block size result in faster performance?

| 字段 | 值 |
| --- | --- |
| Issue | [#6868](https://github.com/vllm-project/vllm/issues/6868) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Why doesn't a larger block size result in faster performance?

### Issue 正文摘录

### Anything you want to discuss about vllm. Hello. Recently, I have been conducting experiments based on several hypotheses, but the results have been different from what I expected, so I am seeking your advice. ### Hypothesis I hypothesized that a larger block size would decrease throughput but improve latency. Conversely, I expected a **smaller block size to increase throughput but worsen latency**. The reasoning behind this is as follows: 1. **For Larger Block Size:** - **Throughput:** Decreases - **Latency:** Improves - **Reason:** With a larger block size, memory fragmentation increases, leading to inefficient use of memory space. However, the number of blocks to manage decreases, thereby reducing the overhead from block table management. 2. **For Smaller Block Size:** - **Throughput:** Increases - **Latency:** Worsens - **Reason:** With a smaller block size, memory fragmentation decreases, making memory use more efficient. However, the number of blocks to manage increases, thereby increasing the overhead from block table management. ### Experimental Setup - **Model:** Llama-2-7b-hf, utilizing 12.5523 GB of memory. - **GPU Memory Utilization:** Set to gpu_memory_utilization=...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ng the overhead from block table management. ### Experimental Setup - **Model:** Llama-2-7b-hf, utilizing 12.5523 GB of memory. - **GPU Memory Utilization:** Set to gpu_memory_utilization=0.9 (default value). - **Other...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Misc]: Why doesn't a larger block size result in faster performance? stale ### Anything you want to discuss about vllm. Hello. Recently, I have been conducting experiments based on several hypotheses, but the results h...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: number of blocks to manage decreases, thereby reducing the overhead from block table management. 2. **For Smaller Block Size:** - **Throughput:** Increases - **Latency:** Worsens - **Reason:** With a smaller block size,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ### Hypothesis I hypothesized that a larger block size would decrease throughput but improve latency. Conversely, I expected a **smaller block size to increase throughput but worsen latency**. The reasoning behind this...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: th a larger block size, memory fragmentation increases, leading to inefficient use of memory space. However, the number of blocks to manage decreases, thereby reducing the overhead from block table management. 2. **For...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
