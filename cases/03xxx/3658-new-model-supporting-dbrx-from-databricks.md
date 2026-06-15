# vllm-project/vllm#3658: [New Model]: Supporting DBRX from Databricks

| 字段 | 值 |
| --- | --- |
| Issue | [#3658](https://github.com/vllm-project/vllm/issues/3658) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Supporting DBRX from Databricks

### Issue 正文摘录

### The model to consider. Databricks has released [DBRX](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm), which consists of 2 models - [dbrx](https://huggingface.co/databricks/dbrx-base) - [dbrx-instruct](https://huggingface.co/databricks/dbrx-instruct) It's a 132B parameter MoE model. Might be useful. ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? It seems that they have a custom script in their files, might need custom implementation on that regard.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: Supporting DBRX from Databricks new-model ### The model to consider. Databricks has released [DBRX](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm), which consists of 2 models - [db...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: . Databricks has released [DBRX](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm), which consists of 2 models - [dbrx](https://huggingface.co/databricks/dbrx-base) - [dbrx-instruct](https://huggi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: (https://huggingface.co/databricks/dbrx-instruct) It's a 132B parameter MoE model. Might be useful. ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want?...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
