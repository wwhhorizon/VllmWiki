# vllm-project/vllm#5095: [New Model]: IBM Granite Code Models

| 字段 | 值 |
| --- | --- |
| Issue | [#5095](https://github.com/vllm-project/vllm/issues/5095) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: IBM Granite Code Models

### Issue 正文摘录

### The model to consider. https://huggingface.co/collections/ibm-granite/granite-code-models-6624c5cec322e4c148c8b330 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? https://github.com/huggingface/transformers/pull/30031 Granite requires a transformers upgrade. If it is executed, the model still does not work correctly when running through vLLM.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: IBM Granite Code Models new-model ### The model to consider. https://huggingface.co/collections/ibm-granite/granite-code-models-6624c5cec322e4c148c8b330 ### The closest model vllm already supports. _No resp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
