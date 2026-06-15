# vllm-project/vllm#38234: Test Failure: test_run_eagle_dp[FLASH_ATTN] produces non-deterministic outputs with EAGLE speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#38234](https://github.com/vllm-project/vllm/issues/38234) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Test Failure: test_run_eagle_dp[FLASH_ATTN] produces non-deterministic outputs with EAGLE speculative decoding

### Issue 正文摘录

## Summary The distributed EAGLE data parallel test `tests/v1/distributed/test_eagle_dp.py::test_run_eagle_dp[FLASH_ATTN]` is failing because the token outputs generated with EAGLE speculative decoding differ from those generated without it, despite using `temperature=0` for deterministic sampling. ## Test Details - **Test file**: `tests/v1/distributed/test_eagle_dp.py::test_run_eagle_dp[FLASH_ATTN]` - **Date**: 2026-03-25T06:22:37Z - **Model**: `meta-llama/Llama-3.1-8B-Instruct` (target) with `yuhuili/EAGLE-LLaMA3.1-Instruct-8B` (draft) - **Configuration**: `DP_SIZE=2`, `data_parallel_backend="mp"`, `VLLM_BATCH_INVARIANT=1` - **Attention backend**: `FLASH_ATTN` ## Expected Behavior With `temperature=0` and batch invariant mode enabled, both engine configurations (with and without EAGLE) should produce identical token sequences. ## Actual Behavior The generated token sequences completely diverge from the first token: **Without EAGLE**: `[323, 10344, 13, 578, 1296, 374, 311, 1629, 264, 4382, 13790, 31649, 1646, 389, 264, 10550, 315, 220, 1041, 15]` **With EAGLE**: `[198, 2028, 374, 264, 1296, 315, 828, 15638, 449, 60989, 198, 2028, 374, 264, 1296, 315, 828, 15638, 449, 60989]` Firs...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: .py::test_run_eagle_dp[FLASH_ATTN]` - **Date**: 2026-03-25T06:22:37Z - **Model**: `meta-llama/Llama-3.1-8B-Instruct` (target) with `yuhuili/EAGLE-LLaMA3.1-Instruct-8B` (draft) - **Configuration**: `DP_SIZE=2`, `data_par...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: Test Failure: test_run_eagle_dp[FLASH_ATTN] produces non-deterministic outputs with EAGLE speculative decoding ## Summary The distributed EAGLE data parallel test `tests/v1/distributed/test_eagle_dp.py::test_run_eagle_d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: t_run_eagle_dp[FLASH_ATTN] produces non-deterministic outputs with EAGLE speculative decoding ## Summary The distributed EAGLE data parallel test `tests/v1/distributed/test_eagle_dp.py::test_run_eagle_dp[FLASH_ATTN]` is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Test Failure: test_run_eagle_dp[FLASH_ATTN] produces non-deterministic outputs with EAGLE speculative decoding ## Summary The distributed EAGLE data parallel test `tests/v1/distributed/test_eagle_dp.py::test_run_eagle_d
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .1-Instruct-8B` (draft) - **Configuration**: `DP_SIZE=2`, `data_parallel_backend="mp"`, `VLLM_BATCH_INVARIANT=1` - **Attention backend**: `FLASH_ATTN` ## Expected Behavior With `temperature=0` and batch invariant mode e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
