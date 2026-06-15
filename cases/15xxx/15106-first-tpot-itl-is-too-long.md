# vllm-project/vllm#15106: First tpot/itl is too long?

| 字段 | 值 |
| --- | --- |
| Issue | [#15106](https://github.com/vllm-project/vllm/issues/15106) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> First tpot/itl is too long?

### Issue 正文摘录

I discovered a somewhat strange (or is it reasonable?) phenomenon: For example, I started a vllm OpenAI server with chunked prefill=True and max_num_batched_tokens=2k, then sent an input of 5k tokens using the /chat endpoint with stream=True. The server first returned a token that includes the role but with an empty content, taking 0.9 seconds (on my hardware and model, the prefill time for 2k tokens is 0.9 seconds), which is counted as ttft. Then, it returned a second token with non-empty content, taking 1.3 seconds (on my hardware and model, the prefill time for 3k tokens is 1.3 seconds), which is counted as the first tpot/itl. Next, it returned a third token with non-empty content, taking 0.02 seconds (on my hardware and model, the decode time is 0.02 seconds), and all subsequent tokens took 0.02 seconds each. This is inconsistent with the tpot/itl I usually observe in benchmarks (which are all 0.02 seconds), so I traced it down to the implementation of the chat interface: https://github.com/vllm-project/vllm/blob/ed6e9075d31e32c8548b480a47d1ffb77da1f54c/vllm/entrypoints/openai/serving_chat.py#L372-L438 https://github.com/vllm-project/vllm/blob/ed6e9075d31e32c8548b480a47d1ffb77...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: First tpot/itl is too long? performance;stale I discovered a somewhat strange (or is it reasonable?) phenomenon: For example, I started a vllm OpenAI server with chunked prefill=True and max_num_batched_tokens=2k, then...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: First tpot/itl is too long? performance;stale I discovered a somewhat strange (or is it reasonable?) phenomenon: For example, I started a vllm OpenAI server with chunked prefill=True and max_num_batched_tokens=2k, then...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e role but with an empty content, taking 0.9 seconds (on my hardware and model, the prefill time for 2k tokens is 0.9 seconds), which is counted as ttft. Then, it returned a second token with non-empty content, taking 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
