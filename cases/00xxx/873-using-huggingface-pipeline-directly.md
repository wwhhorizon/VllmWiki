# vllm-project/vllm#873: Using HuggingFace pipeline directly

| 字段 | 值 |
| --- | --- |
| Issue | [#873](https://github.com/vllm-project/vllm/issues/873) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Using HuggingFace pipeline directly

### Issue 正文摘录

How can we use pipeline directly with vLLM? Or using loaded model with LlamaForCausalLM directly with vLLM. Is it possible? How about passing `GenerationConfig` and quantization config?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Using HuggingFace pipeline directly How can we use pipeline directly with vLLM? Or using loaded model with LlamaForCausalLM directly with vLLM. Is it possible? How about passing `GenerationConfig` and quantization confi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ctly with vLLM. Is it possible? How about passing `GenerationConfig` and quantization config?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
