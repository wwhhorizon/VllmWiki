# vllm-project/vllm#1592: Mistral 7B with AWQ - bfloat16 error

| 字段 | 值 |
| --- | --- |
| Issue | [#1592](https://github.com/vllm-project/vllm/issues/1592) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Mistral 7B with AWQ - bfloat16 error

### Issue 正文摘录

I saw @WoosukKwon's msg [here](https://github.com/vllm-project/vllm/issues/1433#issuecomment-1772995719) on how to setup AWQ. I downloaded the weights from the bloke [here](https://huggingface.co/TheBloke/Mistral-7B-v0.1-AWQ) but I'm having issues with Mistral as it's bfloat16 and currently for quantization it seems you have some assumptions that the model should be float16 only? What's the state with Mistral has anyone run a quantized version? Thanks!

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Mistral 7B with AWQ - bfloat16 error I saw @WoosukKwon's msg [here](https://github.com/vllm-project/vllm/issues/1433#issuecomment-1772995719) on how to setup AWQ. I downloaded the weights from the bloke [here](https://h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ow to setup AWQ. I downloaded the weights from the bloke [here](https://huggingface.co/TheBloke/Mistral-7B-v0.1-AWQ) but I'm having issues with Mistral as it's bfloat16 and currently for quantization it seems you have s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: float16 only? What's the state with Mistral has anyone run a quantized version? Thanks!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
