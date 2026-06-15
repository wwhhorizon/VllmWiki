# vllm-project/vllm#841: Support for RLHF (ILQL)-trained Models

| 字段 | 值 |
| --- | --- |
| Issue | [#841](https://github.com/vllm-project/vllm/issues/841) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support for RLHF (ILQL)-trained Models

### Issue 正文摘录

LMs trained with [ILQL](https://github.com/CarperAI/trlx/blob/main/trlx/models/modeling_ilql.py) are not supported by vLLM at the moment. Is this in the roadmap? It looks like it shouldn't be tough to do it.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Support for RLHF (ILQL)-trained Models feature request LMs trained with [ILQL](https://github.com/CarperAI/trlx/blob/main/trlx/models/modeling_ilql.py) are not supported by vLLM at the moment. Is this in the roadmap? It...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Support for RLHF (ILQL)-trained Models feature request LMs trained with [ILQL](https://github.com/CarperAI/trlx/blob/main/trlx/models/modeling_ilql.py) are not supported by vLLM at the moment. Is this in the roadmap? It...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
