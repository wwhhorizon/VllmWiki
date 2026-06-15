# vllm-project/vllm#34893: [Bug]: Qwen3.5-397B-A17B-FP8 fails with TP=4 - fused linear layer sharding incompatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#34893](https://github.com/vllm-project/vllm/issues/34893) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;gemm_linear;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;fp8;kernel;moe;quantization |
| 症状 | crash;mismatch |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-397B-A17B-FP8 fails with TP=4 - fused linear layer sharding incompatibility

### Issue 正文摘录

## Summary Deployment of **Qwen3.5-397B-A17B-FP8** with `--tensor-parallel-size 4` fails consistently during engine initialization in vLLM v0.16.0rc2. Model weights load successfully (96% complete), but crashes when vLLM attempts to shard fused QKV linear layers across 4 TP ranks. **Error:** `RuntimeError: start (0) + length (2048) exceeds dimension size (96).` **Location:** `vllm/model_executor/layers/linear.py:858` in `_load_fused_module_from_checkpoint()` --- ## Environment - **vLLM Version:** 0.16.0rc2.dev269+ga49ea5a58 (nightly 2026-02-18) - **Model:** Qwen/Qwen3.5-397B-A17B-FP8 - **Configuration:** - `--tensor-parallel-size 4` - `--pipeline-parallel-size 1` - `--quantization fp8` - `--enable-expert-parallel` (also tested) - **Hardware:** 4× NVIDIA H200 NVL (140GB VRAM each) - **Cluster:** OpenShift (Linux kernel 6.x) --- ## Reproduction --- ## Root Cause Analysis ### Key Observations 1. All 4 TP workers fail identically at `linear.py:858` during fused layer sharding 2. Weight loading succeeds up to 96% (shard 90/94) — only final shards crash 3. Crash occurs specifically when sharding fused QKV layers with TP=4 4. `--enable-expert-parallel` doesn't help (expert loading works;...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3.5-397B-A17B-FP8 fails with TP=4 - fused linear layer sharding incompatibility ## Summary Deployment of **Qwen3.5-397B-A17B-FP8** with `--tensor-parallel-size 4` fails consistently during engine initializati...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen3.5-397B-A17B-FP8 fails with TP=4 - fused linear layer sharding incompatibility ## Summary Deployment of **Qwen3.5-397B-A17B-FP8** with `--tensor-parallel-size 4` fails consistently during engine initializati...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: - `--pipeline-parallel-size 1` - `--quantization fp8` - `--enable-expert-parallel` (also tested) - **Hardware:** 4× NVIDIA H200 NVL (140GB VRAM each) - **Cluster:** OpenShift (Linux kernel 6.x) --- ## Reproduction --- #...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: in `_load_fused_module_from_checkpoint()` --- ## Environment - **vLLM Version:** 0.16.0rc2.dev269+ga49ea5a58 (nightly 2026-02-18) - **Model:** Qwen/Qwen3.5-397B-A17B-FP8 - **Configuration:** - `--tensor-parallel-size 4`...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ension 96 to a shard of size 2048, which is impossible. This indicates a mismatch between: - Expected shard size (2048) - Actual weight dimension (96) - TP degree (4) For FP8-quantized fused layers in Qwen3.5-397B-A17B,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
