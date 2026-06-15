# vllm-project/vllm#5426: [Feature]: ci test with vGPU

| 字段 | 值 |
| --- | --- |
| Issue | [#5426](https://github.com/vllm-project/vllm/issues/5426) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: ci test with vGPU

### Issue 正文摘录

### 🚀 The feature, motivation and pitch it seems aws and gcp supports [vGPU](https://docs.nvidia.com/grid/cloud-service-support.html) . we can run some small tests in vGPU, which should be cost-efficient and also test broader software support to avoid https://github.com/vllm-project/vllm/issues/4587 . ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: ci test with vGPU feature request;stale ### 🚀 The feature, motivation and pitch it seems aws and gcp supports [vGPU](https://docs.nvidia.com/grid/cloud-service-support.html) . we can run some small tests in v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: ci test with vGPU feature request;stale ### 🚀 The feature, motivation and pitch it seems aws and gcp supports [vGPU](https://docs.nvidia.com/grid/cloud-service-support.html) . we can run some small tests in v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tps://docs.nvidia.com/grid/cloud-service-support.html) . we can run some small tests in vGPU, which should be cost-efficient and also test broader software support to avoid https://github.com/vllm-project/vllm/issues/45...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: ci test with vGPU feature request;stale ### 🚀 The feature, motivation and pitch it seems aws and gcp supports [vGPU](https://docs.nvidia.com/grid/cloud-service-support.html) . we can run some small tests in v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
