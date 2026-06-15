# vllm-project/vllm#1823: ValueError: torch.bfloat16 is not supported for quantization method awq. Supported dtypes: [torch.float16]

| 字段 | 值 |
| --- | --- |
| Issue | [#1823](https://github.com/vllm-project/vllm/issues/1823) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ValueError: torch.bfloat16 is not supported for quantization method awq. Supported dtypes: [torch.float16]

### Issue 正文摘录

I want to use qwen's awq model, but an error occurred. How can I solve this problem?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ValueError: torch.bfloat16 is not supported for quantization method awq. Supported dtypes: [torch.float16] I want to use qwen's awq model, but an error occurred. How can I solve this problem?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: quantization method awq. Supported dtypes: [torch.float16] I want to use qwen's awq model, but an error occurred. How can I solve this problem?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
