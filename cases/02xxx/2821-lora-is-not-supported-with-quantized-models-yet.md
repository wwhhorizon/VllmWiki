# vllm-project/vllm#2821: LoRA is not supported with quantized models yet

| 字段 | 值 |
| --- | --- |
| Issue | [#2821](https://github.com/vllm-project/vllm/issues/2821) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> LoRA is not supported with quantized models yet

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/3711811b1d2956e83e626c72f0e1607f2dfbc8fb/vllm/config.py#L504 Would like to be able to use with bitsandbytes 4/8 bit, awq, etc.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: LoRA is not supported with quantized models yet https://github.com/vllm-project/vllm/blob/3711811b1d2956e83e626c72f0e1607f2dfbc8fb/vllm/config.py#L504 Would like to be able to use with bitsandbytes 4/8 bit, awq, etc.
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: LoRA is not supported with quantized models yet https://github.com/vllm-project/vllm/blob/3711811b1d2956e83e626c72f0e1607f2dfbc8fb/vllm/config.py#L504 Would like to be able to use with bitsandbytes 4/8 bit, awq, etc.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
