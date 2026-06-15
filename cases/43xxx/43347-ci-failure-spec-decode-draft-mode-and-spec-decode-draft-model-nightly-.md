# vllm-project/vllm#43347: [CI Failure]: Spec Decode Draft Mode and Spec Decode Draft Model Nightly B200 failing with low match ratio

| 字段 | 值 |
| --- | --- |
| Issue | [#43347](https://github.com/vllm-project/vllm/issues/43347) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Spec Decode Draft Mode and Spec Decode Draft Model Nightly B200 failing with low match ratio

### Issue 正文摘录

### Name of failing test v1/e2e/spec_decode/test_spec_decode.py::test_draft_model_correctness ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `v1/e2e/spec_decode/test_spec_decode.py::test_draft_model_correctness` failing with ratio 75 and 76 respectively (should be >= 90) ### 📝 History of failing test This is a new failure ### CC List. _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [CI Failure]: Spec Decode Draft Mode and Spec Decode Draft Model Nightly B200 failing with low match ratio ci-failure ### Name of failing test v1/e2e/spec_decode/test_spec_decode.py::test_draft_model_correctness ### Bas...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: Spec Decode Draft Mode and Spec Decode Draft Model Nightly B200 failing with low match ratio ci-failure ### Name of failing test v1/e2e/spec_decode/test_spec_decode.py::test_draft_model_correctness ### Bas...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: aft_model_correctness ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `v1/e2e/spec_decode/test_spec_deco...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: Spec Decode Draft Mode and Spec Decode Draft Model Nightly B200 failing with low match ratio ci-failure ### Name of failing test v1/e2e/spec_decode/test_spec_decode.py::test_draft_model_correctness ### Bas
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: Spec Decode Draft Mode and Spec Decode Draft Model Nightly B200 failing with low match ratio ci-failure ### Name of failing test v1/e2e/spec_decode/test_spec_decode.py::test_draft_model_correctness ### Bas...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
