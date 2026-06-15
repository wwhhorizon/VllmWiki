# vllm-project/vllm#1167: Phi 1.5 support

| 字段 | 值 |
| --- | --- |
| Issue | [#1167](https://github.com/vllm-project/vllm/issues/1167) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Phi 1.5 support

### Issue 正文摘录

Phi 1.5 is a new model from Microsoft, supporting this model would be extremely usefull. A detailed list of info of phi 1.5 can be found here : [https://huggingface.co/microsoft/phi-1_5](url) Its basically supporting MixFormerSequentialConfig . The phi 1.5 has weird features, also 4 bit support would be great !! (and not only on gpu, but cpu also please, this model size should work ok on cpu)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Phi 1.5 support new-model Phi 1.5 is a new model from Microsoft, supporting this model would be extremely usefull. A detailed list of info of phi 1.5 can be found here : [https://huggingface.co/microsoft/phi-1_5](url) I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
