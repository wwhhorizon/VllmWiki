# vllm-project/vllm#1545: The AWQ model's sampling time cost of first generate token is much slower than FP16 model

| 字段 | 值 |
| --- | --- |
| Issue | [#1545](https://github.com/vllm-project/vllm/issues/1545) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The AWQ model's sampling time cost of first generate token is much slower than FP16 model

### Issue 正文摘录

After a lots of test, I found that the first token latency on awq weight model is slower than FP16 weight model, and logs shown that the sampling process of first token of AWQ model is 2-5x(depends on the length of input) slower than FP16 model, but 30x faster than FP16 model in the following tokens. Considering the sampling process of long prompt is really slow, sampling become a obvious bottleneck for awq model, and I can't catch which line cause this situation, it seems there are lots of async operations in the sampling process?

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: t of first generate token is much slower than FP16 model After a lots of test, I found that the first token latency on awq weight model is slower than FP16 weight model, and logs shown that the sampling process of first...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: The AWQ model's sampling time cost of first generate token is much slower than FP16 model After a lots of test, I found that the first token latency on awq weight model is slower than FP16 weight model, and logs shown t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
