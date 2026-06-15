# vllm-project/vllm#5016: [Feature] [Spec decode]: Combine chunked prefill with speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#5016](https://github.com/vllm-project/vllm/issues/5016) |
| 状态 | closed |
| 标签 | feature request;speculative-decoding;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] [Spec decode]: Combine chunked prefill with speculative decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Speculative decoding can achieve 50%+ latency reduction, but in vLLM it can suffer from the throughput-optimized default scheduling strategy where prefills are prioritized eagerly. Chunked prefill is a recent work in vLLM which optimizes this by spreading out the prefill work over many different decode batches. We can combine chunked prefill with speculative decoding's dynamic speculation length to get the best of both worlds. This is a complex task that requires some design, if you're interested please reach out. ### Alternatives _No response_ ### Additional context cc @LiuXiaoxuanPKU @comaniac @rkooo567

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Feature] [Spec decode]: Combine chunked prefill with speculative decoding feature request;speculative-decoding;stale ### 🚀 The feature, motivation and pitch Speculative decoding can achieve 50%+ latency reduction, but...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: The feature, motivation and pitch Speculative decoding can achieve 50%+ latency reduction, but in vLLM it can suffer from the throughput-optimized default scheduling strategy where prefills are prioritized eagerly. Chun...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
