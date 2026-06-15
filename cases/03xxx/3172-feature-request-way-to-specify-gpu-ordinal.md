# vllm-project/vllm#3172: [Feature Request] Way to specify GPU ordinal

| 字段 | 值 |
| --- | --- |
| Issue | [#3172](https://github.com/vllm-project/vllm/issues/3172) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature Request] Way to specify GPU ordinal

### Issue 正文摘录

Hello. I am currently employing the vllm library alongside dataparallel for my projects. Up until version 0.2.6, it was feasible to designate specific GPUs for each worker explicitly, which was instrumental for optimizing resource allocation, particularly when not using tensor parallelism. The code snippet below illustrates how this configuration was implemented: ```python def child_process(rank): os.environ["LOCAL_RANK"] = str(rank) from vllm import LLM ``` This functionality seems to be unsupported in versions of vllm later than 0.2.6. This feature is crucial for achieving higher throughput, especially when working with smaller models on high-VRAM GPUs (e.g., a 2B parameter model on an A100 80G GPU). Thank you!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature Request] Way to specify GPU ordinal stale Hello. I am currently employing the vllm library alongside dataparallel for my projects. Up until version 0.2.6, it was feasible to designate specific GPUs for each wor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: imizing resource allocation, particularly when not using tensor parallelism. The code snippet below illustrates how this configuration was implemented: ```python def child_process(rank): os.environ["LOCAL_RANK"] = str(r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t using tensor parallelism. The code snippet below illustrates how this configuration was implemented: ```python def child_process(rank): os.environ["LOCAL_RANK"] = str(rank) from vllm import LLM ``` This functionality...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature Request] Way to specify GPU ordinal stale Hello. I am currently employing the vllm library alongside dataparallel for my projects. Up until version 0.2.6, it was feasible to designate specific GPUs for each wor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: of vllm later than 0.2.6. This feature is crucial for achieving higher throughput, especially when working with smaller models on high-VRAM GPUs (e.g., a 2B parameter model on an A100 80G GPU). Thank you!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
