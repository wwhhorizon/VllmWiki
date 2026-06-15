# vllm-project/vllm#22501: [Usage]: Running a 300-400B Parameter Model on Multi-Node Setup (2x 8xA100)

| 字段 | 值 |
| --- | --- |
| Issue | [#22501](https://github.com/vllm-project/vllm/issues/22501) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Running a 300-400B Parameter Model on Multi-Node Setup (2x 8xA100)

### Issue 正文摘录

When multiple nodes are required, how can you run a model using LLM instances? For example, running a model with 300-400 billion parameters on two 8xA100 machines.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage]: Running a 300-400B Parameter Model on Multi-Node Setup (2x 8xA100) usage;stale When multiple nodes are required, how can you run a model using LLM instances? For example, running a model with 300-400 billion pa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Running a 300-400B Parameter Model on Multi-Node Setup (2x 8xA100) usage;stale When multiple nodes are required, how can you run a model using LLM instances? For example, running a model with 300-400 billion pa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Running a 300-400B Parameter Model on Multi-Node Setup (2x 8xA100) usage;stale When multiple nodes are required, how can you run a model using LLM instances? For example, running a model with 300-400 billion parameters...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
