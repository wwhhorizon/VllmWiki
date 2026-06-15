# vllm-project/vllm#31216: [RFC]: Sampling Optimization: move gather of logits after argmax.

| 字段 | 值 |
| --- | --- |
| Issue | [#31216](https://github.com/vllm-project/vllm/issues/31216) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Sampling Optimization: move gather of logits after argmax.

### Issue 正文摘录

### Motivation. As shown in the left part of the following picture, in the original sampling procedure we perform `llm_head` and `gather` first, then perform `argmax` to full `logits`. However, we can in fact move `gather` after `argmax` to reduce both the communication volume of `gather` and the computation load of `argmax`. The test results during the puncturing phase show that this feature can optimize the `logits_processor + sampler` time consumption by more than 200 us in certain scenarios. In speculative decoding scenarios, where multiple rounds of post-processing are required for each step, the benefits of this feature can become even more pronounced. So I think this is an important optimization especially when eagle3 become more and more popular. Later I will propose a PR to implement this. ### Proposed Change. Implementing PR: https://github.com/vllm-project/vllm/pull/32021 1. Remove the `gather/all_gather` operation from logits processor. 2. Add two `gather/all_gather` operations to sampler to gather both max value and max index of `argmax`. Then perform `max` to obtain the global max value and related max index. ### Results. Original argmax: ![Image](https://github.com/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s of this feature can become even more pronounced. So I think this is an important optimization especially when eagle3 become more and more popular. Later I will propose a PR to implement this. ### Proposed Change. Impl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Sampling Optimization: move gather of logits after argmax. RFC;stale ### Motivation. As shown in the left part of the following picture, in the original sampling procedure we perform `llm_head` and `gather` first...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ication volume of `gather` and the computation load of `argmax`. The test results during the puncturing phase show that this feature can optimize the `logits_processor + sampler` time consumption by more than 200 us in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
