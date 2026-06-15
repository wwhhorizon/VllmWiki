# vllm-project/vllm#37707: [CI Failure]:  mi325_1: PyTorch Compilation Passes Unit Tests

| 字段 | 值 |
| --- | --- |
| Issue | [#37707](https://github.com/vllm-project/vllm/issues/37707) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;ci_build;distributed_parallel |
| 子分类 |  |
| Operator 关键词 | activation |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_1: PyTorch Compilation Passes Unit Tests

### Issue 正文摘录

### Name of failing test `pytest -s -v tests/compile/passes --ignore tests/compile/passes/distributed` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This is a new test group that we are trying to enable. There are a lot of failures there, most of them related to silu, rmsnorm, and rope. ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/6721/steps/canvas?sid=019d09d4-70ef-4508-b295-ba00a2274a8b&tab=output ### CC List. cc @tjtanaa I know you have been working on fusions, is this TG supposed to be in your TODO list, or we should go ahead and triage it?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_1: PyTorch Compilation Passes Unit Tests ci-failure ### Name of failing test `pytest -s -v tests/compile/passes --ignore tests/compile/passes/distributed` ### Basic information - [ ] Flaky test - [
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: e/passes/distributed` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This is a new test group that we a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s/compile/passes --ignore tests/compile/passes/distributed` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_1: PyTorch Compilation Passes Unit Tests ci-failure ### Name of failing test `pytest -s -v tests/compile/passes --ignore tests/compile/passes/distributed` ### Basic information - [ ] Flaky test - [x]...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
