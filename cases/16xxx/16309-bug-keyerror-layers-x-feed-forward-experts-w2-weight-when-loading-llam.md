# vllm-project/vllm#16309: [Bug]: KeyError: 'layers.X.feed_forward.experts.w2_weight' when loading Llama 4 Scout W4A16 (quantized via llmcompressor)

| 字段 | 值 |
| --- | --- |
| Issue | [#16309](https://github.com/vllm-project/vllm/issues/16309) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'layers.X.feed_forward.experts.w2_weight' when loading Llama 4 Scout W4A16 (quantized via llmcompressor)

### Issue 正文摘录

lemme rewrite the issue. there was something wrong

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: yers.X.feed_forward.experts.w2_weight' when loading Llama 4 Scout W4A16 (quantized via llmcompressor) bug lemme rewrite the issue. there was something wrong
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: KeyError: 'layers.X.feed_forward.experts.w2_weight' when loading Llama 4 Scout W4A16 (quantized via llmcompressor) bug lemme rewrite the issue. there was something wrong
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: KeyError: 'layers.X.feed_forward.experts.w2_weight' when loading Llama 4 Scout W4A16 (quantized via llmcompressor) bug lemme rewrite the issue. there was something wrong

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
