# vllm-project/vllm#6563: [New Model]: Mistral-Nemo

| 字段 | 值 |
| --- | --- |
| Issue | [#6563](https://github.com/vllm-project/vllm/issues/6563) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Mistral-Nemo

### Issue 正文摘录

### The model to consider. https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407 ### The closest model vllm already supports. - https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/llama.py - https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mixtral.py ### What's your difficulty of supporting the model you want? _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Mistral-Nemo new-model ### The model to consider. https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407 ### The closest model vllm already supports. - https://github.com/vllm-project/vllm/blob/main/vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
