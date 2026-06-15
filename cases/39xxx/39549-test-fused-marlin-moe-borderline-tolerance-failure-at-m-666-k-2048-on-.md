# vllm-project/vllm#39549: test_fused_marlin_moe borderline tolerance failure at m=666, K=2048 on L4

| 字段 | 值 |
| --- | --- |
| Issue | [#39549](https://github.com/vllm-project/vllm/issues/39549) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;quantization |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> test_fused_marlin_moe borderline tolerance failure at m=666, K=2048 on L4

### Issue 正文摘录

`test_fused_marlin_moe` fails on L4 (SM89) at m=666, K=2048 with max absolute error 0.04297 vs `atol=4e-2`. Failures are 1-4 elements out of 1.4M (0.0003%). **Investigation:** - FP32 accumulation is used on SM80+ (`use_fp16_accum = false`) — not an accumulation precision issue - Partial block handling is correct: predicated loads skip padding rows, output writes are guarded by `row < block_num_valid_tokens` - The `default_vllm_config` fixture does not change Marlin kernel dispatch — `moe_wna16_marlin_gemm` is a direct C++ call with no config-dependent paths - The error is inherent 4-bit weight quantization noise accumulated over K=2048 at the test's fixed seed (`torch.cuda.manual_seed(1)`) - m=1 and m=123 pass at the same K=2048. Only m=666 (chosen as a non-aligned stress test) is borderline - The error varies by L4 instance — PR #39024 passed all MOE tests on a different L4 `test_fused_marlin_moe_with_bias` already uses `@pytest.mark.flaky(reruns=2)` for similar borderline behavior. The base test should probably match, since the 0.003 margin over tolerance is within hardware variance range. Observed during CI for #35568. Only surfaces when MOE tests are triggered by csrc/ changes.

## 现有链接修复摘要

#35568 [Bugfix] Fix SM121 (DGX Spark) exclusion from Marlin/CUTLASS FP8 paths

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ion is used on SM80+ (`use_fp16_accum = false`) — not an accumulation precision issue - Partial block handling is correct: predicated loads skip padding rows, output writes are guarded by `row < block_num_valid_tokens`...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: vestigation:** - FP32 accumulation is used on SM80+ (`use_fp16_accum = false`) — not an accumulation precision issue - Partial block handling is correct: predicated loads skip padding rows, output writes are guarded by...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: okens` - The `default_vllm_config` fixture does not change Marlin kernel dispatch — `moe_wna16_marlin_gemm` is a direct C++ call with no config-dependent paths - The error is inherent 4-bit weight quantization noise acc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: call with no config-dependent paths - The error is inherent 4-bit weight quantization noise accumulated over K=2048 at the test's fixed seed (`torch.cuda.manual_seed(1)`) - m=1 and m=123 pass at the same K=2048. Only m=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ance failure at m=666, K=2048 on L4 `test_fused_marlin_moe` fails on L4 (SM89) at m=666, K=2048 with max absolute error 0.04297 vs `atol=4e-2`. Failures are 1-4 elements out of 1.4M (0.0003%). **Investigation:** - FP32...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35568](https://github.com/vllm-project/vllm/pull/35568) | mentioned | 0.45 | [Bugfix] Fix SM121 (DGX Spark) exclusion from Marlin/CUTLASS FP8 paths | tolerance is within hardware variance range. observed during ci for #35568. only surfaces when moe tests are triggered by csrc/ changes. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
