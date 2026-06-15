# vllm-project/vllm#3756: [New Model]: CohereForAI/c4ai-command-r-v01-4bit

| 字段 | 值 |
| --- | --- |
| Issue | [#3756](https://github.com/vllm-project/vllm/issues/3756) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: CohereForAI/c4ai-command-r-v01-4bit

### Issue 正文摘录

### The model to consider. [[https://huggingface.co/openai-community/](https://huggingface.co/CohereForAI/c4ai-command-r-v01-4bit](https://huggingface.co/CohereForAI/c4ai-command-r-v01-4bit) ### The closest model vllm already supports. https://huggingface.co/CohereForAI/c4ai-command-r-v01 ### What's your difficulty of supporting the model you want? No idea if vLLM supports this type of quantization, but if its possible would be eternally grateful for the model support, as one will become able to run it even on weaker setups.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: CohereForAI/c4ai-command-r-v01-4bit new-model ### The model to consider. [[https://huggingface.co/openai-community/](https://huggingface.co/CohereForAI/c4ai-command-r-v01-4bit](https://huggingface.co/Cohere...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: of supporting the model you want? No idea if vLLM supports this type of quantization, but if its possible would be eternally grateful for the model support, as one will become able to run it even on weaker setups.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
