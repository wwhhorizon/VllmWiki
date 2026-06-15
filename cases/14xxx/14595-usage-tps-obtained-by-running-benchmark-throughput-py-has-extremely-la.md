# vllm-project/vllm#14595: [Usage]: tps obtained by running benchmark_throughput.py has extremely large differences

| 字段 | 值 |
| --- | --- |
| Issue | [#14595](https://github.com/vllm-project/vllm/issues/14595) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: tps obtained by running benchmark_throughput.py has extremely large differences

### Issue 正文摘录

I use benchmark_throughput.py to calculate the TPS for Qwen7B on a single A100 GPU. However, it's quite strange that the TPS values obtained by running benchmark_throughput.py vary significantly each time, ranging from 71 TPS to 104 TPS. Moreover, I use the export CUDA_VISIBLE_DEVICES command to specify a particular GPU for use.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: use benchmark_throughput.py to calculate the TPS for Qwen7B on a single A100 GPU. However, it's quite strange that the TPS values obtained by running benchmark_throughput.py vary significantly each time, ranging from 71...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: tps obtained by running benchmark_throughput.py has extremely large differences usage;stale I use benchmark_throughput.py to calculate the TPS for Qwen7B on a single A100 GPU. However, it's quite strange that t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: o 104 TPS. Moreover, I use the export CUDA_VISIBLE_DEVICES command to specify a particular GPU for use.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ences usage;stale I use benchmark_throughput.py to calculate the TPS for Qwen7B on a single A100 GPU. However, it's quite strange that the TPS values obtained by running benchmark_throughput.py vary significantly each t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: by running benchmark_throughput.py has extremely large differences usage;stale I use benchmark_throughput.py to calculate the TPS for Qwen7B on a single A100 GPU. However, it's quite strange that the TPS values obtained...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
