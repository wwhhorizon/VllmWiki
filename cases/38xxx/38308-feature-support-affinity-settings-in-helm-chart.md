# vllm-project/vllm#38308: [Feature]: support affinity settings in helm chart

| 字段 | 值 |
| --- | --- |
| Issue | [#38308](https://github.com/vllm-project/vllm/issues/38308) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support affinity settings in helm chart

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Problem This issue concerns [chart-helm](https://github.com/vllm-project/vllm/tree/main/examples/online_serving/chart-helm). This Helm Chart does not support configuring `affinity` for Deployment/Pod. Currently, the following use cases are not supported: - The case where users want to specify `podAffinity` - The case where users want to specify `podAntiAffinity` - The case where users want to specify generic `nodeAffinity` (Currently, the specific `nodeAffinity` is created by `gpuModels` in `values.yaml`.) - The case where users do not want to explicitly pin GPU product labels (Currently, it is mandatory to pin this by `gpuModels` in `values.yaml`.) ### Expected behavior The chart should allow users to provide generic `affinity` block via `values.yaml`, mapped directly to Deployment's `spec.template.spec.affinity`. This would make it possible to specify `podAffinity`, `podAntiAffinity`, and `nodeAffinity` that is not limited to the one pinning GPU product labels. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n/examples/online_serving/chart-helm). This Helm Chart does not support configuring `affinity` for Deployment/Pod. Currently, the following use cases are not supported: - The case where users want to specify `podAffinit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: following use cases are not supported: - The case where users want to specify `podAffinity` - The case where users want to specify `podAntiAffinity` - The case where users want to specify generic `nodeAffinity` (Current...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ted behavior The chart should allow users to provide generic `affinity` block via `values.yaml`, mapped directly to Deployment's `spec.template.spec.affinity`. This would make it possible to specify `podAffinity`, `podA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: support affinity settings in helm chart feature request ### 🚀 The feature, motivation and pitch ### Problem This issue concerns [chart-helm](https://github.com/vllm-project/vllm/tree/main/examples/online_serv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
