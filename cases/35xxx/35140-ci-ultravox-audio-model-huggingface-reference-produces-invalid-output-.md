# vllm-project/vllm#35140: [CI] Ultravox audio model HuggingFace reference produces invalid output with NaN logprobs

| 字段 | 值 |
| --- | --- |
| Issue | [#35140](https://github.com/vllm-project/vllm/issues/35140) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI] Ultravox audio model HuggingFace reference produces invalid output with NaN logprobs

### Issue 正文摘录

## Name of failing test - `models/multimodal/generation/test_common.py::test_audio_models[ultravox-test_case0]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Multi-Modal Models (Standard) **Category:** test ## Describe the failing test The test_audio_models test for ultravox fails because the HuggingFace reference implementation produces garbage output (all exclamation marks) with NaN logprobs, while vLLM produces correct audio transcription. The HuggingFace model has uninitialized weights (lm_head.weight not loaded from checkpoint), causing invalid inference results. ``` AssertionError: HuggingFace reference model produces invalid output with NaN logprobs and garbage tokens (exclamation marks) due to uninitialized lm_head.weight, while vLLM produces correct audio transcription. Assertion fails when comparing vLLM token against HF reference logprobs. AssertionError: HuggingFace reference output contains all exclamation marks with NaN logprobs {1: nan, 0: nan, 2: nan, 4: nan, 3: nan} while vLLM produces correct audio transcription. HuggingFace model has uninitialized weights - 'Some weights of LlamaForCausalL...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [CI] Ultravox audio model HuggingFace reference produces invalid output with NaN logprobs ci-failure ## Name of failing test - `models/multimodal/generation/test_common.py::test_audio_models[ultravox-test_case0]` ## Bas...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI] Ultravox audio model HuggingFace reference produces invalid output with NaN logprobs ci-failure ## Name of failing test - `models/multimodal/generation/test_common.py::test_audio_models[ultravox-test_case0]` ## Bas
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [ultravox-test_case0]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Multi-Modal Models (Standard) **Category:** test ## Describe the failing tes...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: produces invalid output with NaN logprobs ci-failure ## Name of failing test - `models/multimodal/generation/test_common.py::test_audio_models[ultravox-test_case0]` ## Basic information - [ ] Flaky test - [ ] Can reprod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
