# vllm-project/vllm#1995: How can I deploy vllm model with multi-replicas

| 字段 | 值 |
| --- | --- |
| Issue | [#1995](https://github.com/vllm-project/vllm/issues/1995) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How can I deploy vllm model with multi-replicas

### Issue 正文摘录

I want to deploy a LLM model on 8 A100 gpus. To support the higher concurrency, I want to deploy 8 replicas (one replica on one gpu), and I want to expose one service to handle user requests, how can I do it?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: deploy vllm model with multi-replicas I want to deploy a LLM model on 8 A100 gpus. To support the higher concurrency, I want to deploy 8 replicas (one replica on one gpu), and I want to expose one service to handle user...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: How can I deploy vllm model with multi-replicas I want to deploy a LLM model on 8 A100 gpus. To support the higher concurrency, I want to deploy 8 replicas (one replica on one gpu), and I want to expose one service to h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: one replica on one gpu), and I want to expose one service to handle user requests, how can I do it?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
