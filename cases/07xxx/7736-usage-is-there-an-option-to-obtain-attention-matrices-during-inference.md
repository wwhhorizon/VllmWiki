# vllm-project/vllm#7736: [Usage]: Is there an option to obtain attention matrices during inference, similar to the output_attentions=True parameter in the transformers package?

| 字段 | 值 |
| --- | --- |
| Issue | [#7736](https://github.com/vllm-project/vllm/issues/7736) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is there an option to obtain attention matrices during inference, similar to the output_attentions=True parameter in the transformers package?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Feature Request: Access to Attention Matrices and/or KV-Cache during Inference I'm wondering if there's a way to obtain attention matrices or access the KV-Cache during inference with vLLM, similar to how the transformers package allows this with the output_attensions=True parameter or through the past_key_values attribute.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: the output_attentions=True parameter in the transformers package? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Feature Request: Access to...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: u like to use vllm Feature Request: Access to Attention Matrices and/or KV-Cache during Inference I'm wondering if there's a way to obtain attention matrices or access the KV-Cache during inference with vLLM, similar to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
