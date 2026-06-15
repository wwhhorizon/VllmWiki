# vllm-project/vllm#9346: [Usage]: Obtaining success / error rate % metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#9346](https://github.com/vllm-project/vllm/issues/9346) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Obtaining success / error rate % metrics

### Issue 正文摘录

### Your current environment Running vLLM v0.5.1 on GKE, but my exact setup isn't relevant to the question below ### How would you like to use vllm I see that in [vllm/engine/metrics.py](https://github.com/vllm-project/vllm/blob/main/vllm/engine/metrics.py#L144C19-L144C45) there is a success count metric, split up by success reason (anecdotally for me `length` and `stop`). Is it currently possible to get a success rate % metric by dividing this by a denominator? What denominator should I use here -- maybe `num_requests_running` or `time_to_first_token_seconds_count`? I tried both, but they didn't seem to provide the right result (in that the ratio could potentially momentarily go above 100). If there was a error count metric, I could graph success % as the fraction success / (success + error). Is that in the works? I see [a roadmap](https://github.com/vllm-project/vllm/issues/3616#issuecomment-2030858781) from April which states that `request_failure` is a planned addition, but wasn't sure if this is up to date. Thanks! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [docu...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Obtaining success / error rate % metrics usage;stale ### Your current environment Running vLLM v0.5.1 on GKE, but my exact setup isn't relevant to the question below ### How would you like to use vllm I see tha...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
