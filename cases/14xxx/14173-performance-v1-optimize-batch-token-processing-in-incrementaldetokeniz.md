# vllm-project/vllm#14173: [Performance] [V1]: Optimize batch token processing in `IncrementalDetokenizer.update()`

| 字段 | 值 |
| --- | --- |
| Issue | [#14173](https://github.com/vllm-project/vllm/issues/14173) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance] [V1]: Optimize batch token processing in `IncrementalDetokenizer.update()`

### Issue 正文摘录

### Proposal to improve performance https://github.com/vincent-4/vllm/blob/b9f1d4294e30b700dcb25390c74831a5c178f5fd/vllm/v1/engine/detokenizer.py#L96-L97 The current implementation of `IncrementalDetokenizer.update()` processes tokens one by one in a loop, which becomes inefficient when handling multiple tokens at once. As noted in the TODO comment linked above: ``` # TODO(woosuk): This method becomes very inefficient when the number of # new_token_ids is more than 1. We need to optimize this. ``` The method currently processes each token individually, running ```detokenize_incrementally()``` in a loop for each new token ID. This creates unnecessary overhead when processing batches of tokens. ### Report of performance regression _No response_ ### Misc discussion on performance I have no issues working on this, I have a pending fix ready to be uploaded if I can get a 'sanity'-OK from owners. ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: zer.update()` processes tokens one by one in a loop, which becomes inefficient when handling multiple tokens at once. As noted in the TODO comment linked above: ``` # TODO(woosuk): This method becomes very inefficient w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: y overhead when processing batches of tokens. ### Report of performance regression _No response_ ### Misc discussion on performance I have no issues working on this, I have a pending fix ready to be uploaded if I can ge...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: batch token processing in `IncrementalDetokenizer.update()` performance;stale ### Proposal to improve performance https://github.com/vincent-4/vllm/blob/b9f1d4294e30b700dcb25390c74831a5c178f5fd/vllm/v1/engine/detokenize...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
