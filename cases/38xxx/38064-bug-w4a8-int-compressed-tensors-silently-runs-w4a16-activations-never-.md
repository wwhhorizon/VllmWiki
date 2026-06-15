# vllm-project/vllm#38064: [Bug] W4A8-INT compressed_tensors silently runs W4A16 — activations never quantized to int8

| 字段 | 值 |
| --- | --- |
| Issue | [#38064](https://github.com/vllm-project/vllm/issues/38064) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | kernel;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] W4A8-INT compressed_tensors silently runs W4A16 — activations never quantized to int8

### Issue 正文摘录

## Summary The W4A8-INT quantization path in `compressed_tensors` silently degrades to W4A16 on all GPUs. Activations are never quantized to int8 — the kernel receives bf16 input regardless of the configured quantization scheme. ## Root Cause In `compressed_tensors_w4a8_int.py`, `create_weights` passes `act_type=params_dtype` (which is `torch.bfloat16`) instead of `torch.int8` to `MPLinearLayerConfig`: ```python # Current (broken) mp_linear_kernel_config = MPLinearLayerConfig( ... act_type=params_dtype, # bf16 — wrong! ... ) # Fix mp_linear_kernel_config = MPLinearLayerConfig( ... act_type=torch.int8, # correct ... ) ``` Because `act_type` is `bf16`, the Marlin kernel's `apply_gptq_marlin_linear` never enters the int8 quantization branch: ```python if input_dtype == torch.int8: reshaped_x, a_scales = marlin_quant_input(...) # ← never reached ``` ## Verification Add a dtype print in `apply_gptq_marlin_linear`: ```python print(f"x.dtype={x.dtype}", file=sys.stderr, flush=True) # Outputs: x.dtype=torch.bfloat16 ← should be torch.int8 ``` (Use `VLLM_ENABLE_V1_MULTIPROCESSING=0` to force single-process so the print is visible.) ## Impact All GPUs (A100, L40, A30, etc.). Every W4A8-INT...

## 现有链接修复摘要

#38066 feat(quantization): fix W4A8-INT activation quantization and int4 support in Marlin kernel

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: Bug] W4A8-INT compressed_tensors silently runs W4A16 — activations never quantized to int8 ## Summary The W4A8-INT quantization path in `compressed_tensors` silently degrades to W4A16 on all GPUs. Activations are never...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ver quantized to int8 — the kernel receives bf16 input regardless of the configured quantization scheme. ## Root Cause In `compressed_tensors_w4a8_int.py`, `create_weights` passes `act_type=params_dtype` (which is `torc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ## Fix See: https://github.com/yeshihai/vllm/tree/feat/marlin-w4a8-int Tested on L40 (SM89) with Qwen2.5-7B: - Latency (bs=1, input=512, output=128): **2.72x improvement** over W4A16 - Throughput (16 prompts): **2.14x i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: to force single-process so the print is visible.) ## Impact All GPUs (A100, L40, A30, etc.). Every W4A8-INT model loaded via compressed_tensors actually runs as W4A16, wasting memory bandwidth and defeating the purpose...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n_norm;model_support;quantization kernel;quantization slowdown dtype;env_dependency #38066 feat(quantization): fix W4A8-INT activation quantization and int4 support in Marlin kernel Summary

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38066](https://github.com/vllm-project/vllm/pull/38066) | closes_keyword | 0.95 | feat(quantization): fix W4A8-INT activation quantization and int4 support in Marlin kernel | Fixes #38064 ## Root Causes & Changes ### 1. `compressed_tensors_w4a8_int.py` - `act_type=params_dtype` (bf16) → `act_type=torch.int8` - Add `weight_type=self.quant_type` to `MPL |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
