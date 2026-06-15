# vllm-project/vllm#966: Non-deterministic outputs for llama2

| 字段 | 值 |
| --- | --- |
| Issue | [#966](https://github.com/vllm-project/vllm/issues/966) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Non-deterministic outputs for llama2

### Issue 正文摘录

For some adversarially optimized prompts, it seems that llama2 running on vllm returns slightly different generations from time to time. Does anyone know what could be causing this, and if it's possible to fix this? My suspicion is the model shards not being reduced in the same order every time which leads to different floating point values due to non-associativity.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: Non-deterministic outputs for llama2 bug For some adversarially optimized prompts, it seems that llama2 running on vllm returns slightly different generations from time to time. Does anyone know what could be causing thi
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Non-deterministic outputs for llama2 bug For some adversarially optimized prompts, it seems that llama2 running on vllm returns slightly different generations from time to time. Does anyone know what could be causing th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ow what could be causing this, and if it's possible to fix this? My suspicion is the model shards not being reduced in the same order every time which leads to different floating point values due to non-associativity.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Non-deterministic outputs for llama2 bug For some adversarially optimized prompts, it seems that llama2 running on vllm returns slightly different generations from time to time. Does anyone know what could be causing th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
