# vllm-project/vllm#3885: Sample configurations to maximize throughput on typical GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#3885](https://github.com/vllm-project/vllm/issues/3885) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Sample configurations to maximize throughput on typical GPUs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am running the `benchmark_throughput` on A100 with the dataset mentioned in readme. However, from `nvtop`, the GPU utilization is only 20% even if I've set `max_num_batched_tokens=10240, max_num_seqs=1024`. Could you provide some sample configurations for typical GPUs like A100, V100 that can maximize the throughput performance? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Sample configurations to maximize throughput on typical GPUs feature request;stale ### 🚀 The feature, motivation and pitch I am running the `benchmark_throughput` on A100 with the dataset mentioned in readme. However, f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Sample configurations to maximize throughput on typical GPUs feature request;stale ### 🚀 The feature, motivation and pitch I am running the `benchmark_throughput` on A100 with the dataset mentioned in readme. However, f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: eature, motivation and pitch I am running the `benchmark_throughput` on A100 with the dataset mentioned in readme. However, from `nvtop`, the GPU utilization is only 20% even if I've set `max_num_batched_tokens=10240, m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Sample configurations to maximize throughput on typical GPUs feature request;stale ### 🚀 The feature, motivation and pitch I am running the `benchmark_throughput` on A100 with the dataset mentioned in readme. However, f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
