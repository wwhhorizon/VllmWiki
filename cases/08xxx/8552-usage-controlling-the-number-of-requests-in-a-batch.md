# vllm-project/vllm#8552: [Usage]: Controlling the number of requests in a batch

| 字段 | 值 |
| --- | --- |
| Issue | [#8552](https://github.com/vllm-project/vllm/issues/8552) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Controlling the number of requests in a batch

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hello, I am quite new to vLLM setup. Can you help me with this? Suppose during online inference, I have requests waiting in queue to be processed and a batched request (assume batch size =100) is running. Out of that batch, let us say that 10 requests have been completed (both prefill and decode) so we have got space for 10 new requests to enter in that batch. Now 10 requests from the queue will be shifted to that batch for prefill. So, my doubt is can I control the number of running requests in a batch i.e. when 10 requests in a batch gets completed, I don't want to push 10 requests from the queue to that batch; instead I want to push requests into that batch only when current number of running requests in that batch goes down to (say) 40, not before. That's when I want to push 60 requests in that batch. So is there any engine argument that can control this feature. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/la...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Usage]: Controlling the number of requests in a batch usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hello, I am quite new to vLLM setup. C...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: re. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
