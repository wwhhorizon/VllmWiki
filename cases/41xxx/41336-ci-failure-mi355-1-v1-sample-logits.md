# vllm-project/vllm#41336: [CI Failure]:  mi355_1: V1 Sample + Logits

| 字段 | 值 |
| --- | --- |
| Issue | [#41336](https://github.com/vllm-project/vllm/issues/41336) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_1: V1 Sample + Logits

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_1-v1-sample---logits && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && pytest -v -s v1/sample && pytest -v -s v1/logits_processors && pytest -v -s v1/test_oracle.py && pytest -v -s v1/test_request.py && pytest -v -s v1/test_outputs.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED v1/sample/test_logprobs.py::test_spec_decode_logprobs[ngram-raw_logprobs] FAILED v1/sample/test_logprobs.py::test_spec_decode_logprobs[ngram-processed_logprobs] ``` ### 📝 History of failing test - Break frequency (60d, pass↔fail flips): 0 - Latest nightly date: 2026-04-29 - Latest build(s): [amd-ci #8058](https://buildkite.com/vllm/amd-ci/builds/8058) - Latest hardware status: `mi355_1`=fail

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 355_1: V1 Sample + Logits ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_1-v1-sample---logits && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tes...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: V1 Sample + Logits ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_1-v1-sample---logits && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vl
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: its_processors && pytest -v -s v1/test_oracle.py && pytest -v -s v1/test_request.py && pytest -v -s v1/test_outputs.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external librari...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s v1/test_outputs.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED v1/sample/test_logprobs...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: v -s v1/test_request.py && pytest -v -s v1/test_outputs.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
