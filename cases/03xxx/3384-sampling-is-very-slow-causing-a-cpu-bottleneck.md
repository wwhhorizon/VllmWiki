# vllm-project/vllm#3384: Sampling is very slow, causing a CPU bottleneck

| 字段 | 值 |
| --- | --- |
| Issue | [#3384](https://github.com/vllm-project/vllm/issues/3384) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Sampling is very slow, causing a CPU bottleneck

### Issue 正文摘录

When running inference we see that the CPU of the VLLM process is maxed at 100%, but the GPU varies between 50-70%. For a single request, our avg generated throughput is only about 100 tokens/second. We used a Python profiler and found that more than 90% of the overall CPU time is spent in sampler.py:_sample(). In particular the slowness is exclusively due the the GPU->CPU sync from the `.cpu()` call in this code: ``` def _random_sample( selected_seq_groups: List[Tuple[List[int], SamplingParams]], is_prompts: List[bool], random_samples: torch.Tensor, ) -> List[Tuple[List[int], List[int]]]: # Find the maximum best_of value of the prompt phase requests. random_samples = random_samples.cpu() ``` Is this a known performance issue and are there any plans for a fix? Are there any other settings we should be aware of to increase our throughput? Of course, it shouldn't be the case that the CPU is the bottleneck as opposed to the GPU. Thanks

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Sampling is very slow, causing a CPU bottleneck stale When running inference we see that the CPU of the VLLM process is maxed at 100%, but the GPU varies between 50-70%. For a single request, our avg generated throughpu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: t the GPU varies between 50-70%. For a single request, our avg generated throughput is only about 100 tokens/second. We used a Python profiler and found that more than 90% of the overall CPU time is spent in sampler.py:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
