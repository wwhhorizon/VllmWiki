# vllm-project/vllm#1346: [v0.2.1] Release Tracker

| 字段 | 值 |
| --- | --- |
| Issue | [#1346](https://github.com/vllm-project/vllm/issues/1346) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [v0.2.1] Release Tracker

### Issue 正文摘录

**ETA**: ~~Oct. 15th (Sun)~~ Oct 16th (Mon). ## Major changes TBD ## PRs to be merged before the release - [x] PagedAttention V2 #1348 - [x] Support `echo` #1328 #959 - [x] Fix `TORCH_CUDA_ARCH_LIST` err msg #1239 - ~~Support YaRN #1264 #1161~~ (Deferred) - ~~Add `repetition_penalty` sampling parameter #866~~ (Deferred)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: gedAttention V2 #1348 - [x] Support `echo` #1328 #959 - [x] Fix `TORCH_CUDA_ARCH_LIST` err msg #1239 - ~~Support YaRN #1264 #1161~~ (Deferred) - ~~Add `repetition_penalty` sampling parameter #866~~ (Deferred)

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
