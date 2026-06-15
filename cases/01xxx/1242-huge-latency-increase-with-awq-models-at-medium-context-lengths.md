# vllm-project/vllm#1242: Huge latency increase with AWQ models at medium context lengths

| 字段 | 值 |
| --- | --- |
| Issue | [#1242](https://github.com/vllm-project/vllm/issues/1242) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Huge latency increase with AWQ models at medium context lengths

### Issue 正文摘录

Using an awq quantized model from thebloke (TheBloke/manticore-13b-chat-pyg-AWQ), generation is fine and starts after a few seconds with only a few sentences in the context window, but anything more than three or four makes it take ~30 seconds to start generation. Tried different awq models, and the issue doesn't happen with unquantized models. Is this normal/something to do with the way it handles awq models?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: rease with AWQ models at medium context lengths performance Using an awq quantized model from thebloke (TheBloke/manticore-13b-chat-pyg-AWQ), generation is fine and starts after a few seconds with only a few sentences i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Huge latency increase with AWQ models at medium context lengths performance Using an awq quantized model from thebloke (TheBloke/manticore-13b-chat-pyg-AWQ), generation is fine and starts after a few seconds with only a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Huge latency increase with AWQ models at medium context lengths performance Using an awq quantized model from thebloke (TheBloke/manticore-13b-chat-pyg-AWQ), generation is fine and starts after a few seconds with only a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
