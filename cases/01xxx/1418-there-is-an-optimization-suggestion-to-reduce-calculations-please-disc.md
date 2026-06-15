# vllm-project/vllm#1418: There is an optimization suggestion to reduce calculations. Please discuss whether it is feasible.

| 字段 | 值 |
| --- | --- |
| Issue | [#1418](https://github.com/vllm-project/vllm/issues/1418) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> There is an optimization suggestion to reduce calculations. Please discuss whether it is feasible.

### Issue 正文摘录

I have a suggestion here. In the prompt stage, if the last layer of decoders does not use 'multi_query_kv_attention', but uses the hidden state corresponding to the last token in the prompt as query[1] to calculate 'single_query_cached_kv_attention', then before sampling, There is no need to go through the '_prune_hidden_states' function [2]. This can not only reduce the amount of calculation, but also reduce unnecessary function calls. Reference: [1] https://github.com/vllm-project/vllm/blob/f8a1e39fae05ca610be8d5a78be9d40f5274e5fc/vllm/model_executor/models/opt.py#L244 [2] https://github.com/vllm-project/vllm/blob/665c48963be11b2e5cb7209cd25f884129e5c284/vllm/model_executor/layers/sampler.py#L41

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/f8a1e39fae05ca610be8d5a78be9d40f5274e5fc/vllm/model_executor/models/opt.py#L244 [2] https://github.com/vllm-project/vllm/blob/665c48963be11b2e5cb7209cd25f884129e5c284/vllm/model_executor/layer...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ble. I have a suggestion here. In the prompt stage, if the last layer of decoders does not use 'multi_query_kv_attention', but uses the hidden state corresponding to the last token in the prompt as query[1] to calculate...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
