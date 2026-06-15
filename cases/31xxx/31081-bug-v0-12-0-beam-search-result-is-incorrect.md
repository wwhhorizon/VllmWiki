# vllm-project/vllm#31081: [Bug]: v0.12.0 beam search result is incorrect

| 字段 | 值 |
| --- | --- |
| Issue | [#31081](https://github.com/vllm-project/vllm/issues/31081) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v0.12.0 beam search result is incorrect

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug v0.12.0 introduced pr #19347, which optimized beam search performance but also introduced a bug that can cause array out-of-bounds errors or incorrect results. In lines 466, 467, 492, and 493 of `serving_engine.py`, the index is calculated using `idx // logprobs_num`. It assumes that the `engine_client.generate` method will always return the specified `logprobs_num` results, but this assumption is incorrect; it's possible that it will actually return `logprobs_num + 1` results. This causes errors in calculating the beam index using `idx // logprobs_num`, potentially leading to array out-of-bounds errors or incorrect results. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sumes that the `engine_client.generate` method will always return the specified `logprobs_num` results, but this assumption is incorrect; it's possible that it will actually return `logprobs_num + 1` results. This cause...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: v0.12.0 beam search result is incorrect bug;stale ### Your current environment ### 🐛 Describe the bug v0.12.0 introduced pr #19347, which optimized beam search performance but also introduced a bug that can cause...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: v0.12.0 beam search result is incorrect bug;stale ### Your current environment ### 🐛 Describe the bug v0.12.0 introduced pr #19347, which optimized beam search performance but also introduced a bug that can cause...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
