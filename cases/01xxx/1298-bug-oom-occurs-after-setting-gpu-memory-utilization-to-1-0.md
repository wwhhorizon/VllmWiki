# vllm-project/vllm#1298: [Bug]OOM occurs after setting gpu_memory_utilization to 1.0

| 字段 | 值 |
| --- | --- |
| Issue | [#1298](https://github.com/vllm-project/vllm/issues/1298) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]OOM occurs after setting gpu_memory_utilization to 1.0

### Issue 正文摘录

When I execute the following command, it runs llama2 70b ```shell python3 benchmark_latency.py --model llama2_70b --input-len 1536 --output-len 512 --batch-size 11 -tp 2 ``` The default gpu_memory_utilization is 0.90, and the above command can run normally. But if I set the gpu_memory_utilization default value to 1.0 and run the same command, OOM occurs ![image](https://github.com/vllm-project/vllm/assets/19977378/18447fec-0358-4d84-bd44-4747fc526bc2) Is this reasonable? What is the maximum value that gpu_memory_utilization can be set to? Thanks~

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _memory_utilization to 1.0 When I execute the following command, it runs llama2 70b ```shell python3 benchmark_latency.py --model llama2_70b --input-len 1536 --output-len 512 --batch-size 11 -tp 2 ``` The default gpu_me...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: en I execute the following command, it runs llama2 70b ```shell python3 benchmark_latency.py --model llama2_70b --input-len 1536 --output-len 512 --batch-size 11 -tp 2 ``` The default gpu_memory_utilization is 0.90, and...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]OOM occurs after setting gpu_memory_utilization to 1.0 When I execute the following command, it runs llama2 70b ```shell python3 benchmark_latency.py --model llama2_70b --input-len 1536 --output-len 512 --batch-siz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
