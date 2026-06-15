# vllm-project/vllm#39146: [Bug]: KV block corruption in base scheduler, Non-deterministic output at temperature=0 without prefix caching

| 字段 | 值 |
| --- | --- |
| Issue | [#39146](https://github.com/vllm-project/vllm/issues/39146) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;nondeterministic |
| 根因提示 | env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KV block corruption in base scheduler, Non-deterministic output at temperature=0 without prefix caching

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Related to:** #37076 , PR #37164 ## Summary We fuzzed with prefix-cache but forgot to fuzz without it 😅. But when testing `--speculative-config`, we found a KV block corruption bug that reproduces with **no `--enable-prefix-caching`**. Identical prompts at `temperature=0` produce **_completely_** different output sequences across runs, confirmed **10/10** on three independent traces. The findings were originally discovered while running with `--speculative-config` active, but a controlled isolation test (re-running each trace against a server with speculative decoding removed) confirmed all three reproduce identically without it. The minimum reproduction config is a fully stock vLLM server — no APC, no spec, no LoRA. **This is distinct** from #37076, because that requires `--enable-prefix-caching` and shared prefix content. PR #37164 addresses the TOCTOU race inside `get_computed_blocks()`, while it's not merged, that TOCTOU should not affect the base vllm. SO, these findings point to a separate block lifecycle bug in the base scheduler's non-APC path. ## Background: how this differs from #37076 and PR #37164 **#37076 / PR #371...

## 现有链接修复摘要

#39283 [Bugfix] Zero recycled KV cache blocks for FullAttention models | #43741 [Bugfix][V1] Zero recycled KV cache blocks for FullAttentionSpec to fix non-deterministic output at temperature=0

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: [Bug]: KV block corruption in base scheduler, Non-deterministic output at temperature=0 without prefix caching bug ### Your current environment ### 🐛 Describe the bug **Related to:** #37076 , PR #37164 ## Summary We fuz...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: KV block corruption in base scheduler, Non-deterministic output at temperature=0 without prefix caching bug ### Your current environment ### 🐛 Describe the bug **Related to:** #37076 , PR #37164 ## Summary We fuz...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: he allocation order and thus the "dirty" block distribution shifts, producing different outputs each time. Abd finding_00030's cancel path is the same mechanism but via an few explicit cancellations: `r01`-`r05` are can...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: U race where `cache_full_blocks` inserts newly allocated blocks into the prefix cache hash table before the GPU forward pass completes. The patch pre-pins blocks inside `get_computed_blocks()`. **In my perspective, what...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t outputs each time. Abd finding_00030's cancel path is the same mechanism but via an few explicit cancellations: `r01`-`r05` are cancelled mid-generation, freeing their blocks immediately. The retries arrive 60ms later...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39283](https://github.com/vllm-project/vllm/pull/39283) | closes_keyword | 0.95 | [Bugfix] Zero recycled KV cache blocks for FullAttention models | Closes #39146. The KV block zeroing pipeline from #35219 was gated to Mamba-only models; enabling it for FullAttention prevents stale K/V in partial-block tail slots from propagati |
| [#43741](https://github.com/vllm-project/vllm/pull/43741) | mentioned | 0.6 | [Bugfix][V1] Zero recycled KV cache blocks for FullAttentionSpec to fix non-deterministic output at temperature=0 | dently. ## Test Results **Repro test using fuzzer traces from issue #39146 (vLLM 0.19.0, unpatched — confirms bug exists):** - `finding_00450` — `CONFIRMED` (3/3 expected divergen… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
