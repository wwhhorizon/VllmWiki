# vllm-project/vllm#23113: [RFC]: Enabling Multiple Graphs Based on pre-defined conditions

| 字段 | 值 |
| --- | --- |
| Issue | [#23113](https://github.com/vllm-project/vllm/issues/23113) |
| 状态 | closed |
| 标签 | RFC;torch.compile |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Enabling Multiple Graphs Based on pre-defined conditions

### Issue 正文摘录

### Motivation. ### **Goal**: Extend `CUDAPiecewiseBackend` to dynamically select and execute different compiled graphs based on runtime conditions, moving beyond its current reliance on pre-defined compile sizes. This includes the ability to apply specific fusion passes conditionally within the backend. ### Motivation: Currently, CUDAPiecewiseBackend compiles separate graphs for different pre-defined "compile sizes." Any graph modifications that are shape specific require compiling for every shape separately. For example, if we want to apply different optimizations for `num_tokens = 256`, we’d have to manually compile all sizes under 256.This changes are specifically needed for performance of allreduce fusion. We need to have separate graphs: 1. where we use FlashInfer fused `allreduce+RMSNorm + Quant`(for certain range of input sizes) and 2. the default graph with non-fused allreduce. If we condition on the size in the same graph, we have worse than default performance for non-fused path.These changes are essential for optimizing all-reduce fusion performance. We require two distinct graphs: 1. one employing FlashInfer's fused all-reduce + RMSNorm + Quant (for specific input siz...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ed conditions RFC;torch.compile ### Motivation. ### **Goal**: Extend `CUDAPiecewiseBackend` to dynamically select and execute different compiled graphs based on runtime conditions, moving beyond its current reliance on...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: to: Compile distinct graphs for different conditional branches within a model's execution. Enable the application of specific passes only when certain runtime conditions are met. This enhancement would enable more perfo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: RFC;torch.compile ### Motivation. ### **Goal**: Extend `CUDAPiecewiseBackend` to dynamically select and execute different compiled graphs based on runtime conditions, moving beyond its current reliance on pre-defined co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: RFC]: Enabling Multiple Graphs Based on pre-defined conditions RFC;torch.compile ### Motivation. ### **Goal**: Extend `CUDAPiecewiseBackend` to dynamically select and execute different compiled graphs based on runtime c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: iseBackend`, we will implement the following: - **Condition Checking**: Evaluate the predefined runtime conditions (e.g., input tensor shapes, specific model parameters). For shape conditions, **New Graph Creation**: If...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
