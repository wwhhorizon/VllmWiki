# vllm-project/vllm#968: vllm，qwen-chat长度过长时，直接输出终止符 | when input is very long(6K), vllm output end_token directly

| 字段 | 值 |
| --- | --- |
| Issue | [#968](https://github.com/vllm-project/vllm/issues/968) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm，qwen-chat长度过长时，直接输出终止符 \| when input is very long(6K), vllm output end_token directly

### Issue 正文摘录

input长度在6k左右，对于同一个api_server，短的文本（2k）可以生成摘要，但是6k的则直接输出终止符。 相同的6k长度的输入，对于调用**qwen官方的hf**的代码，可以正常输出摘要。 调了很多生成参数，结果不变。 大家有遇到过相似的吗？

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vllm，qwen-chat长度过长时，直接输出终止符 | when input is very long(6K), vllm output end_token directly input长度在6k左右，对于同一个api_server，短的文本（2k）可以生成摘要，但是6k的则直接输出终止符。 相同的6k长度的输入，对于调用**qwen官方的hf**的代码，可以正常输出摘要。 调了很多生成参数，结果不变。 大家有遇到过相似的吗？

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
