# vllm-project/vllm#2373: Speed up awq quant？

| 字段 | 值 |
| --- | --- |
| Issue | [#2373](https://github.com/vllm-project/vllm/issues/2373) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Speed up awq quant？

### Issue 正文摘录

I tested the awq quantitative inference of the llama model of the two frameworks vllm and trtllm. Using the same quantification method, we found that the linear layer calculation of trtllm is faster. Is it due to the poor performance of the awq gemm kernel in vllm? Can the kernel calculation in trtllm be transplanted to vllm? Because they are all calculated by w8A16, there is essentially no difference.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Speed up awq quant？ I tested the awq quantitative inference of the llama model of the two frameworks vllm and trtllm. Using the same quantification method, we found that the linear layer calculation of trtllm is faster....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Speed up awq quant？ I tested the awq quantitative inference of the llama model of the two frameworks vllm and trtllm. Using the same quantification method, we found that the linear layer calculation of trtllm is faster....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: lation of trtllm is faster. Is it due to the poor performance of the awq gemm kernel in vllm? Can the kernel calculation in trtllm be transplanted to vllm? Because they are all calculated by w8A16, there is essentially...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Speed up awq quant？ I tested the awq quantitative inference of the llama model of the two frameworks vllm and trtllm. Using the same quantification method, we found that the linear layer calculation of trtllm is faster....

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
