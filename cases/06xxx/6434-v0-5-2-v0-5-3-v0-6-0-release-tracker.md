# vllm-project/vllm#6434: v0.5.2, v0.5.3, v0.6.0 Release Tracker

| 字段 | 值 |
| --- | --- |
| Issue | [#6434](https://github.com/vllm-project/vllm/issues/6434) |
| 状态 | closed |
| 标签 |  |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> v0.5.2, v0.5.3, v0.6.0 Release Tracker

### Issue 正文摘录

### Anything you want to discuss about vllm. We will make a triplet of releases in the following 3 weeks. - [x] v0.5.2 on Monday July 15th. - [x] v0.5.3 by Tuesday July 23rd. - [ ] v0.6.0 after Monday July 29th. Blockers - [x] #6463 - [x] #6517 - [x] #6698 - [ ] Test vLLM works with 405B that's `num_kv_heads=8` instead of 16. ~The reason for such pace is that we want to remove beam search (#6226), which unlocks a suite of scheduler refactoring to enhance performance (async scheduling to overlap scheduling and forward pass for example). We want to release v0.5.2 ASAP to issue warnings and uncover new signals. Then we will decide the removal in v0.6.0. Normally we will deprecate slowly by stretching it by one month or two. However, (1) RFC has been opened for a while (2) it is unfortunately on the critical path of refactoring and performance enhancements.~ Please also feel free to add release blockers. But do keep in mind that I will not slow the release for v0.5.* series unless critical bug.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: se v0.5.2 ASAP to issue warnings and uncover new signals. Then we will decide the removal in v0.6.0. Normally we will deprecate slowly by stretching it by one month or two. However, (1) RFC has been opened for a while (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tead of 16. ~The reason for such pace is that we want to remove beam search (#6226), which unlocks a suite of scheduler refactoring to enhance performance (async scheduling to overlap scheduling and forward pass for exa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: - [x] v0.5.3 by Tuesday July 23rd. - [ ] v0.6.0 after Monday July 29th. Blockers - [x] #6463 - [x] #6517 - [x] #6698 - [ ] Test vLLM works with 405B that's `num_kv_heads=8` instead of 16. ~The reason for such pace is th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: is that we want to remove beam search (#6226), which unlocks a suite of scheduler refactoring to enhance performance (async scheduling to overlap scheduling and forward pass for example). We want to release v0.5.2 ASAP...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: er Monday July 29th. Blockers - [x] #6463 - [x] #6517 - [x] #6698 - [ ] Test vLLM works with 405B that's `num_kv_heads=8` instead of 16. ~The reason for such pace is that we want to remove beam search (#6226), which unl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
