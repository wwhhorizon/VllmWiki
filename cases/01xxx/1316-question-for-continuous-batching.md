# vllm-project/vllm#1316: Question for continuous batching

| 字段 | 值 |
| --- | --- |
| Issue | [#1316](https://github.com/vllm-project/vllm/issues/1316) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question for continuous batching

### Issue 正文摘录

Hi vllm team: in the `attention.py` https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/attention.py#L209 looks like you split the prompt phase and generation phase. But in continuous batching, what may happen is There will be a mixture of prompt phase and generation phase. For example, if one of the request in this batch is finished before others, so another new request will be inserted into this batch. In this case, there will be one request in prompt phase and other requests in generation phase. How do you handle this situation? Thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n the `attention.py` https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/attention.py#L209 looks like you split the prompt phase and generation phase. But in continuous batching, what may happen is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ixture of prompt phase and generation phase. For example, if one of the request in this batch is finished before others, so another new request will be inserted into this batch. In this case, there will be one request i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
