# vllm-project/vllm#37849: [RFC]: Unify the function of getting device count

| 字段 | 值 |
| --- | --- |
| Issue | [#37849](https://github.com/vllm-project/vllm/issues/37849) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Unify the function of getting device count

### Issue 正文摘录

### Motivation. now, we have three kinds of functions for getting device count as below, - cuda_device_count_stateless - current_platform.device_count - torch.accelerator.device_count() Sometimes it will make user to be confused to choose. we had better using one to unify. And for the first one, it is only for cuda, in some current usage in test/, it will block other accelerators like xpu. https://github.com/vllm-project/vllm/pull/37841 as an example, it will make the decorator multi_gpu_test can not work on xpu. ### Proposed Change. To choose current_platform.device_count or torch.accelerator.device_count(), I suggest torch.accelerator.device_count() as it is suggested by torch community, but current_platform.device_count is also ok to me. We can do below step by step. 1. to replace the cuda_device_count_stateless() with current_platform.device_count or torch.accelerator.device_count() 2. unify the usage of getting device count to current_platform.device_count or torch.accelerator.device_count() ### Feedback Period. _No response_ ### CC List. @youkaichao @simon-mo @WoosukKwon @zhuohan123 @jikunshang ### Any Other Things. maybe related: https://github.com/vllm-project/vllm/issues/...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: w, we have three kinds of functions for getting device count as below, - cuda_device_count_stateless - current_platform.device_count - torch.accelerator.device_count() Sometimes it will make user to be confused to choos...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: first one, it is only for cuda, in some current usage in test/, it will block other accelerators like xpu. https://github.com/vllm-project/vllm/pull/37841 as an example, it will make the decorator multi_gpu_test can not...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: y. And for the first one, it is only for cuda, in some current usage in test/, it will block other accelerators like xpu. https://github.com/vllm-project/vllm/pull/37841 as an example, it will make the decorator multi_g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
