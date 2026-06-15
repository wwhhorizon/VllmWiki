# vllm-project/vllm#42186: [Bug][flashinfer 0.6.8]: worker hang on Qwen3.5-397B-A17B-NVFP4 EP=8 (B200 SM100) - bisected to flashinfer-python 0.6.7 → 0.6.8.post1

| 字段 | 值 |
| --- | --- |
| Issue | [#42186](https://github.com/vllm-project/vllm/issues/42186) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic |
| 根因提示 | env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug][flashinfer 0.6.8]: worker hang on Qwen3.5-397B-A17B-NVFP4 EP=8 (B200 SM100) - bisected to flashinfer-python 0.6.7 → 0.6.8.post1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary Running the standard `vllm bench serve` against the `vllm serve` of Qwen3.5-397B-A17B-NVFP4 with data parallelism + expert parallelism on 8× B200 hangs the workers a few hundred requests into the bench. The engine eventually times out on its IPC dequeue and turns into a `EngineDeadError`. Bisect (vLLM-side, between adjacent first-parent commits) isolates the regression to **PR vllm-project/vllm#39959 "Update flashinfer to 0.6.8"**, and *within* that PR to the **`flashinfer-python` 0.6.7 → 0.6.8.post1** version pin in `requirements/cuda.txt`. Pinning flashinfer back to 0.6.7 on the first-bad vLLM commit restores `1024/1024` PASS. _Update._ flashinfer v0.6.11 doesn't fix the bug. ## Environment - vLLM (affected): every commit at or after `191e3fdaa1fd3dd09441e7b22d4f2ddef51c012c` (2026-04-20 17:37 UTC, PR vllm-project/vllm#39959). This includes the `v0.19.1`, `v0.20.0`, and `v0.20.1` releases and current `main`. - vLLM (last known good): `b9cf629bd0e924c69f3d8bfefbfdb77df5ffc7be` (2026-04-20 17:31 UTC) — the immediate predecessor on first-parent. - `flashinfer-python==0.6.8.post1`, `flashinfer-cubin==0.6.8.post1` (the ve...

## 现有链接修复摘要

#39959 Update flashinfer to 0.6.8

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: and *within* that PR to the **`flashinfer-python` 0.6.7 → 0.6.8.post1** version pin in `requirements/cuda.txt`. Pinning flashinfer back to 0.6.7 on the first-bad vLLM commit restores `1024/1024` PASS. _Update._ flashinf...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: ang. I don't see any important difference except driver version. ## Reproducer Server (one shell, all 8 B200s): ```bash vllm serve nvidia/Qwen3.5-397B-A17B-NVFP4 \ --port 8000 \ -tp 1 -pp 1 -dp 8 \ --enable-expert-paral...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: allelism + expert parallelism on 8× B200 hangs the workers a few hundred requests into the bench. The engine eventually times out on its IPC dequeue and turns into a `EngineDeadError`. Bisect (vLLM-side, between adjacen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug][flashinfer 0.6.8]: worker hang on Qwen3.5-397B-A17B-NVFP4 EP=8 (B200 SM100) - bisected to flashinfer-python 0.6.7 → 0.6.8.post1 bug ### Your current environment ### 🐛 Describe the bug ## Summary Running the standar
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug][flashinfer 0.6.8]: worker hang on Qwen3.5-397B-A17B-NVFP4 EP=8 (B200 SM100) - bisected to flashinfer-python 0.6.7 → 0.6.8.post1 bug ### Your current environment ### 🐛 Describe the bug ## Summary Running the standa...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39959](https://github.com/vllm-project/vllm/pull/39959) | mentioned | 0.45 | Update flashinfer to 0.6.8 | ent on `origin/main`'s first-parent line — the regression is uniquely #39959. bug |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
