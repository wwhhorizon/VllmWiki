# vllm-project/vllm#6155: [Usage]: How to use Multi-instance in Vllm? (Model replication on multiple GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#6155](https://github.com/vllm-project/vllm/issues/6155) |
| 状态 | closed |
| 标签 | usage;unstale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use Multi-instance in Vllm? (Model replication on multiple GPUs)

### Issue 正文摘录

I would like to use techniques such as Multi-instance Support supported by the tensorrt-llm backend. In the documentation, I can see that multiple models are served using modes like Leader mode and Orchestrator mode. Does vLLM support this functionality separately? Or should I implement it similarly to the tensorrt-llm backend? Here is for reference url : https://github.com/triton-inference-server/tensorrtllm_backend?tab=readme-ov-file#leader-mode

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: techniques such as Multi-instance Support supported by the tensorrt-llm backend. In the documentation, I can see that multiple models are served using modes like Leader mode and Orchestrator mode. Does vLLM support this...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: How to use Multi-instance in Vllm? (Model replication on multiple GPUs) usage;unstale I would like to use techniques such as Multi-instance Support supported by the tensorrt-llm backend. In the documentation, I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: use Multi-instance in Vllm? (Model replication on multiple GPUs) usage;unstale I would like to use techniques such as Multi-instance Support supported by the tensorrt-llm backend. In the documentation, I can see that mu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
