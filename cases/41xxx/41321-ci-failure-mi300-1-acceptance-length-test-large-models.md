# vllm-project/vllm#41321: [CI Failure]:  mi300_1: Acceptance Length Test (Large Models)

| 字段 | 值 |
| --- | --- |
| Issue | [#41321](https://github.com/vllm-project/vllm/issues/41321) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;moe |
| 子分类 |  |
| Operator 关键词 | moe |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi300_1: Acceptance Length Test (Large Models)

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-acceptance-length-test-large-models && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && export VLLM_ALLOW_INSECURE_SERIALIZATION=1 && pytest -v -s v1/spec_decode/test_acceptance_length.py -m slow_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED v1/spec_decode/test_acceptance_length.py::test_eagle3_acceptance_length[ROCM_ATTN-tp1-3-qwen3-30b-moe-vl-eagle3] FAILED v1/spec_decode/test_acceptance_length.py::test_eagle3_acceptance_length[ROCM_AITER_UNIFIED_ATTN-tp1-3-qwen3-30b-moe-vl-eagle3] FAILED v1/spec_decode/test_acceptance_length.py::test_eagle3_acceptance_length[TRITON_ATTN-tp1-3-qwen3-30b-moe-vl-eagle3] ``` ### 📝 History of failing test - Current streak start: 2026-04-25 - First failure in 60d window: 2026-04-25 - Last successful nightly: 2026-04-24 - Break frequency (60d, pass↔fail flips): 1 - Latest nightly date: 2026-04-29 - Latest build(s): [amd-ci #8058](https://buildkite.com/vllm/amd-ci/builds/8058) - Latest hardware status: `mi...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [CI Failure]: mi300_1: Acceptance Length Test (Large Models) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-acceptance-length-test-large-models && export VLLM_ALLO...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: mi300_1: Acceptance Length Test (Large Models) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-acceptance-length-test-large-models && export VLLM_ALLO...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: pec_decode/test_acceptance_length.py::test_eagle3_acceptance_length[ROCM_AITER_UNIFIED_ATTN-tp1-3-qwen3-30b-moe-vl-eagle3] FAILED v1/spec_decode/test_acceptance_length.py::test_eagle3_acceptance_length[TRITON_ATTN-tp1-3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi300_1: Acceptance Length Test (Large Models) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-acceptance-length-test-large-models && export VLLM_ALLO
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ngth.py -m slow_test` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED v1/spec_decode/test_acc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
