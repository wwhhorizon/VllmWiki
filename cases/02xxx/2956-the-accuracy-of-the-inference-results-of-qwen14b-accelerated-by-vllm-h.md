# vllm-project/vllm#2956: The accuracy of the inference results of qwen14B accelerated by VLLM has decreased

| 字段 | 值 |
| --- | --- |
| Issue | [#2956](https://github.com/vllm-project/vllm/issues/2956) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The accuracy of the inference results of qwen14B accelerated by VLLM has decreased

### Issue 正文摘录

Hello!Here's my issue: I have recently noticed that there is inconsistency between the results of streaming inference using vllm-accelerated qwen14B and the original qwen inference, leading to a decrease in accuracy. Could you please investigate and address this issue? Thank you very much for your assistance and support.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: The accuracy of the inference results of qwen14B accelerated by VLLM has decreased Hello!Here's my issue: I have recently noticed that there is inconsistency between the results of streaming inference using vllm-acceler...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: The accuracy of the inference results of qwen14B accelerated by VLLM has decreased Hello!Here's my issue: I have recently noticed that there is inconsistency between the results of streaming inference using vllm-acceler...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: The accuracy of the inference results of qwen14B accelerated by VLLM has decreased Hello!Here's my issue: I have recently noticed that there is inconsistency between the results of streaming inference using vllm-acceler...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
