# vllm-project/vllm#26017: [Feature]: CI workflow for building non-CUDA Aarch64 wheels

| 字段 | 值 |
| --- | --- |
| Issue | [#26017](https://github.com/vllm-project/vllm/issues/26017) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: CI workflow for building non-CUDA Aarch64 wheels

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We're currently working on a PR for adding a workflow for building a CUDA independent Aarch64 wheel. Based on [this comment](https://github.com/pytorch/pytorch-integration-testing/pull/44#issuecomment-3331154820) on a pytorch-integration-testing PR it seems there is infrastructure to support wheels for a CPU only build. There _should_ be a `linux.arm64.m7g.metal` runner ready to use. This runner may also be used for building Aarch64 wheels. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature]: CI workflow for building non-CUDA Aarch64 wheels feature request ### 🚀 The feature, motivation and pitch We're currently working on a PR for adding a workflow for building a CUDA independent Aarch64 wheel. Ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: CI workflow for building non-CUDA Aarch64 wheels feature request ### 🚀 The feature, motivation and pitch We're currently working on a PR for adding a workflow for building a CUDA independent Aarch64 wheel. Ba...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: CI workflow for building non-CUDA Aarch64 wheels feature request ### 🚀 The feature, motivation and pitch We're currently working on a PR for adding a workflow for building a CUDA independent Aarch64 wheel. Ba...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: . Based on [this comment](https://github.com/pytorch/pytorch-integration-testing/pull/44#issuecomment-3331154820) on a pytorch-integration-testing PR it seems there is infrastructure to support wheels for a CPU only bui...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
