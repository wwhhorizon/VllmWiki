# vllm-project/vllm#27208: [Feature]: Upgrade CUDA version to 12.9.1 in docker images

| 字段 | 值 |
| --- | --- |
| Issue | [#27208](https://github.com/vllm-project/vllm/issues/27208) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Upgrade CUDA version to 12.9.1 in docker images

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The current builds display warning logs like these ``` Warning: please use at least NVCC 12.9 for the best DeepGEMM performance ``` Can we bump this version easily? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Feature]: Upgrade CUDA version to 12.9.1 in docker images feature request ### 🚀 The feature, motivation and pitch The current builds display warning logs like these ``` Warning: please use at least NVCC 12.9 for the be...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Upgrade CUDA version to 12.9.1 in docker images feature request ### 🚀 The feature, motivation and pitch The current builds display warning logs like these ``` Warning: please use at least NVCC 12.9 for the be...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: s like these ``` Warning: please use at least NVCC 12.9 for the best DeepGEMM performance ``` Can we bump this version easily? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Upgrade CUDA version to 12.9.1 in docker images feature request ### 🚀 The feature, motivation and pitch The current builds display warning logs like these ``` Warning: please use at least NVCC 12.9 for the be...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance ci_build;frontend_api cuda build_error env_dependency 🚀 The feature, moti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
