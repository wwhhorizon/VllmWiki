# vllm-project/vllm#8148: [Feature]: Expert parallel for mixture-of-experts models

| 字段 | 值 |
| --- | --- |
| Issue | [#8148](https://github.com/vllm-project/vllm/issues/8148) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Expert parallel for mixture-of-experts models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Due to the nature of the MoE (Mixture of Experts) structure, combining expert parallelism with tensor parallelism results in reduced communication costs during inference. This effect becomes more pronounced as the number of experts increases. Given the recent trend of releasing open-source models with a large number of experts, it would be beneficial to support inference using the expert parallel + tensor parallel approach. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ure of the MoE (Mixture of Experts) structure, combining expert parallelism with tensor parallelism results in reduced communication costs during inference. This effect becomes more pronounced as the number of experts i...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: Expert parallel for mixture-of-experts models feature request;stale ### 🚀 The feature, motivation and pitch Due to the nature of the MoE (Mixture of Experts) structure, combining expert parallelism with tenso...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Expert parallel for mixture-of-experts models feature request;stale ### 🚀 The feature, motivation and pitch Due to the nature of the MoE (Mixture of Experts) structure, combining expert parallelism with tenso...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ing open-source models with a large number of experts, it would be beneficial to support inference using the expert parallel + tensor parallel approach. ### Alternatives _No response_ ### Additional context _No response...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Expert parallel for mixture-of-experts models feature request;stale ### 🚀 The feature, motivation and pitch Due to the nature of the MoE (Mixture of Experts) structure, combining expert parallelism with tenso...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
