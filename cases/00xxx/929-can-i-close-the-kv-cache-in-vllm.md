# vllm-project/vllm#929: Can I close the kv cache in vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#929](https://github.com/vllm-project/vllm/issues/929) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can I close the kv cache in vllm?

### Issue 正文摘录

Turning on KV cache will cause the model to use historical data to generate answers every time. I don't want the model to use historical data to generate answers, so I want to turn off KV cache. Is there any configuration item in vllm that can turn off KV cache?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Can I close the kv cache in vllm? Turning on KV cache will cause the model to use historical data to generate answers every time. I don't want the model to use historical data to generate answers, so I want to turn off...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Can I close the kv cache in vllm? Turning on KV cache will cause the model to use historical data to generate answers every time. I don't want the model to use historical data to generate answers, so I want to turn off...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
