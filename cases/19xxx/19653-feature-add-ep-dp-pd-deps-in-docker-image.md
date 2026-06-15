# vllm-project/vllm#19653: [Feature]: Add EP/DP/PD deps in docker image

| 字段 | 值 |
| --- | --- |
| Issue | [#19653](https://github.com/vllm-project/vllm/issues/19653) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add EP/DP/PD deps in docker image

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We should be adding DeepEP, pplx-kernels, DeepGEMM, and NIXL to the docker image. You can refer to the tools/ep_kernels for instruction for first two. DeepGEEM repo. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add EP/DP/PD deps in docker image feature request;stale ### 🚀 The feature, motivation and pitch We should be adding DeepEP, pplx-kernels, DeepGEMM, and NIXL to the docker image. You can refer to the tools/ep_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Add EP/DP/PD deps in docker image feature request;stale ### 🚀 The feature, motivation and pitch We should be adding DeepEP, pplx-kernels, DeepGEMM, and NIXL to the docker image. You can refer to the tools/ep_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ure, motivation and pitch We should be adding DeepEP, pplx-kernels, DeepGEMM, and NIXL to the docker image. You can refer to the tools/ep_kernels for instruction for first two. DeepGEEM repo. ### Alternatives _No respon...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
