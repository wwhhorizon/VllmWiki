# vllm-project/vllm#1569: Support Dynamic SplitFuse 

| 字段 | 值 |
| --- | --- |
| Issue | [#1569](https://github.com/vllm-project/vllm/issues/1569) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support Dynamic SplitFuse 

### Issue 正文摘录

https://github.com/microsoft/DeepSpeed/tree/master/blogs/deepspeed-fastgen#background In their experiment, DeepSpeed-FastGen outperforms vLLM in both throughput and latency, providing equivalent latency with greater throughput or more responsive latency and the same throughput. I think the main reason is the dynamic splitFuse method, can vllm support it ?

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ckground In their experiment, DeepSpeed-FastGen outperforms vLLM in both throughput and latency, providing equivalent latency with greater throughput or more responsive latency and the same throughput. I think the main...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
