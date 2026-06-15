# vllm-project/vllm#35924: [Bug] Qwen3.5 GatedDeltaNet in_proj_ba fails Marlin MIN_THREAD_N=64 at TP>=4

| 字段 | 值 |
| --- | --- |
| Issue | [#35924](https://github.com/vllm-project/vllm/issues/35924) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;gemm_linear;model_support;moe;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;kernel;moe;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug] Qwen3.5 GatedDeltaNet in_proj_ba fails Marlin MIN_THREAD_N=64 at TP>=4

### Issue 正文摘录

### Summary Qwen3.5's `GatedDeltaNet` linear attention layers use `MergedColumnParallelLinear` for the `in_proj_ba` (B/A state projections). The output dimension is `num_v_heads` (64 for 397B, 48 for 27B). When tensor-parallel splits this across TP ranks, the per-rank output size drops below Marlin's `GPTQ_MARLIN_MIN_THREAD_N = 64` constraint, causing a hard failure. | Model | num_v_heads | TP | Per-rank size | Result | |---|---|---|---|---| | Qwen3.5-397B | 64 | 4 | 16 | **FAIL** (16 < 64) | | Qwen3.5-397B | 64 | 2 | 32 | **FAIL** (32 < 64) | | Qwen3.5-27B | 48 | 1 | 48 | **FAIL** (48 < 64) | | Qwen3.5-27B | 48 | 2 | 24 | **FAIL** (24 < 64) | ### Reproduction ```bash # Using Intel/Qwen3.5-397B-A17B-int4-AutoRound on 4-node DGX Spark, TP=4 vllm serve Intel/Qwen3.5-397B-A17B-int4-AutoRound \ --tensor-parallel-size 4 \ --quantization gptq_marlin \ --max-model-len 4096 ``` The Marlin kernel raises a `ValueError` during weight loading because the column-parallel split produces partitions smaller than 64 elements for the `in_proj_ba` layer in `Qwen3NextGatedDeltaNet`. ### Environment - **vLLM**: 0.16.1rc1 - **Hardware**: 4× NVIDIA GB10 (DGX Spark) with 100G RoCEv2 interconnect - **Mode...

## 现有链接修复摘要

#14138 [Kernel] optimize performance of gptq marlin kernel when n is small | #36199 [Bugfix] Fix Qwen3.5 Marlin TP failure for GDN in_proj_ba | #36329 [Bugfix] Fix Qwen3.5 GatedDeltaNet in_proj_ba Marlin failure at TP>=2 | #37562 [Bugfix] Rebase of #36329: Fix Qwen3.5 GatedDeltaNet in_proj_ba Marlin failure at TP>=2 + torch.compile compatibility | #40361 [Kernel][Bugfix] Marlin W4A16: pad sub-tile output dims on load

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: input_size=hidden_size, output_sizes=[num_v_heads] * 2, bias=False, quant_config=quant_config, prefix=f"{prefix}.in_proj_ba", ) ``` `MergedColumnParallelLinear` divides each output across TP ranks. With `num_v_heads=64`...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: * (24 < 64) | ### Reproduction ```bash # Using Intel/Qwen3.5-397B-A17B-int4-AutoRound on 4-node DGX Spark, TP=4 vllm serve Intel/Qwen3.5-397B-A17B-int4-AutoRound \ --tensor-parallel-size 4 \ --quantization gptq_marlin \...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug] Qwen3.5 GatedDeltaNet in_proj_ba fails Marlin MIN_THREAD_N=64 at TP>=4 ### Summary Qwen3.5's `GatedDeltaNet` linear attention layers use `MergedColumnParallelLinear` for the `in_proj_ba` (B/A state projections). T...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: del_support;moe;quantization attention;kernel;moe;quantization dtype;env_dependency;memory_layout;shape #14138 [Kernel] optimize performance of gptq marlin kernel when n is small | #36199 [Bugfix] Fix Qwen3.5 Marlin TP...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ons are too small for column-parallel splitting (cf. small MLP layers in MoE models). **Init change:** ```python # BEFORE: self.in_proj_ba = MergedColumnParallelLinear( input_size=hidden_size, output_sizes=[num_v_heads]...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#14138](https://github.com/vllm-project/vllm/pull/14138) | mentioned | 0.45 | [Kernel] optimize performance of gptq marlin kernel when n is small | ussion - sglang #19406 — same marlin failure on qwen3.5-27b - vllm pr #14138 — optimizes small-n marlin but doesn't remove the 64-element floor - vllm pr #34604 — rope validation… |
| [#36199](https://github.com/vllm-project/vllm/pull/36199) | closes_keyword | 0.95 | [Bugfix] Fix Qwen3.5 Marlin TP failure for GDN in_proj_ba | Closes #35924 Split the GDN `in_proj_ba` linear into separate `in_proj_b` and `in_proj_a` so each column dimension meets Marlin's MIN_THREAD_N=64 constraint at TP>=4. |
| [#36329](https://github.com/vllm-project/vllm/pull/36329) | closes_keyword | 0.95 | [Bugfix] Fix Qwen3.5 GatedDeltaNet in_proj_ba Marlin failure at TP>=2 | Fixes #35924 — Qwen3.5 `GatedDeltaNet` `in_proj_ba` fails Marlin `MIN_THREAD_N=64` at TP>=2. **Root cause:** `in_proj_ba` uses `MergedColumnParallelLinear` with `output_sizes=[num |
| [#37562](https://github.com/vllm-project/vllm/pull/37562) | closes_keyword | 0.95 | [Bugfix] Rebase of #36329: Fix Qwen3.5 GatedDeltaNet in_proj_ba Marlin failure at TP>=2 + torch.compile compatibility | Fixes #35924 - Original PR: #36329 (needs rebase) - Credit: All original work by @sonusflow --- ## Notes for Reviewers ### Key Changes in This Rebase 1. **Base update:** Rebased |
| [#40361](https://github.com/vllm-project/vllm/pull/40361) | closes_keyword | 0.95 | [Kernel][Bugfix] Marlin W4A16: pad sub-tile output dims on load | Closes #35924 (generically, not Qwen3.5-GDN-specific) Related: #40354 ## Testing - `test_marlin_gemm_sub_tile_n_pad[{32,48,96}]` (new) in `tests/kernels/quantization/test_marli |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
