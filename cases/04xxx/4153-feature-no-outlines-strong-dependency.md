# vllm-project/vllm#4153: [Feature]: No `outlines` strong dependency

| 字段 | 值 |
| --- | --- |
| Issue | [#4153](https://github.com/vllm-project/vllm/issues/4153) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: No `outlines` strong dependency

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://github.com/vllm-project/vllm/blob/main/requirements-common.txt Here vllm has `outlines == 0.0.34` But starting from [v0.0.38](https://github.com/outlines-dev/outlines/releases/tag/0.0.38) outlines has VLLM integration https://github.com/outlines-dev/outlines/pull/772 But I can't update to latest vllm to use it, as it rises versioning error This error can be ignored But can somehow this be resolved? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: No `outlines` strong dependency feature request;stale ### 🚀 The feature, motivation and pitch https://github.com/vllm-project/vllm/blob/main/requirements-common.txt Here vllm has `outlines == 0.0.34` But star...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: No `outlines` strong dependency feature request;stale ### 🚀 The feature, motivation and pitch https://github.com/vllm-project/vllm/blob/main/requirements-common.txt Here vllm has `outlines == 0.0.34` But star...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tps://github.com/outlines-dev/outlines/pull/772 But I can't update to latest vllm to use it, as it rises versioning error This error can be ignored But can somehow this be resolved? ### Alternatives _No response_ ### Ad...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
