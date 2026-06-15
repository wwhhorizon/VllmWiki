# vllm-project/vllm#1189: Automatically configure `max_num_batched_tokens` based on model length

| 字段 | 值 |
| --- | --- |
| Issue | [#1189](https://github.com/vllm-project/vllm/issues/1189) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Automatically configure `max_num_batched_tokens` based on model length

### Issue 正文摘录

BTW, can you set the `max_num_batched_tokens` argument default value to 4096 or 8192 since many LLMs have supported 4096/8192 prompt now. _Originally posted by @irasin in https://github.com/vllm-project/vllm/issues/1018#issuecomment-1714852004_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Automatically configure `max_num_batched_tokens` based on model length BTW, can you set the `max_num_batched_tokens` argument default value to 4096 or 8192 since many LLMs have supported 4096/8192 prompt now. _Originall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
