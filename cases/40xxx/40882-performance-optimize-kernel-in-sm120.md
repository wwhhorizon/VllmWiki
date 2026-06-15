# vllm-project/vllm#40882: [Performance]: Optimize kernel in SM120

| 字段 | 值 |
| --- | --- |
| Issue | [#40882](https://github.com/vllm-project/vllm/issues/40882) |
| 状态 | open |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Optimize kernel in SM120

### Issue 正文摘录

### Proposal to improve performance Evaluate how to use https://github.com/lukealonso/b12x in vllm to optimize the performance to run vLLM in DGX Spark ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) Evaluate how to use https://github.com/lukealonso/b12x in vllm to optimize the performance to run vLLM in DGX Spark ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ptimize kernel in SM120 performance ### Proposal to improve performance Evaluate how to use https://github.com/lukealonso/b12x in vllm to optimize the performance to run vLLM in DGX Spark ### Report of performance regre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Performance]: Optimize kernel in SM120 performance ### Proposal to improve performance Evaluate how to use https://github.com/lukealonso/b12x in vllm to optimize the performance to run vLLM in DGX Spark ### Report of p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
