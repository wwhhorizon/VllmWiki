# vllm-project/vllm#32481: [Bug]: Batch Invariance fails under more diverse workloads

| 字段 | 值 |
| --- | --- |
| Issue | [#32481](https://github.com/vllm-project/vllm/issues/32481) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Batch Invariance fails under more diverse workloads

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When doing testing of batch invariance, results were returned that showed deviations. By scaling an existing test to send a more diverse workload, batch invariance failure could be observed. Then changes are namely: ``` tests/v1/determinism/test_batch_invariance.py - Increased max_num_seqs and max_model_len: - max_num_seqs from 32 → 128. - max_model_len from 8192 → 16384. - Expanded prompt mix to include longer prompts: - Replaced 32 short prompts with a combined set of 128 prompts: 28 short (10–50 words), 50 medium (512–1024 words), and 50 long (2048–4096 words). - Increased sampling workload: - max_tokens from 8 → 128. - logprobs from 5 → 20. tests/v1/determinism/utils.py - Increased padding repetition from target_words // 50 → target_words // 10 to make prompts longer - Changed padding text order to prepended to the base prompt instead of appended (base_prompt = base_prompt + padding_text → base_prompt = padding_text + base_prompt) ``` Draft PR for exact diffs: https://github.com/vllm-project/vllm/pull/32480 Running the updated tests result in: ``` CUDA_VISIBLE_DEVICES=7 VLLM_TEST_SEED=12345 pytest tests/v1/determinism/test_ba...

## 现有链接修复摘要

#32561 Disable Cascade Attention for Batch Invariance

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: [Bug]: Batch Invariance fails under more diverse workloads bug ### Your current environment ### 🐛 Describe the bug When doing testing of batch invariance, results were returned that showed deviations. By scaling an exis...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: lure could be observed. Then changes are namely: ``` tests/v1/determinism/test_batch_invariance.py - Increased max_num_seqs and max_model_len: - max_num_seqs from 32 → 128. - max_model_len from 8192 → 16384. - Expanded...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e_prompt + padding_text → base_prompt = padding_text + base_prompt) ``` Draft PR for exact diffs: https://github.com/vllm-project/vllm/pull/32480 Running the updated tests result in: ``` CUDA_VISIBLE_DEVICES=7 VLLM_TEST...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: bug ### Your current environment ### 🐛 Describe the bug When doing testing of batch invariance, results were returned that showed deviations. By scaling an existing test to send a more diverse workload, batch invariance...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32561](https://github.com/vllm-project/vllm/pull/32561) | closes_keyword | 0.95 | Disable Cascade Attention for Batch Invariance | closes #32481. ## Test Plan Run the updated `test_logprobs_bitwise_batch_invariance_bs1_vs_bsN` before and after the disabling of cascade attention. ## Test Result Before: ``` CU |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
