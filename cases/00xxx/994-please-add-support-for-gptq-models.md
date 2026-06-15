# vllm-project/vllm#994: Please add support for GPTQ models

| 字段 | 值 |
| --- | --- |
| Issue | [#994](https://github.com/vllm-project/vllm/issues/994) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Please add support for GPTQ models

### Issue 正文摘录

I'd love to run this model with VLLM, but I get an error currently due to quantization! https://huggingface.co/TheBloke/Llama-2-13B-chat-GPTQ

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Please add support for GPTQ models I'd love to run this model with VLLM, but I get an error currently due to quantization! https://huggingface.co/TheBloke/Llama-2-13B-chat-GPTQ
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 'd love to run this model with VLLM, but I get an error currently due to quantization! https://huggingface.co/TheBloke/Llama-2-13B-chat-GPTQ

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
