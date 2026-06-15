# vllm-project/vllm#42516: [Bug]: Gemma4 NVFP4 fails to start with pipeline parallel = 2, or TP = 2 without EP

| 字段 | 值 |
| --- | --- |
| Issue | [#42516](https://github.com/vllm-project/vllm/issues/42516) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma4 NVFP4 fails to start with pipeline parallel = 2, or TP = 2 without EP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary Three distinct fixes for serving Gemma4 with NVFP4 quantization in vLLM 0.20.2: ### 1. Pipeline-parallel crash (PP > 1) When `pipeline-parallel-size > 1`, `Gemma4Model.forward` unconditionally packed `residual` and `per_layer_inputs` into `IntermediateTensors` even when both are `None`. This crashed non-first PP ranks in `sync_and_slice_intermediate_tensors` with `TypeError` (slicing `None`). **Fix**: Only include non-`None` keys in the returned `IntermediateTensors`; use `.get()` on the receive side; guard `sync_and_slice_intermediate_tensors` against `None` entries. ### 2. Missing `.get()` on IntermediateTensors `IntermediateTensors` had no `.get()` method, causing `AttributeError` during `torch.compile` tracing when optional keys were accessed. ### 3. Gated MoE intermediate padding for VLLM_CUTLASS With `tensor-parallel-size: 2` and `moe-backend: cutlass`, the `swizzle_blockscale` function pads the intermediate dimension of the NVFP4 block-scale tensor to the next multiple of 128. When this padded dimension exceeds the packed weight tensor's dimension, padding is needed. The existing code only implemented this paddi...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: onal keys were accessed. ### 3. Gated MoE intermediate padding for VLLM_CUTLASS With `tensor-parallel-size: 2` and `moe-backend: cutlass`, the `swizzle_blockscale` function pads the intermediate dimension of the NVFP4 b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t PP ranks in `sync_and_slice_intermediate_tensors` with `TypeError` (slicing `None`). **Fix**: Only include non-`None` keys in the returned `IntermediateTensors`; use `.get()` on the receive side; guard `sync_and_slice...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Gemma4 NVFP4 fails to start with pipeline parallel = 2, or TP = 2 without EP bug ### Your current environment ### 🐛 Describe the bug ## Summary Three distinct fixes for serving Gemma4 with NVFP4 quantization in v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: mediateTensors.get()` | | `vllm/model_executor/models/gemma4.py` | Only ship non-None tensors in PP; use `.get()` on receive | | `vllm/v1/worker/gpu_model_runner.py` | Guard `sync_and_slice` against None values | | `vll...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: With `tensor-parallel-size: 2` and `moe-backend: cutlass`, the `swizzle_blockscale` function pads the intermediate dimension of the NVFP4 block-scale tensor to the next multiple of 128. When this padded dimension exceed...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
