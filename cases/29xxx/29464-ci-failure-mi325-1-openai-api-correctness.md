# vllm-project/vllm#29464: [CI Failure]: mi325_1: OpenAI API correctness

| 字段 | 值 |
| --- | --- |
| Issue | [#29464](https://github.com/vllm-project/vllm/issues/29464) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;sampling |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: OpenAI API correctness

### Issue 正文摘录

### Name of failing test `pytest -s entrypoints/openai/correctness/` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **1 audio transcription correctness test** - Word Error Rate (WER) accuracy validation #### Failed Test: `test_wer_correctness[12.74498-D4nt3/esb-datasets-earnings22-validation-tiny-filtered-openai/whisper-large-v3]` **Failure:** Assertion failure in WER accuracy comparison - `torch.testing.assert_close(wer, expected_wer, atol=1e-1, rtol=1e-2)` **Configuration:** - Model: `openai/whisper-large-v3` (audio transcription) - Dataset: D4nt3/esb-datasets-earnings22-validation-tiny-filtered - Expected WER: 12.744980 - Tolerance: atol=0.1, rtol=0.02 (absolute: ±0.1%, relative: ±2%) - Test duration: ~140 seconds - `test_lm_eval_accuracy_v1_engine` passed (1/2 tests passed) **Likely cause:** ROCm numerical divergence in audio processing pipeline causing Word Error Rate to exceed tolerance. The Whisper model's audio feature extraction and inference produce slightly different transcriptions on ROCm compared to the CUDA baseline, resulting in a WER that falls outsid...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 6: /openai/correctness/` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **1 audio transcription correctnes...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: f failing test `pytest -s entrypoints/openai/correctness/` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_1: OpenAI API correctness ci-failure ### Name of failing test `pytest -s entrypoints/openai/correctness/` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: lm_eval_accuracy_v1_engine` passed (1/2 tests passed) **Likely cause:** ROCm numerical divergence in audio processing pipeline causing Word Error Rate to exceed tolerance. The Whisper model's audio feature extraction an...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Failure]: mi325_1: OpenAI API correctness ci-failure ### Name of failing test `pytest -s entrypoints/openai/correctness/` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
