# vllm-project/vllm#208: Remove Ray for the dependency

| 字段 | 值 |
| --- | --- |
| Issue | [#208](https://github.com/vllm-project/vllm/issues/208) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Remove Ray for the dependency

### Issue 正文摘录

Using Ray in here is considering to be an overkill. You can create a multi-process distributed environment easily using torchdist or mpi launch. Internally you can leverage NCCL or MPI communication protocol for inter-process communications.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Remove Ray for the dependency feature request Using Ray in here is considering to be an overkill. You can create a multi-process distributed environment easily using torchdist or mpi launch. Internally you can leverage...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Remove Ray for the dependency feature request Using Ray in here is considering to be an overkill. You can create a multi-process distributed environment easily using torchdist or mpi launch. Internally you can leverage...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
