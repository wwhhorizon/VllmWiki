# vllm-project/vllm#272: Different from the output of the HF inference

| 字段 | 值 |
| --- | --- |
| Issue | [#272](https://github.com/vllm-project/vllm/issues/272) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Different from the output of the HF inference

### Issue 正文摘录

Looking forward to your reply! I set the temperature=0.1, top-k=10, top-p=0.75，I think i infer the same prompt, I will get the same output, through test the hf and vllm inference, HF will get stable output then vllm sometimes get the different output. Is this normal? The parameters of the two inferences are the same and do not bring the same constraints.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: .1, top-k=10, top-p=0.75，I think i infer the same prompt, I will get the same output, through test the hf and vllm inference, HF will get stable output then vllm sometimes get the different output. Is this normal? The p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Different from the output of the HF inference Looking forward to your reply! I set the temperature=0.1, top-k=10, top-p=0.75，I think i infer the same prompt, I will get the same output, through test the hf and vllm infe...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: e HF inference Looking forward to your reply! I set the temperature=0.1, top-k=10, top-p=0.75，I think i infer the same prompt, I will get the same output, through test the hf and vllm inference, HF will get stable outpu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: .75，I think i infer the same prompt, I will get the same output, through test the hf and vllm inference, HF will get stable output then vllm sometimes get the different output. Is this normal? The parameters of the two...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
