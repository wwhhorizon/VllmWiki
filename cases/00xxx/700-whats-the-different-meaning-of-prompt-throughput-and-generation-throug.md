# vllm-project/vllm#700: whats the different meaning of prompt throughput and generation throughput

| 字段 | 值 |
| --- | --- |
| Issue | [#700](https://github.com/vllm-project/vllm/issues/700) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> whats the different meaning of prompt throughput and generation throughput

### Issue 正文摘录

hello gus! im not quite get the meaning about` prompt throughput` and `generation throughput` because when i use long-text to do inference ,the ` prompt throughput` is so much high like 3thouands/s and the `generation throughput` nearly 0-7 tokens/s but when i use normal-length context like 100 etc. the `generation throughput` becomes normal but ` prompt throughput` somotimes goes to 0. i want to know whats the different meaning of the two? using 1 req: `Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 27.8 tokens/s`

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: whats the different meaning of prompt throughput and generation throughput hello gus! im not quite get the meaning about` prompt throughput` and `generation throughput` because when i use long-text to do inference ,the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
