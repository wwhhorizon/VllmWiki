# vllm-project/vllm#34096: [Tracking Feature]: Support vLLM with Python 3.14

| 字段 | 值 |
| --- | --- |
| Issue | [#34096](https://github.com/vllm-project/vllm/issues/34096) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Tracking Feature]: Support vLLM with Python 3.14

### Issue 正文摘录

### 🚀 The feature, motivation and pitch PyTorch has had official wheels for the past few releases (2.9, 2.10) with Python 3.14 support and we should consider supporting it as well in vLLM. There should be no need to update the vLLM wheel since we already support multiple python versions with one wheel, however we face the issue of needing to resolve vLLM's important dependencies that haven't published compatible 3.14 wheels yet. I tested using a CUDA 13.0 system and updating `pyproject.toml` to have `requires-python = ">=3.10, =2.48.0`: Ray is not required by default anymore, so we can simply make this optional for 3.14 or remove it from required deps eventually, see discussion in https://github.com/vllm-project/vllm/pull/33351 ``` × No solution found when resolving dependencies: ╰─▶ Because only the following versions of ray[cgraph] are available: ray[cgraph] =2.48.0 has no wheels with a matching Python ABI tag (e.g., `cp314`), we can conclude that ray[cgraph]>=2.48.0 cannot be used. And because vllm==0.15.2rc1.dev112+g179ae7da8.d20260208.precompiled depends on ray[cgraph]>=2.48.0, we can conclude that vllm==0.15.2rc1.dev112+g179ae7da8.d20260208.precompiled cannot be used. And be...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ure request ### 🚀 The feature, motivation and pitch PyTorch has had official wheels for the past few releases (2.9, 2.10) with Python 3.14 support and we should consider supporting it as well in vLLM. There should be no...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ies that haven't published compatible 3.14 wheels yet. I tested using a CUDA 13.0 system and updating `pyproject.toml` to have `requires-python = ">=3.10, =2.48.0`: Ray is not required by default anymore, so we can simp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Tracking Feature]: Support vLLM with Python 3.14 feature request ### 🚀 The feature, motivation and pitch PyTorch has had official wheels for the past few releases (2.9, 2.10) with Python 3.14 support and we should cons...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rtant dependencies that haven't published compatible 3.14 wheels yet. I tested using a CUDA 13.0 system and updating `pyproject.toml` to have `requires-python = ">=3.10, =2.48.0`: Ray is not required by default anymore,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
