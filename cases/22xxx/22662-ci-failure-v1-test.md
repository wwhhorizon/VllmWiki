# vllm-project/vllm#22662: [CI Failure]: V1 Test

| 字段 | 值 |
| --- | --- |
| Issue | [#22662](https://github.com/vllm-project/vllm/issues/22662) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [CI Failure]: V1 Test

### Issue 正文摘录

### Name of failing test v1/spec_decode/test_max_len.py::test_eagle_max_len[TREE_ATTN-3] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test > RuntimeError: CUDA error: an illegal memory access was encountered ### 📝 History of failing test Failing since #21496 https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/54aa326d-c77c-8e84-8830-f9de1705b80a?period=14days&execution_id=019887e7-f764-79cb-b985-f8f6897849aa ### CC List. cc @tjtanaa

## 现有链接修复摘要

#21496 [ROCm] [V1] [SpecDec] Enable Speculative Decoding on ROCm V1 Engine

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: V1 Test ci-failure ### Name of failing test v1/spec_decode/test_max_len.py::test_eagle_max_len[TREE_ATTN-3] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libr
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: bug in `transformers`) ### 🧪 Describe the failing test > RuntimeError: CUDA error: an illegal memory access was encountered ### 📝 History of failing test Failing since #21496 https://buildkite.com/organizations/vllm/ana...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [CI Failure]: V1 Test ci-failure ### Name of failing test v1/spec_decode/test_max_len.py::test_eagle_max_len[TREE_ATTN-3] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libra...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _max_len[TREE_ATTN-3] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test > RuntimeError: CUDA error: an ill...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: pec_decode/test_max_len.py::test_eagle_max_len[TREE_ATTN-3] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21496](https://github.com/vllm-project/vllm/pull/21496) | mentioned | 0.45 | [ROCm] [V1] [SpecDec] Enable Speculative Decoding on ROCm V1 Engine | access was encountered ### 📝 history of failing test failing since #21496 https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/54aa326d-c77c-8e84-8830-f9de1705b80a… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
