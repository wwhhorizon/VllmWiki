# vllm-project/vllm#4770: [Feature]: CI: Test on NVLink-enabled machine

| 字段 | 值 |
| --- | --- |
| Issue | [#4770](https://github.com/vllm-project/vllm/issues/4770) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: CI: Test on NVLink-enabled machine

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The custom allreduce code https://github.com/vllm-project/vllm/blob/main/vllm/distributed/device_communicators/custom_all_reduce.py works with NVLink only. To run the corresponding distributed tests https://github.com/vllm-project/vllm/blob/main/tests/distributed/test_custom_all_reduce.py , we need at least 2 NVLink-enabled GPUs. (Ideally we need 4 to test for all cases). cc @simon-mo ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: CI: Test on NVLink-enabled machine feature request ### 🚀 The feature, motivation and pitch The custom allreduce code https://github.com/vllm-project/vllm/blob/main/vllm/distributed/device_communicators/custom...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: CI: Test on NVLink-enabled machine feature request ### 🚀 The feature, motivation and pitch The custom allreduce code https://github.com/vllm-project/vllm/blob/main/vllm/distributed/device_communicators/custom...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: CI: Test on NVLink-enabled machine feature request ### 🚀 The feature, motivation and pitch The custom allreduce code https://github.com/vllm-project/vllm/blob/main/vllm/distributed/device_communicators/custom...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
