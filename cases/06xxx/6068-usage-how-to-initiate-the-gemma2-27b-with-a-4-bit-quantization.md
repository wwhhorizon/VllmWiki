# vllm-project/vllm#6068: [Usage]: how to initiate the gemma2-27b with a 4-bit quantization?

| 字段 | 值 |
| --- | --- |
| Issue | [#6068](https://github.com/vllm-project/vllm/issues/6068) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to initiate the gemma2-27b with a 4-bit quantization?

### Issue 正文摘录

### Your current environment how to initiate the gemma2-27b with a 4-bit quantization? ### How would you like to use vllm Could you please explain how to initiate the gemma2-27b with a 4-bit quantization?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Usage]: how to initiate the gemma2-27b with a 4-bit quantization? usage ### Your current environment how to initiate the gemma2-27b with a 4-bit quantization? ### How would you like to use vllm Could you please explain...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: how to initiate the gemma2-27b with a 4-bit quantization? usage ### Your current environment how to initiate the gemma2-27b with a 4-bit quantization? ### How would you like to use vllm Could you please explain...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: how to initiate the gemma2-27b with a 4-bit quantization? usage ### Your current environment how to initiate the gemma2-27b with a 4-bit quantization? ### How would you like to use vllm Could you please explain...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
