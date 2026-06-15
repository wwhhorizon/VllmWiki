# vllm-project/vllm#2663: [BUG] Quantization support for MoE models

| 字段 | 值 |
| --- | --- |
| Issue | [#2663](https://github.com/vllm-project/vllm/issues/2663) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [BUG] Quantization support for MoE models

### Issue 正文摘录

After #2453 and #2542, the new fused MoE kernel used in Mixtral and DeepSeek-MoE does not support quantization.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [BUG] Quantization support for MoE models After #2453 and #2542, the new fused MoE kernel used in Mixtral and DeepSeek-MoE does not support quantization.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [BUG] Quantization support for MoE models After #2453 and #2542, the new fused MoE kernel used in Mixtral and DeepSeek-MoE does not support quantization.
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [BUG] Quantization support for MoE models After #2453 and #2542, the new fused MoE kernel used in Mixtral and DeepSeek-MoE does not support quantization.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
