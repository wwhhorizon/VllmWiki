# vllm-project/vllm#1138: Can we get quantization for GPT2LMHeadModel supported?

| 字段 | 值 |
| --- | --- |
| Issue | [#1138](https://github.com/vllm-project/vllm/issues/1138) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can we get quantization for GPT2LMHeadModel supported?

### Issue 正文摘录

At the moment, vLLM only supports quantization for LlamaForCausalLM model. Can we add quantization support for GPT2LMHeadModel as well?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Can we get quantization for GPT2LMHeadModel supported? At the moment, vLLM only supports quantization for LlamaForCausalLM model. Can we add quantization support for GPT2LMHeadModel as well?
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Can we get quantization for GPT2LMHeadModel supported? At the moment, vLLM only supports quantization for LlamaForCausalLM model. Can we add quantization support for GPT2LMHeadModel as well?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
