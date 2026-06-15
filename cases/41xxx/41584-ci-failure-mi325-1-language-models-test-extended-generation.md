# vllm-project/vllm#41584: [CI Failure]:  mi325_1: Language Models Test (Extended Generation)

| 字段 | 值 |
| --- | --- |
| Issue | [#41584](https://github.com/vllm-project/vllm/issues/41584) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_1: Language Models Test (Extended Generation)

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi325_1-language-models-test-extended-generation && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && uv pip install --system --no-build-isolation 'git+https://github.com/AndreasKaratzas/mamba@fix-rocm-7.0-warp-size-constexpr' && uv pip install --system --no-build-isolation 'git+https://github.com/Dao-AILab/causal-conv1d@v1.6.0' && pytest -v -s models/language/generation -m '(not core_model) and (not hybrid_model)'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED models/language/generation/test_common.py::test_models[True-False-5-32-naver-hyperclovax/HyperCLOVAX-SEED-Think-14B] FAILED models/language/generation/test_common.py::test_models[False-False-5-32-naver-hyperclovax/HyperCLOVAX-SEED-Think-14B] ``` ### 📝 History of failing test - Current streak start: 2026-04-16 - First failure in 60d window: 2026-04-09 - Last successful nightly: 2026-04-15 - Break frequency (60d, pass↔fail flips): 3 - Latest nightly date: 2026-05-03 - Latest build(s): [amd-ci #...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_1: Language Models Test (Extended Generation) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi325_1-language-models-test-extended-generation && export
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: est (Extended Generation) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi325_1-language-models-test-extended-generation && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 &&...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: mi325_1: Language Models Test (Extended Generation) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi325_1-language-models-test-extended-generation && export...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: (not hybrid_model)'` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED models/language/generati...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ``` FAILED models/language/generation/test_common.py::test_models[True-False-5-32-naver-hyperclovax/HyperCLOVAX-SEED-Think-14B] FAILED models/language/generation/test_common.py::test_models[False-False-5-32-naver-hyperc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
