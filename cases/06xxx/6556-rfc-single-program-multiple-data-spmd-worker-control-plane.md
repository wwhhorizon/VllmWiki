# vllm-project/vllm#6556: [RFC]: Single Program Multiple Data (SPMD) Worker Control Plane

| 字段 | 值 |
| --- | --- |
| Issue | [#6556](https://github.com/vllm-project/vllm/issues/6556) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Single Program Multiple Data (SPMD) Worker Control Plane

### Issue 正文摘录

### Motivation. **TL;DR**: Introduce SPMD-style control plane to improve control plane architecture and optimize performance. For distributed inference, vLLM currently leverages a “driver-worker”, along with other workers. As shown in the diagram below, this driver-worker is in the same process as the driver. It prepares the arguments, then broadcasts them to all other workers to execute the sharded model, leveraging NCCL as the control plane. This architecture has a few drawbacks. First, the driver-worker needs to participate in the NCCL group and execute the model. Since NCCL broadcast is a synchronous operation, this creates interference with other driver functionality such as scheduling and affects performance. Moreover, this architecture made it difficult to support speculative decoding. Specifically, 1. Speculative decoding framework may not run the draft model if Dynamic Speculative Decoding (DSD) or other policy is enabled. In this case, the decision of whether to run the draft model must be communicated to other ranks. So DSD cannot work with TP>1, unless there is additional communication (which incurs latency overhead). 2. Pipeline parallelism can be composed within the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: architecture has a few drawbacks. First, the driver-worker needs to participate in the NCCL group and execute the model. Since NCCL broadcast is a synchronous operation, this creates interference with other driver funct...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Single Program Multiple Data (SPMD) Worker Control Plane RFC;stale ### Motivation. **TL;DR**: Introduce SPMD-style control plane to improve control plane architecture and optimize performance. For distributed inf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: **TL;DR**: Introduce SPMD-style control plane to improve control plane architecture and optimize performance. For distributed inference, vLLM currently leverages a “driver-worker”, along with other workers. As shown in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: uments, then broadcasts them to all other workers to execute the sharded model, leveraging NCCL as the control plane. This architecture has a few drawbacks. First, the driver-worker needs to participate in the NCCL grou...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: t work with TP>1, unless there is additional communication (which incurs latency overhead). 2. Pipeline parallelism can be composed within the speculative decoding framework. However the speculative tokens must be sent...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
