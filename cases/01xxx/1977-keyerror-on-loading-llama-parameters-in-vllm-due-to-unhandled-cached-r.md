# vllm-project/vllm#1977: KeyError on Loading LLaMA Parameters in vLLM due to Unhandled Cached Rotary Embeddings

| 字段 | 值 |
| --- | --- |
| Issue | [#1977](https://github.com/vllm-project/vllm/issues/1977) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> KeyError on Loading LLaMA Parameters in vLLM due to Unhandled Cached Rotary Embeddings

### Issue 正文摘录

While integrating the LLaMA model with vLLM, I encountered a KeyError related to the rotary embeddings' cached cosine and sine values (`cos_cached` and `sin_cached`). These parameters, while present in LLaMA, are not directly handled or required by vLLM. This results in a conflict when loading the model with these cached values.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: KeyError on Loading LLaMA Parameters in vLLM due to Unhandled Cached Rotary Embeddings While integrating the LLaMA model with vLLM, I encountered a KeyError related to the rotary embeddings' cached cosine and sine value...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
