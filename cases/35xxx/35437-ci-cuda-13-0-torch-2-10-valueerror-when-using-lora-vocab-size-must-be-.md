# vllm-project/vllm#35437: [ci][cuda 13.0, torch 2.10] ValueError: When using LoRA, vocab size must be > 32000 and <= 258048

| 字段 | 值 |
| --- | --- |
| Issue | [#35437](https://github.com/vllm-project/vllm/issues/35437) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [ci][cuda 13.0, torch 2.10] ValueError: When using LoRA, vocab size must be > 32000 and <= 258048

### Issue 正文摘录

### Name of failing test `tests/lora/test_mixtral.py::test_mixtral_lora[4]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This failure occurs on the PR bumping vllm to cuda 13.0: https://github.com/vllm-project/vllm/pull/35315 CI: https://buildkite.com/vllm/ci/builds/53407/steps/canvas?jid=019c9ace-451d-454d-891c-834330d0e8cf ### 📝 History of failing test occurs on the PR bumping vllm to cuda 13.0: https://github.com/vllm-project/vllm/pull/35315 ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [ci][cuda 13.0, torch 2.10] ValueError: When using LoRA, vocab size must be > 32000 and <= 258048 ci-failure ### Name of failing test `tests/lora/test_mixtral.py::test_mixtral_lora[4]` ### Basic information - [ ] Flaky
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: test_mixtral_lora[4]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This failure occurs on the PR bump...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [ci][cuda 13.0, torch 2.10] ValueError: When using LoRA, vocab size must be > 32000 and <= 258048 ci-failure ### Name of failing test `tests/lora/test_mixtral.py::test_mixtral_lora[4]` ### Basic information - [ ] Flaky...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ng test `tests/lora/test_mixtral.py::test_mixtral_lora[4]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: vocab size must be > 32000 and <= 258048 ci-failure ### Name of failing test `tests/lora/test_mixtral.py::test_mixtral_lora[4]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
