# vllm-project/vllm#29521: [CI Failure]: mi325_1: Samplers Test

| 字段 | 值 |
| --- | --- |
| Issue | [#29521](https://github.com/vllm-project/vllm/issues/29521) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | sampling |
| 症状 | build_error;mismatch;nondeterministic |
| 根因提示 | dtype;race_condition |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Samplers Test

### Issue 正文摘录

### Name of failing test `pytest -v -s samplers && VLLM_USE_FLASHINFER_SAMPLER=1 pytest -v -s samplers` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests Summary:** **test_beam_search_with_concurrency_limit** in `test_beam_search.py` - Tests: Beam search output consistency with/without concurrency limits - Failure: Output mismatch between concurrent and sequential beam search - Configuration: TinyLlama-1.1B, beam_width=4, max_tokens=64, dtype=half - Likely cause: Non-deterministic behavior or race conditions in beam search implementation when processing requests concurrently, possibly related to scheduling or state management differences on ROCm. **test_ranks** in `test_logprobs.py` (4 failures) - Tests: Logprobs rank validation for greedy/non-greedy with flat/nested logprobs - Failure: Assertion errors in logprobs structure or rank verification - Configuration: distilgpt2, all combinations of greedy/flat_logprobs flags - Likely cause: Systematic issue with logprobs calculation, extraction, or ranking logic, potentially related to numerical precision in...

## 现有链接修复摘要

#31076 [ROCm][Bugfix] Disable CUDA graphs for distilgpt2 on ROCm | #31077 Fix ROCm CUDA graph replay synchronization bug (issue #29521)

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 8: ytest -v -s samplers` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests Summary:** **test_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: # 🧪 Describe the failing test **Failing Tests Summary:** **test_beam_search_with_concurrency_limit** in `test_beam_search.py` - Tests: Beam search output consistency with/without concurrency limits - Failure: Output mis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ers && VLLM_USE_FLASHINFER_SAMPLER=1 pytest -v -s samplers` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1: Samplers Test ci-failure ### Name of failing test `pytest -v -s samplers && VLLM_USE_FLASHINFER_SAMPLER=1 pytest -v -s samplers` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ehavior or race conditions in beam search implementation when processing requests concurrently, possibly related to scheduling or state management differences on ROCm. **test_ranks** in `test_logprobs.py` (4 failures) -...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31076](https://github.com/vllm-project/vllm/pull/31076) | closes_keyword | 0.95 | [ROCm][Bugfix] Disable CUDA graphs for distilgpt2 on ROCm | Fixes #29521 ([CI Failure]: mi325_1: Samplers Test) - From official vLLM AMD CI project board 🤖 Generated with [Claude Code](https://claude.com/claude-code) Co-Authored-By: Claud |
| [#31077](https://github.com/vllm-project/vllm/pull/31077) | closes_keyword | 0.95 | Fix ROCm CUDA graph replay synchronization bug (issue #29521) | Fixes #29521 - Addresses ROCm-specific CUDA graph failures mentioned in vLLM AMD CI board |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
