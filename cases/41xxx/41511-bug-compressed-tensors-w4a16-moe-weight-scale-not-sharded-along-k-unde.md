# vllm-project/vllm#41511: [Bug]: compressed-tensors W4A16 MoE: weight_scale not sharded along K under tensor parallelism, kernel computes wrong group_size

| 字段 | 值 |
| --- | --- |
| Issue | [#41511](https://github.com/vllm-project/vllm/issues/41511) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization |
| 子分类 | shape_align |
| Operator 关键词 | attention;cuda;fp8;gemm;kernel;moe;operator;quantization |
| 症状 | crash;mismatch;oom |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: compressed-tensors W4A16 MoE: weight_scale not sharded along K under tensor parallelism, kernel computes wrong group_size

### Issue 正文摘录

### Your current environment - vLLM commit: `0ac3de079` = jasl/ds4-sm120 base `428e08e` + neuralmagic/kylesayrs/deepseek-ct (PR #41276) `f910a73a` cherry-picked + a `packed_modules_mapping` class-attr patch on `DeepseekV4ForCausalLM` (which the PR references at line 205 but doesn't define on the class) - The 4 commits between live tree base and current jasl/ds4-sm120 HEAD `68901da` (`06e11f8`, `2148a6e`, `2e06cbd`, `68901da`) do not modify `vllm/model_executor/layers/quantization/compressed_tensors/`. Verified empty: `git log 06e11f8..68901da -- vllm/model_executor/layers/quantization/compressed_tensors/`. Behavior on `68901da` is the same by construction for the affected code path - PyTorch: 2.11.0+cu130 - CUDA: 13.0 - GPU: 8× NVIDIA H200 (SM 9.0), 141 GB HBM3e each - Model: pastapaul/DeepSeek-V4-Flash-W4A16-FP8 (FP8_BLOCK attention + W4A16 GPTQ routed experts, group_size=128, produced via [llm-compressor PR #2647](https://github.com/vllm-project/llm-compressor/pull/2647) branch `kylesayrs/transformers-v5`, attention quant mirrors RedHatAI/DeepSeek-V4-Flash-NVFP4-FP8 topology) ### 🐛 Describe the bug When serving a compressed-tensors W4A16 MoE model under tensor parallelism, the M...

## 现有链接修复摘要

#38222 [Bugfix] Add dimension alignment check to Marlin MoE kernel selection | #40991 [DSv4][Nvidia] SM12x DeepSeek V4 support | #41276 [WIP] [DSV4] Quantization Support

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: compressed-tensors W4A16 MoE: weight_scale not sharded along K under tensor parallelism, kernel computes wrong group_size ### Your current environment - vLLM commit: `0ac3de079` = jasl/ds4-sm120 base `428e08e` +...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: tartup: ``` INFO compressed_tensors_moe_wna16_marlin.py:87] Using Marlin backend for WNA16 MoE (group_size=128, num_bits=4) ``` …but at kernel-dispatch time the GEMM call sees `group_size = 16`. That's a 1×8 mismatch un...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: kernel-dispatch time the GEMM call sees `group_size = 16`. That's a 1×8 mismatch under TP=8, exactly the K-shard ratio. ### Empirical observations across TP sizes | TP | K_per_rank | num_groups (from on-disk scale) | ke...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Default`, yielding the cryptic `thread_k=-1` error. ### Reproduction Recipe (mirrors RedHatAI/DeepSeek-V4-Flash-NVFP4-FP8 attention group + W4A16 GPTQ on routed experts): ```python from llmcompressor.modifiers.quantizat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ensors W4A16 MoE: weight_scale not sharded along K under tensor parallelism, kernel computes wrong group_size ### Your current environment - vLLM commit: `0ac3de079` = jasl/ds4-sm120 base `428e08e` + neuralmagic/kylesay...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38222](https://github.com/vllm-project/vllm/pull/38222) | mentioned | 0.45 | [Bugfix] Add dimension alignment check to Marlin MoE kernel selection | aller-than-necessary tiles). ### related issues / prs - #38022 / pr #38222: separate marlin moe shape-alignment bug for non-128-aligned hidden dims (different root cause; same sym… |
| [#40991](https://github.com/vllm-project/vllm/pull/40991) | mentioned | 0.45 | [DSv4][Nvidia] SM12x DeepSeek V4 support | mt` and linear-wrap fixes; does not touch moe tp scale sharding. - pr #40991 (jasl sm12x v4): adds sm12x kernel fallbacks; does not touch compressed-tensors moe quantization paths… |
| [#41276](https://github.com/vllm-project/vllm/pull/41276) | mentioned | 0.45 | [WIP] [DSV4] Quantization Support | issues - [x] verified bug fires on `0ac3de079` = jasl `428e08e` + pr #41276 cherry-pick (python content equivalent to current `68901da` head for the affected code path; intervenin… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
