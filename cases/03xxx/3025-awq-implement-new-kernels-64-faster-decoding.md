# vllm-project/vllm#3025: AWQ: Implement new kernels (64% faster decoding)

| 字段 | 值 |
| --- | --- |
| Issue | [#3025](https://github.com/vllm-project/vllm/issues/3025) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AWQ: Implement new kernels (64% faster decoding)

### Issue 正文摘录

According to my testing, it's possible to get even faster decoding than if you were to use ExLlamaV2 kernels. The prefilling speed is roughly the same as the current GEMM kernels (including the dequantize + torch.matmul trick). Reference: https://github.com/casper-hansen/AutoAWQ/pull/365

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ing speed is roughly the same as the current GEMM kernels (including the dequantize + torch.matmul trick). Reference: https://github.com/casper-hansen/AutoAWQ/pull/365
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: AWQ: Implement new kernels (64% faster decoding) stale According to my testing, it's possible to get even faster decoding than if you were to use ExLlamaV2 kernels. The prefilling speed is roughly the same as the curren...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ing, it's possible to get even faster decoding than if you were to use ExLlamaV2 kernels. The prefilling speed is roughly the same as the current GEMM kernels (including the dequantize + torch.matmul trick). Reference:...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: LlamaV2 kernels. The prefilling speed is roughly the same as the current GEMM kernels (including the dequantize + torch.matmul trick). Reference: https://github.com/casper-hansen/AutoAWQ/pull/365
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: AWQ: Implement new kernels (64% faster decoding) stale According to my testing, it's possible to get even faster decoding than if you were to use ExLlamaV2 kernels. The prefilling speed is roughly the same as the curren...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
