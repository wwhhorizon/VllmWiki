# vllm-project/vllm#39764: [Bug]: Uninitialized `PerTensorScaleParameter` slots corrupt fused-on-disk quantized models (NVFP4 / compressed-tensors)

| 字段 | 值 |
| --- | --- |
| Issue | [#39764](https://github.com/vllm-project/vllm/issues/39764) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Uninitialized `PerTensorScaleParameter` slots corrupt fused-on-disk quantized models (NVFP4 / compressed-tensors)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary When a quantized checkpoint stores **already-fused** weights (e.g. a single `qkv_proj` instead of separate `q_proj`/`k_proj`/`v_proj`), the per-tensor scale parameters are loaded incorrectly. Only slot 0 of the scale tensor receives the checkpoint value; the remaining slots retain **uninitialized (indeterminate) values** from `torch.empty`. `process_weights_after_loading` then calls `.max()` over all slots, so an indeterminate value that happens to be larger than the true scale silently becomes the effective scale, leading to incorrect dequantization. ## Root cause In `MergedColumnParallelLinear.weight_loader_v2` and `QKVParallelLinear.weight_loader_v2`, when `loaded_shard_id` is `None` (fused-on-disk checkpoint), the code writes the loaded scalar scale into **shard 0 only**, but the parameter retains its full shape `[N]`. The other `N−1` slots are never written. 1. For example, `CompressedTensorsW4A4Fp4` allocate `PerTensorScaleParameter` with `torch.empty(N)`, where N = number of output partitions (3 for QKV, 2 for gate_up). https://github.com/vllm-project/vllm/blob/2a3c32ce674950f94fdd447979e4621267125e41/vllm/model...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [Bug]: Uninitialized `PerTensorScaleParameter` slots corrupt fused-on-disk quantized models (NVFP4 / compressed-tensors) bug ### Your current environment ### 🐛 Describe the bug ## Summary When a quantized checkpoint sto...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: on ### Prerequisites - A GPU with NVFP4 support (e.g. RTX 5090) - vLLM installed from `main` branch - An NVFP4-quantized model with fused weights on disk (e.g. `Phi-3-mini-4k-instruct-NVFP4` from Step 1) ### Step 1: Cre...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: tialized `PerTensorScaleParameter` slots corrupt fused-on-disk quantized models (NVFP4 / compressed-tensors) bug ### Your current environment ### 🐛 Describe the bug ## Summary When a quantized checkpoint stores **alread...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: d. ## Reproduction ### Prerequisites - A GPU with NVFP4 support (e.g. RTX 5090) - vLLM installed from `main` branch - An NVFP4-quantized model with fused weights on disk (e.g. `Phi-3-mini-4k-instruct-NVFP4` from Step 1)...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: Uninitialized `PerTensorScaleParameter` slots corrupt fused-on-disk quantized models (NVFP4 / compressed-tensors) bug ### Your current environment ### 🐛 Describe the bug ## Summary When a quantized checkpoint sto...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
