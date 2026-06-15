# vllm-project/vllm#22180: [Bug]: apply_temperature may cause nan in probs

| 字段 | 值 |
| --- | --- |
| Issue | [#22180](https://github.com/vllm-project/vllm/issues/22180) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: apply_temperature may cause nan in probs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Recently, we met some illegal memory access problems. When we turned off flashinfer sampling, the problem disappeared, or at least it was much harder to trigger. Unfortunately, I can't provide a minimal reproduction here. After some investigation, I believe the problem is caused by `apply_temperature`. Suppose we have a decode batch with both random sampling and greedy sampling. [Here](https://github.com/vllm-project/vllm/blob/a7b8788d2c2fae6bf52c128916de19e85f2b0a25/vllm/v1/worker/gpu_input_batch.py#L306) will set the temperature for greedy sampling to -1.0, and [here](https://github.com/vllm-project/vllm/blob/a7b8788d2c2fae6bf52c128916de19e85f2b0a25/vllm/v1/sample/sampler.py#L99) will div all the logits against temperature. If the logits (for greedy sampling) contains `-inf`, it will become `inf` after the division, and hence the probs tensor will be fully `nan`, I guess maybe it will cause bad things when using flashinfer top_p sampling. I'm not 100% sure about this, because I use probs with `nan` to run against flashinfer top_p sampling, and compute-sanitizer can't find any problems. But anyway, `nan` in probs is dangerous, I...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Recently, we met some illegal memory access problems. When we turned off flashinfer sampling, the problem disappeared, or at least it was much harder to trigger. Unfortunately, I can't provide a minimal reproduction her...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: believe the problem is caused by `apply_temperature`. Suppose we have a decode batch with both random sampling and greedy sampling. [Here](https://github.com/vllm-project/vllm/blob/a7b8788d2c2fae6bf52c128916de19e85f2b0a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
