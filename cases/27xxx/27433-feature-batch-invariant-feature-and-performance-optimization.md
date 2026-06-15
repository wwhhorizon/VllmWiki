# vllm-project/vllm#27433: [Feature]: Batch Invariant Feature and Performance Optimization

| 字段 | 值 |
| --- | --- |
| Issue | [#27433](https://github.com/vllm-project/vllm/issues/27433) |
| 状态 | open |
| 标签 | good first issue;feature request |
| 评论 | 47; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error;nondeterministic |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Batch Invariant Feature and Performance Optimization

### Issue 正文摘录

## 🚀 The feature, motivation and pitch We have basically support Batch Invariant based on https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ https://github.com/orgs/vllm-project/projects/29/views/1 But there are still some work to be done, so here is the issue to track the work ## TODOs: - [x] Basic framework https://github.com/vllm-project/vllm/pull/25603 @bwasti - [x] Flashinfer support https://github.com/vllm-project/vllm/pull/26373 @bwasti - [x] Deepseek-v3 https://github.com/vllm-project/vllm/pull/26609 @bwasti - [x] DeepGEMM on Blackwell https://github.com/vllm-project/vllm/pull/27127 @yewentao256 - [x] Batch Invariant for R1 TP 8 on Blackwell https://github.com/vllm-project/vllm/pull/27229 @yewentao256 - [x] Torch compile & Cuda Graph support https://github.com/vllm-project/vllm/pull/27660 @PaulZhang12 - [x] Usability & Documentation @bwasti https://github.com/vllm-project/vllm/pull/27839 - [x] an RL example @bwasti https://github.com/bwasti/spirl - [x] Adds Batch invariant tests to CI https://github.com/vllm-project/vllm/pull/27842 @yewentao256 - [x] TRITON_MLA support https://github.com/vllm-project/vllm/pull/29125 @yewentao256 - [ ] FLASHINFER_ML...

## 现有链接修复摘要

#30018 [Feature] Batch-Invariant Support for FA2 and LoRA | #33537 [Core] Add determinism warmup automation for batch invariant mode | #33688 [Feature] Enable `TRITON_ATTN` for Batch Invariance | #40034 [Doc] Add Qwen3 AWQ models to documentation | #43317 [CI][Bugfix] Use token-id prefix in batch-invariant decode/prefill consistency test | #43656 [Doc] Add google/gemma-2-2b-it to batch invariance tested models

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ttps://github.com/vllm-project/vllm/pull/27229 @yewentao256 - [x] Torch compile & Cuda Graph support https://github.com/vllm-project/vllm/pull/27660 @PaulZhang12 - [x] Usability & Documentation @bwasti https://github.co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Invariant Feature and Performance Optimization good first issue;feature request ## 🚀 The feature, motivation and pitch We have basically support Batch Invariant based on https://thinkingmachines.ai/blog/defeating-nondet...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: porting;model_support;quantization;speculative_decoding cuda build_error;nondeterministic env_dependency;shape #30018 [Feature] Batch-Invariant Support for FA2 and LoRA | #33537 [Core] Add determinism warmup automation...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [ ] 🙋Help needed ## Nice to have: - [ ] Prefix caching support - [ ] NVFP4 support - [ ] AMD testing/support - [ ] Speculative decoding support (this might be hard) - [ ] vLLM Support for Generic Model Definitions @bwas...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nvariant based on https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ https://github.com/orgs/vllm-project/projects/29/views/1 But there are still some work to be done, so here is the issue to tr...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#30018](https://github.com/vllm-project/vllm/pull/30018) | mentioned | 0.6 | [Feature] Batch-Invariant Support for FA2 and LoRA | ring, concurrent access, and multi-tenant scenarios. This PR follows #27433. ## Test Plan 1. Install FlashAttention-2 with batch-invariant support Use FA2 PR https://github.com/vl… |
| [#33537](https://github.com/vllm-project/vllm/pull/33537) | mentioned | 0.6 | [Core] Add determinism warmup automation for batch invariant mode | into GPU worker's `compile_or_warm_up_model()` method Related issue: #27433 ## Test Plan ```bash # Run unit tests pytest tests/v1/determinism/test_determinism_warmup.py -v # Run w… |
| [#33688](https://github.com/vllm-project/vllm/pull/33688) | mentioned | 0.6 | [Feature] Enable `TRITON_ATTN` for Batch Invariance | `TRITON_ATTN` support for batch invariance. Related / parent issue: #27433 ## Test Plan Run tests with and without the `or is_batch_invariant` check in the triton_unified_attentio… |
| [#40034](https://github.com/vllm-project/vllm/pull/40034) | mentioned | 0.6 | [Doc] Add Qwen3 AWQ models to documentation | atch invariance on. The addition of this to docs was discussed in [#27433](https://github.com/vllm-project/vllm/issues/27433#issuecomment-4198462162). ## Test Plan Ran the follo |
| [#43317](https://github.com/vllm-project/vllm/pull/43317) | mentioned | 0.6 | [CI][Bugfix] Use token-id prefix in batch-invariant decode/prefill consistency test | LLM, no batch-invariant kernels) and runs in a few seconds. Related: #27433. ## Why this is not a duplicate Searched on 2026-05-21 with `gh`: - `gh pr list --repo vllm-project/vll… |
| [#43656](https://github.com/vllm-project/vllm/pull/43656) | closes_keyword | 0.95 | [Doc] Add google/gemma-2-2b-it to batch invariance tested models | Closes part of #27433 (Help needed for validations of more models) --- Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com> Signed-off-by: Yuval Luria <yluria@redhat.com> |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
