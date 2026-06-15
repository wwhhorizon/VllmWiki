# vllm-project/vllm#21124: [Feature]: Remove Unused Moe Permute / Un-permute

| 字段 | 值 |
| --- | --- |
| Issue | [#21124](https://github.com/vllm-project/vllm/issues/21124) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Remove Unused Moe Permute / Un-permute

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently in main branch, we don't call the `moe_permute` and `moe_unpermute` operator at all, and even for `_moe_permute/unpermute`, Varun just removed the dependencies in https://github.com/vllm-project/vllm/pull/20903, so I think we can safely remove this kernel and its corresponding benchmark & unit test ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature]: Remove Unused Moe Permute / Un-permute feature request ### 🚀 The feature, motivation and pitch Currently in main branch, we don't call the `moe_permute` and `moe_unpermute` operator at all, and even for `_moe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 20903, so I think we can safely remove this kernel and its corresponding benchmark & unit test ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: l, and even for `_moe_permute/unpermute`, Varun just removed the dependencies in https://github.com/vllm-project/vllm/pull/20903, so I think we can safely remove this kernel and its corresponding benchmark & unit test #...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Remove Unused Moe Permute / Un-permute feature request ### 🚀 The feature, motivation and pitch Currently in main branch, we don't call the `moe_permute` and `moe_unpermute` operator at all, and even for `_moe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
