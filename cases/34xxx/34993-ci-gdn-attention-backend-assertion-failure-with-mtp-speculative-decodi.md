# vllm-project/vllm#34993: [CI] GDN attention backend assertion failure with MTP speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#34993](https://github.com/vllm-project/vllm/issues/34993) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI] GDN attention backend assertion failure with MTP speculative decoding

### Issue 正文摘录

## Name of failing test - `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** LM Eval Small Models (B200) **Category:** test ## Describe the failing test The GDN attention backend asserts that num_decodes and num_spec_decodes cannot both be greater than 0 simultaneously, but MTP speculative decoding scheduler schedules both regular decode tokens and speculative decode tokens in the same step, violating this constraint. ``` AssertionError: num_decodes: 1, num_spec_decodes: 45 ``` ## Relevant builds - [Build #52432](https://buildkite.com/vllm/ci/builds/52432) (8de7c636) - [LM Eval Small Models (B200)](https://buildkite.com/vllm/ci/builds/52432#019c79da-6537-422c-aa51-bfe75e752e28) ## History of failing test - **First seen:** Build #52432 (8de7c636) - **Last pass:** Build #52333 (4fb8beef) - **Commits between last pass and first seen:** 17 --- *Filed from [CI Triage Dashboard](http://localhost:8001/known-failures/49)*

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: g test - `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [CI] GDN attention backend assertion failure with MTP speculative decoding ci-failure ## Name of failing test - `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2]` ## Basic info...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI] GDN attention backend assertion failure with MTP speculative decoding ci-failure ## Name of failing test - `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2]` ## Basic info
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: m8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** LM Eval Small...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: h MTP speculative decoding ci-failure ## Name of failing test - `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2]` ## Basic information - [ ] Flaky test - [ ] Can reproduce loc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
