# vllm-project/vllm#2866: Add a model to the model executor list that is derived from RagTokenForGeneration model

| 字段 | 值 |
| --- | --- |
| Issue | [#2866](https://github.com/vllm-project/vllm/issues/2866) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add a model to the model executor list that is derived from RagTokenForGeneration model

### Issue 正文摘录

How do I add a model executor that is derived from the huggingface model class [RagTokenForGeneration](https://huggingface.co/docs/transformers/en/model_doc/rag#transformers.RagTokenForGeneration). I could only find this [link](https://docs.vllm.ai/en/latest/models/adding_model.html) that documents about adding a new model. Can someone elaborate for this use case. Thanks

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Add a model to the model executor list that is derived from RagTokenForGeneration model How do I add a model executor that is derived from the huggingface model class [RagTokenForGeneration](https://huggingface.co/docs/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: el_doc/rag#transformers.RagTokenForGeneration). I could only find this [link](https://docs.vllm.ai/en/latest/models/adding_model.html) that documents about adding a new model. Can someone elaborate for this use case. Th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ForGeneration). I could only find this [link](https://docs.vllm.ai/en/latest/models/adding_model.html) that documents about adding a new model. Can someone elaborate for this use case. Thanks

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
