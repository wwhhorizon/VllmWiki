# vllm-project/vllm#39589: [Bug]: KV Cache Read/Write Index Corruption Under Concurrent Prefill of Variable-Length Sequences (vLLM V1, FlashInfer)

| 字段 | 值 |
| --- | --- |
| Issue | [#39589](https://github.com/vllm-project/vllm/issues/39589) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;nondeterministic |
| 根因提示 | env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: KV Cache Read/Write Index Corruption Under Concurrent Prefill of Variable-Length Sequences (vLLM V1, FlashInfer)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary After locally adopt patches from pr #37076 /pr #37152 and #39146/pr #39283, a new issue showed up, two or more concurrent requests with **different prompt lengths** produce non-deterministic output at `temperature=0`, even with Batch-invariant enabled. The same requests sent sequentially always produce identical output, indicating the model is attending to incorrect KV cache data. ## Minimal Reproducer Script: [repro_minimal.py](https://gist.github.com/Yunzez/c01fd7a87b72a74f3cc1ff825b2c3112#file-repro_minimal-py) Run: `python3 repro_minimal.py --base-url http://localhost:8000 --runs 50` **Trigger:** 2 concurrent `/v1/completions` requests at `temperature=0` with different `prompt_len`. ``` Request A: prompt_len=128, max_tokens=32, temperature=0 Request B: prompt_len=256, max_tokens=32, temperature=0 (sent simultaneously) ``` **Divergence rate:** ~8% of runs (4/50). ## More Controlled Experiment Results All tests: 50 runs, `temperature=0`, same prompts every run. | Test | Variants | Divergence Rate | Verdict | |---|---|---|---| | 2 concurrent, different size (128, 256) | 2 | 4/50 (8%) | **BUG** | | 2 sequential, differ...

## 现有链接修复摘要

#39283 [Bugfix] Zero recycled KV cache blocks for FullAttention models | #39591 [Bugfix] Zero block_table row tail to fix concurrent variable-length prefill non-determinism (#39589)

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 7: wo or more concurrent requests with **different prompt lengths** produce non-deterministic output at `temperature=0`, even with Batch-invariant enabled. The same requests sent sequentially always produce identical outpu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Divergence persists at 11.5% (23/200 runs), ruling out floating-point precision as the root cause. - The logprob gap at the first diverging token is ~0.125 (top-5 tokens are within 0.25 range), which is within floating-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: prefix caching on): also reproduces ### Not floating-point non-determinism - Divergence starts at token 0, not at a single boundary token - Up to 7 distinct output variants in 20 runs (floating-point would give 2) - Seq...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ) also diverges. The trigger appears related to sequence length crossing block/chunk boundaries, not strictly requiring different prompt lengths. With more concurrent requests, divergence increases dramatically: | Test...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: KV Cache Read/Write Index Corruption Under Concurrent Prefill of Variable-Length Sequences (vLLM V1, FlashInfer) bug ### Your current environment ### 🐛 Describe the bug ## Summary After locally adopt patches from...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39283](https://github.com/vllm-project/vllm/pull/39283) | mentioned | 0.45 | [Bugfix] Zero recycled KV cache blocks for FullAttention models | after locally adopt patches from pr #37076 /pr #37152 and #39146/pr #39283, a new issue showed up, two or more concurrent requests with **different prompt lengths** produce non-de… |
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | closes_keyword | 0.95 | [Bugfix] Zero block_table row tail to fix concurrent variable-length prefill non-determinism (#39589) | Closes #39589 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
