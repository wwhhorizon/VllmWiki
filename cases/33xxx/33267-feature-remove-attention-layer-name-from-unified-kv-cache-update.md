# vllm-project/vllm#33267: [Feature]: Remove attention layer name from `unified_kv_cache_update`

| 字段 | 值 |
| --- | --- |
| Issue | [#33267](https://github.com/vllm-project/vllm/issues/33267) |
| 状态 | open |
| 标签 | help wanted;good first issue;feature request;torch.compile;startup-ux |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Remove attention layer name from `unified_kv_cache_update`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch `unified_kv_cache_update` appears in piecewise cudagraph regions, and each layer has a different name, so each of these have to be compiled separately. This increases cold start compilation time with Dynamo partition because the graphs can no longer be reused. We should use the same approach as #32805 and #33184 to iterate through the layers in the forward context. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: re, motivation and pitch `unified_kv_cache_update` appears in piecewise cudagraph regions, and each layer has a different name, so each of these have to be compiled separately. This increases cold start compilation time...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: fied_kv_cache_update` help wanted;good first issue;feature request;torch.compile;startup-ux ### 🚀 The feature, motivation and pitch `unified_kv_cache_update` appears in piecewise cudagraph regions, and each layer has a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: name from `unified_kv_cache_update` help wanted;good first issue;feature request;torch.compile;startup-ux ### 🚀 The feature, motivation and pitch `unified_kv_cache_update` appears in piecewise cudagraph regions, and eac...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
