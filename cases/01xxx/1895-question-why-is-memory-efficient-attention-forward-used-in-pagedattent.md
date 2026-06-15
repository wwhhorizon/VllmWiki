# vllm-project/vllm#1895: Question: Why is `memory_efficient_attention_forward` used in PagedAttention?

| 字段 | 值 |
| --- | --- |
| Issue | [#1895](https://github.com/vllm-project/vllm/issues/1895) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question: Why is `memory_efficient_attention_forward` used in PagedAttention?

### Issue 正文摘录

Hello everybody, During my development of [candle-vllm](https://github.com/EricLBuehler/candle-vllm), I am implementing PagedAttention based on the implementation here. However, I noticed that in the `.forward` method, a [call to `xops.memory_efficient_attention_forward`](https://github.com/vllm-project/vllm/blob/f86bd6190ad300051fce5f0a13ba03b29e5e199a/vllm/model_executor/layers/attention.py#L156C24-L156C58) is made if the input is a prompt. Can this be substituted for a "normal" attention? Thanks!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Question: Why is `memory_efficient_attention_forward` used in PagedAttention? Hello everybody, During my development of [candle-vllm](https://github.com/EricLBuehler/candle-vllm), I am implementing PagedAttention based...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/f86bd6190ad300051fce5f0a13ba03b29e5e199a/vllm/model_executor/layers/attention.py#L156C24-L156C58) is made if the input is a prompt. Can this be substituted for a "normal" attention? Thanks!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
