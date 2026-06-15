# vllm-project/vllm#24124: Remove CUDA 11.8

| 字段 | 值 |
| --- | --- |
| Issue | [#24124](https://github.com/vllm-project/vllm/issues/24124) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Remove CUDA 11.8

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Now that vLLM is on PyTorch 2.8.0, we are in a good shape to remove all build, test and references against CUDA 11. I believe we need to remove them in `release-pipeline.yaml` and in CI infra. `CMakeLists` and csrc might have guards as well. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Now that vLLM is on PyTorch 2.8.0, we are in a good shape to remove all build, test and references against CUDA 11. I believe we need to remove them in `release-pipeline.yaml` and in CI infra. `CMakeLists` and csrc migh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Remove CUDA 11.8 feature request;stale ### 🚀 The feature, motivation and pitch Now that vLLM is on PyTorch 2.8.0, we are in a good shape to remove all build, test and references against CUDA 11. I believe we need to rem...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Remove CUDA 11.8 feature request;stale ### 🚀 The feature, motivation and pitch Now that vLLM is on PyTorch 2.8.0, we are in a good shape to remove all build, test and references against CUDA 11. I believe we need to rem...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: at vLLM is on PyTorch 2.8.0, we are in a good shape to remove all build, test and references against CUDA 11. I believe we need to remove them in `release-pipeline.yaml` and in CI infra. `CMakeLists` and csrc might have...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
