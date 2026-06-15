# vllm-project/vllm#41319: [CI Failure]:  mi355_2: NixlConnector PD + Spec Decode acceptance (2 GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#41319](https://github.com/vllm-project/vllm/issues/41319) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cache |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_2: NixlConnector PD + Spec Decode acceptance (2 GPUs)

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_2-nixlconnector-pd---spec-decode-acceptance-2-gpus && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && uv pip install --system -r /vllm-workspace/requirements/kv_connectors_rocm.txt && ROCM_ATTN=1 bash v1/kv_connector/nixl_integration/spec_decode_acceptance_test.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `AssertionError: All kv cache tensors must have the same number of blocks` ### 📝 History of failing test - Current streak start: 2026-04-28 - First failure in 60d window: 2026-04-21 - Last successful nightly: 2026-04-27 - Break frequency (60d, pass↔fail flips): 3 - Latest nightly date: 2026-04-29 - Latest build(s): [amd-ci #8058](https://buildkite.com/vllm/amd-ci/builds/8058) - Latest hardware status: `mi250_2`=fail

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi355_2: NixlConnector PD + Spec Decode acceptance (2 GPUs) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_2-nixlconnector-pd---spec-decode-acceptance-
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ecode acceptance (2 GPUs) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_2-nixlconnector-pd---spec-decode-acceptance-2-gpus && export VLLM_ALLOW_DEPRECATED_BEAM_SEAR...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [CI Failure]: mi355_2: NixlConnector PD + Spec Decode acceptance (2 GPUs) ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_2-nixlconnector-pd---spec-decode-acceptance-...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: e_acceptance_test.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `AssertionError: All kv cache tens...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: n `transformers`) ### 🧪 Describe the failing test `AssertionError: All kv cache tensors must have the same number of blocks` ### 📝 History of failing test - Current streak start: 2026-04-28 - First failure in 60d window...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
