# vllm-project/vllm#18009: [RFC]: Model Parallelism with Single Worker using SPMD

| 字段 | 值 |
| --- | --- |
| Issue | [#18009](https://github.com/vllm-project/vllm/issues/18009) |
| 状态 | closed |
| 标签 | RFC;unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Model Parallelism with Single Worker using SPMD

### Issue 正文摘录

### Motivation. ## Goal Propose to add an alternative to enable model parallelism with a single worker, partition model with GSPMD. ## Motivation ![Image](https://github.com/user-attachments/assets/872501e3-a1bf-45d2-a229-e401236e127b) _Figure 1: (Left) Current vLLM multi-chip architecture (Right) Proposed single worker architecture_ The current vLLM utilizes multiple workers when a model is partitioned across several devices (**One device per worker**). In this setup, communication operations, such as reducing partial sums or gathering sharded data, are explicitly called within the model's implementation. In contrast, the PyTorch on TPU stack (PyTorch/XLA and the XLA Compiler) offers an alternative parallelism programming model: Programmer implements models **as if it runs on a single device (No explicit communication op)**, and **provides hints to compiler** on how to partition the model. The compiler then automatically inserts the necessary collective communication operations and applies optimization passes to overlap communication and computation. Therefore, the model code is expected to have **global shape** even if the model is partitioned. The TPU compiler stack is heavily...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: vice per worker**). In this setup, communication operations, such as reducing partial sums or gathering sharded data, are explicitly called within the model's implementation. In contrast, the PyTorch on TPU stack (PyTor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC]: Model Parallelism with Single Worker using SPMD RFC;unstale ### Motivation. ## Goal Propose to add an alternative to enable model parallelism with a single worker, partition model with GSPMD. ## Motivation ![Imag...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [RFC]: Model Parallelism with Single Worker using SPMD RFC;unstale ### Motivation. ## Goal Propose to add an alternative to enable model parallelism with a single worker, partition model with GSPMD. ## Motivation ![Imag...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: U during partitioning Initializing the full model on CPU may cause host OOM if the model is very large (e.g. DeepSeek v3 - more than 1.2 TB). To make the model initialization and weight loading more efficient and cleane...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Model Parallelism with Single Worker using SPMD RFC;unstale ### Motivation. ## Goal Propose to add an alternative to enable model parallelism with a single worker, partition model with GSPMD. ## Motivation ![Imag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
