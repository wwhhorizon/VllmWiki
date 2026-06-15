# vllm-project/vllm#480: Reproduce the given benchmark results

| 字段 | 值 |
| --- | --- |
| Issue | [#480](https://github.com/vllm-project/vllm/issues/480) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Reproduce the given benchmark results

### Issue 正文摘录

Hello，I would like to know which model and test tool are used for the performance data provided on the homepage? Is the model available on https://huggingface.co/?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Reproduce the given benchmark results Hello，I would like to know which model and test tool are used for the performance data provided on the homepage? Is the model available on https://huggingface.co/?
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Reproduce the given benchmark results Hello，I would like to know which model and test tool are used for the performance data provided on the homepage? Is the model available on https://huggingface.co/?
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Reproduce the given benchmark results Hello，I would like to know which model and test tool are used for the performance data provided on the homepage? Is the model available on https://huggingface.co/?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
