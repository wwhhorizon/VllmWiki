# vllm-project/vllm#5948: [Usage]: 是否可以多节点多CPU推理

| 字段 | 值 |
| --- | --- |
| Issue | [#5948](https://github.com/vllm-project/vllm/issues/5948) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: 是否可以多节点多CPU推理

### Issue 正文摘录

### Your current environment ``` python=3.10.14 vllm=0.5.0.post1+cpu ray=2.24.0 torch=2.3.1+cpu.cxx11.abi ``` ``` Node status --------------------------------------------------------------- Active: 1 node_a6934217c9f0e60dd1fc630f8dade979cfaec08bbb1d57a252eeaa6f 1 node_29060e43a28cfe9219885582151476537fbad92e78c1f5169fa132ad Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/52.0 CPU 0.0/2.0 GPU 0B/9.32GiB memory 0B/4.29GiB object_store_memory ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: 是否可以多节点多CPU推理 usage;stale ### Your current environment ``` python=3.10.14 vllm=0.5.0.post1+cpu ray=2.24.0 torch=2.3.1+cpu.cxx11.abi ``` ``` Node status ----------------------------------------------------------...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
