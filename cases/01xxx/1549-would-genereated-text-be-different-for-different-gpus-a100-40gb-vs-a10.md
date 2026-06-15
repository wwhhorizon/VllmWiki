# vllm-project/vllm#1549: would genereated text be different for different gpus A100(40GB) vs A10G(24GB) for same finetuned model

| 字段 | 值 |
| --- | --- |
| Issue | [#1549](https://github.com/vllm-project/vllm/issues/1549) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> would genereated text be different for different gpus A100(40GB) vs A10G(24GB) for same finetuned model

### Issue 正文摘录

TLDR : vllm is great. though i have a question i have finetuned a mistral on A100 40GB (QLora) and merged the model. I see the model is quite consitent on A100 but when i infer the same model on A10G (24GB), with same parameter the model output text is inconsistent mostly. dependencies are same. but cuda version is 11.7 vs cuda 12.2 . i am using dtype = bfloat16 for both and trained with bfloat. any suggestions ... i might be doing something wrong or it's normal !!! also when i use inference api using openai.api_server output is little different for same parameters.. i understand that mostly due to randomness. Thanks

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ependencies are same. but cuda version is 11.7 vs cuda 12.2 . i am using dtype = bfloat16 for both and trained with bfloat. any suggestions ... i might be doing something wrong or it's normal !!! also when i use inferen...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ith same parameter the model output text is inconsistent mostly. dependencies are same. but cuda version is 11.7 vs cuda 12.2 . i am using dtype = bfloat16 for both and trained with bfloat. any suggestions ... i might b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: would genereated text be different for different gpus A100(40GB) vs A10G(24GB) for same finetuned model TLDR : vllm is great. though i have a question i have finetuned a mistral on A100 40GB (QLora) and merged the model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: different for different gpus A100(40GB) vs A10G(24GB) for same finetuned model TLDR : vllm is great. though i have a question i have finetuned a mistral on A100 40GB (QLora) and merged the model. I see the model is quit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
