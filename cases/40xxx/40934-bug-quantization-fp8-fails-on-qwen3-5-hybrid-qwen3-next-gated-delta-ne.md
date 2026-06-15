# vllm-project/vllm#40934: [Bug]: --quantization fp8 fails on Qwen3.5 hybrid (qwen3_next gated delta net) with cutlass_scaled_mm Error Internal on GB10 sm_121

| 字段 | 值 |
| --- | --- |
| Issue | [#40934](https://github.com/vllm-project/vllm/issues/40934) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;gemm_linear;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --quantization fp8 fails on Qwen3.5 hybrid (qwen3_next gated delta net) with cutlass_scaled_mm Error Internal on GB10 sm_121

### Issue 正文摘录

## Summary Loading a Qwen3.5 hybrid (Qwen3_5ForConditionalGeneration / qwen3_next) model with `--quantization fp8` fails during `profile_run` with `RuntimeError: Error Internal` from `torch.ops._C.cutlass_scaled_mm`. The same model loads and serves cleanly at `--dtype bfloat16` without `--quantization`. The crash reproduces on a fine-tuned 9B variant of this architecture; I haven't been able to test the public weights yet because of model size. The failure originates in `vllm/_custom_ops.py:845`, `cutlass_scaled_mm` — a generic "Error Internal" assert from the cutlass kernel itself, with no further detail. The traceback site differs depending on whether the model has populated vision weights, but the failing op is the same in both cases. ## Environment - vLLM: 0.18.0 - Hardware: NVIDIA GB10 (DGX Spark), compute capability 12.1 (sm_121) - PyTorch: 2.10.0+cu130, CUDA 13.0 - transformers: 5.5.4 - compressed-tensors: 0.13.0 - OS: Ubuntu 24.04 (aarch64) - Driver / runtime: cu130 with `LD_LIBRARY_PATH=/path/to/cuda12-compat` for legacy soname symlinks (this is the documented setup pattern for GB10 + cu130 right now) ## Repro ``` vllm serve /path/to/Qwen3.5-9B-fine-tuned \ --host 0.0.0.0...

## 现有链接修复摘要

#41021 [Quantization] Per-shard FP8 scaling for MergedColumnParallelLinear

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: --quantization fp8 fails on Qwen3.5 hybrid (qwen3_next gated delta net) with cutlass_scaled_mm Error Internal on GB10 sm_121 ## Summary Loading a Qwen3.5 hybrid (Qwen3_5ForConditionalGeneration / qwen3_next) mode...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: --quantization fp8 fails on Qwen3.5 hybrid (qwen3_next gated delta net) with cutlass_scaled_mm Error Internal on GB10 sm_121 ## Summary Loading a Qwen3.5 hybrid (Qwen3_5ForConditionalGeneration / qwen3_next) mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: wen3_next gated delta net) with cutlass_scaled_mm Error Internal on GB10 sm_121 ## Summary Loading a Qwen3.5 hybrid (Qwen3_5ForConditionalGeneration / qwen3_next) model with `--quantization fp8` fails during `profile_ru...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: antization fp8 fails on Qwen3.5 hybrid (qwen3_next gated delta net) with cutlass_scaled_mm Error Internal on GB10 sm_121 ## Summary Loading a Qwen3.5 hybrid (Qwen3_5ForConditionalGeneration / qwen3_next) model with `--q...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: cu130 with `LD_LIBRARY_PATH=/path/to/cuda12-compat` for legacy soname symlinks (this is the documented setup pattern for GB10 + cu130 right now) ## Repro ``` vllm serve /path/to/Qwen3.5-9B-fine-tuned \ --host 0.0.0.0 --...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41021](https://github.com/vllm-project/vllm/pull/41021) | closes_keyword | 0.95 | [Quantization] Per-shard FP8 scaling for MergedColumnParallelLinear | Fixes #40934. ## Fix Quantize each logical shard independently in `process_weights_after_loading`, then expand to per-channel via `convert_to_channelwise`. The result is a `[N, 1 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
