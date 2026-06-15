# vllm-project/vllm#6994: [RFC]: More rigorous compilation warnings

| 字段 | 值 |
| --- | --- |
| Issue | [#6994](https://github.com/vllm-project/vllm/issues/6994) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: More rigorous compilation warnings

### Issue 正文摘录

### Motivation. For this RFC, I want to tighten down vLLM's compiler flags regarding warnings. Both to eliminate warnings when compiling code, and also to increase the number of warnings to prevent certain classes of bugs that have proven to be problematic in vLLM. **Why eliminate warnings?** Seeing a lot of warning spam is annoying. Bogus or unimportant warnings can also mask real problems. It also just looks bad -- until #6904, one of the first things developers saw when building vLLM from source was a ton of spam about possible divide-by-zeros. These things are usually easy to fix and just need a small forcing function to make it happen. **Why add more warnings?** I think we can eliminate or drastically reduce certain classes of bugs. For example, `-Wconvert` will hopefully prevent bugs like those fixed in #6838, #6649, and #1514 by making our narrowing conversions explicit. ### Proposed Change. **Turn on `-Werror`** This is necessary in order to enforce a clean build. **Turn on `-Wconversion`** Eliminate narrowing conversion bugs especially from `int64_t` to `int32_t`. Currently way too spammy to turn on, especially in the attention kernels. ### Feedback Period. _No response_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: s RFC;stale ### Motivation. For this RFC, I want to tighten down vLLM's compiler flags regarding warnings. Both to eliminate warnings when compiling code, and also to increase the number of warnings to prevent certain c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: le divide-by-zeros. These things are usually easy to fix and just need a small forcing function to make it happen. **Why add more warnings?** I think we can eliminate or drastically reduce certain classes of bugs. For e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: More rigorous compilation warnings RFC;stale ### Motivation. For this RFC, I want to tighten down vLLM's compiler flags regarding warnings. Both to eliminate warnings when compiling code, and also to increase the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
