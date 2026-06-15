# vllm-project/vllm#7528: [Tracking issue] [Help wanted]: Multi-step scheduling follow-ups

| 字段 | 值 |
| --- | --- |
| Issue | [#7528](https://github.com/vllm-project/vllm/issues/7528) |
| 状态 | closed |
| 标签 | help wanted;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracking issue] [Help wanted]: Multi-step scheduling follow-ups

### Issue 正文摘录

Co-authored with @SolitaryThinker @Yard1 @rkooo567 We are landing multi-step scheduling (#7000) to amortize scheduling overhead for better ITL and throughput. Since the first version of multi-step scheduling doesn't work with some existing features, this issue tracks the progress to support them so that multi-step scheduling could become a common and practical feature in vLLM. ## Performance ### Chunked Prefill It is tricky for multi-step scheduling to work with chunked prefill because of the following reasons: 1. Chunked prefill schedules prefill and decode requests to the same batch. 2. Prefill requests only need a few steps (at maximum `prompt_tokens / chunk_size` steps), which could be much less than the configured multi-steps (i.e., 8). 3. We cannot turn a prefill request into a decode request without re-scheduling and re-preparing inputs. As a result, we need a schedule policy to deal with prefill requests in multi-step scheduling. Here are 2 possible policies we could consider at this moment: 1. **Force Single Step**: We force single step when there are prefill requests in a batch. This may work well for offline batching, but not good for online serving because new requests...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: cking issue] [Help wanted]: Multi-step scheduling follow-ups help wanted;stale Co-authored with @SolitaryThinker @Yard1 @rkooo567 We are landing multi-step scheduling (#7000) to amortize scheduling overhead for better I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rtize scheduling overhead for better ITL and throughput. Since the first version of multi-step scheduling doesn't work with some existing features, this issue tracks the progress to support them so that multi-step sched...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m `prompt_tokens / chunk_size` steps), which could be much less than the configured multi-steps (i.e., 8). 3. We cannot turn a prefill request into a decode request without re-scheduling and re-preparing inputs. As a re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ep scheduling (#7000) to amortize scheduling overhead for better ITL and throughput. Since the first version of multi-step scheduling doesn't work with some existing features, this issue tracks the progress to support t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
