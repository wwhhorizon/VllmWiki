# vllm-project/vllm#40728: [CI Failure]: mi355_1: Kernels MoE Test %N

| 字段 | 值 |
| --- | --- |
| Issue | [#40728](https://github.com/vllm-project/vllm/issues/40728) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;moe |
| 子分类 |  |
| Operator 关键词 | kernel;moe |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [CI Failure]: mi355_1: Kernels MoE Test %N

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_1-kernels-moe-test-n && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && pytest -v -s kernels/moe --ignore=kernels/moe/test_modular_oai_triton_moe.py --shard-id=$BUILDKITE_PARALLEL_JOB --num-shards=$BUILDKITE_PARALLEL_JOB_COUNT && pytest -v -s kernels/moe/test_modular_oai_triton_moe.py --shard-id=$BUILDKITE_PARALLEL_JOB --num-shards=$BUILDKITE_PARALLEL_JOB_COUNT --ignore=kernels/moe/test_moe.py --ignore=kernels/moe/test_cutlass_moe.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/amd-ci/builds/7923/steps/canvas?jid=019db8ed-a5d8-42a7-9b22-404dac86af4d&tab=output ### 📝 History of failing test - Last successful nightly: - - Latest nightly date: 2026-04-23 - Latest build(s): [amd-ci #7923](https://buildkite.com/vllm/amd-ci/builds/7923)

## 现有链接修复摘要

#7923 [Frontend][VLM] Add support for multiple multi-modal items in the OpenAI frontend

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 55_1: Kernels MoE Test %N ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_1-kernels-moe-test-n && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tes...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: /tests && pytest -v -s kernels/moe --ignore=kernels/moe/test_modular_oai_triton_moe.py --shard-id=$BUILDKITE_PARALLEL_JOB --num-shards=$BUILDKITE_PARALLEL_JOB_COUNT && pytest -v -s kernels/moe/test_modular_oai_triton_mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: Kernels MoE Test %N ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_1-kernels-moe-test-n && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vl
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e/test_moe.py --ignore=kernels/moe/test_cutlass_moe.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: /test_cutlass_moe.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/amd-ci/...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7923](https://github.com/vllm-project/vllm/pull/7923) | mentioned | 0.45 | [Frontend][VLM] Add support for multiple multi-modal items in the OpenAI frontend | ghtly: - - latest nightly date: 2026-04-23 - latest build(s): [amd-ci #7923](https://buildkite.com/vllm/amd-ci/builds/7923) ci-failure |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
