# vllm-project/vllm#23344: [Feature][Wide EP]: Add NIXL, DeepEP, DeepGEMM, and PPLX to Docker Image

| 字段 | 值 |
| --- | --- |
| Issue | [#23344](https://github.com/vllm-project/vllm/issues/23344) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Wide EP]: Add NIXL, DeepEP, DeepGEMM, and PPLX to Docker Image

### Issue 正文摘录

### 🚀 The feature, motivation and pitch - vLLM has added support for DeepEP, DeepGEMM, and PPLX but this is not shipped in the docker image and users have to install it manually - Update the docker image to include these packages ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature][Wide EP]: Add NIXL, DeepEP, DeepGEMM, and PPLX to Docker Image feature request;stale ### 🚀 The feature, motivation and pitch - vLLM has added support for DeepEP, DeepGEMM, and PPLX but this is not shipped in t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: - vLLM has added support for DeepEP, DeepGEMM, and PPLX but this is not shipped in the docker image and users have to install it manually - Update the docker image to include these packages ### Alternatives _No response...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ][Wide EP]: Add NIXL, DeepEP, DeepGEMM, and PPLX to Docker Image feature request;stale ### 🚀 The feature, motivation and pitch - vLLM has added support for DeepEP, DeepGEMM, and PPLX but this is not shipped in the docke...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature][Wide EP]: Add NIXL, DeepEP, DeepGEMM, and PPLX to Docker Image feature request;stale ### 🚀 The feature, motivation and pitch - vLLM has added support for DeepEP, DeepGEMM, and PPLX but this is not shipped in t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
