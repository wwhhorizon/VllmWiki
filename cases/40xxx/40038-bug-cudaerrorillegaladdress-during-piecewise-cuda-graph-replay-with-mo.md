# vllm-project/vllm#40038: [Bug]: cudaErrorIllegalAddress during PIECEWISE CUDA graph replay with MoE LoRA: stale buffer addresses in `moe_lora_align_block_size`

| 字段 | 值 |
| --- | --- |
| Issue | [#40038](https://github.com/vllm-project/vllm/issues/40038) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cudaErrorIllegalAddress during PIECEWISE CUDA graph replay with MoE LoRA: stale buffer addresses in `moe_lora_align_block_size`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Bug Description When serving a model with Mixture-of-Experts (MoE) and a LoRA adapter that targets expert layers, vLLM crashes with `cudaErrorIllegalAddress` during PIECEWISE CUDA graph replay. The crash occurs when base model and LoRA requests are in the same batch. **Affected versions:** v0.18.0, v0.19.0, nightly-55e1a8e1035bddb0b5b63f9ddecc8b4e16fc3ef6 (likely all versions with PIECEWISE CUDA graph support + MoE LoRA) **Affected models:** Any MoE model with expert-targeting LoRA adapters. Confirmed on: - NemotronH with MoE expert LoRA: - nvidia/NVIDIA-Nemotron-3-Super-120B-A12B - nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B - Mixtral with MoE expert LoRA. **Affected Precision models:** BF16, FP8 # Root Cause `PunicaWrapperGPU.moe_lora_align_block_size()` (`vllm/lora/punica_wrapper/punica_gpu.py`) allocates three temporary output buffers with `torch.empty()` on every invocation: ```python sorted_ids = torch.empty((max_loras * max_num_tokens_padded,), dtype=torch.int32, device=topk_ids.device) expert_ids = torch.empty((max_loras * max_num_m_blocks,), dtype=torch.int32, device=topk_ids.device) num_tokens_post_pad = torch.empty((max_lo...

## 现有链接修复摘要

#40044 [Bugfix][LoRA][MoE] Reuse MoE align buffers for CUDA graph replay

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: urs when base model and LoRA requests are in the same batch. **Affected versions:** v0.18.0, v0.19.0, nightly-55e1a8e1035bddb0b5b63f9ddecc8b4e16fc3ef6 (likely all versions with PIECEWISE CUDA graph support + MoE LoRA) *...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: -30B-A3B - Mixtral with MoE expert LoRA. **Affected Precision models:** BF16, FP8 # Root Cause `PunicaWrapperGPU.moe_lora_align_block_size()` (`vllm/lora/punica_wrapper/punica_gpu.py`) allocates three temporary output b...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: cudaErrorIllegalAddress during PIECEWISE CUDA graph replay with MoE LoRA: stale buffer addresses in `moe_lora_align_block_size` bug ### Your current environment ### 🐛 Describe the bug # Bug Description When servi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: udaErrorIllegalAddress during PIECEWISE CUDA graph replay with MoE LoRA: stale buffer addresses in `moe_lora_align_block_size` bug ### Your current environment ### 🐛 Describe the bug # Bug Description When serving a mod...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: IDIA-Nemotron-3-Nano-30B-A3B - Mixtral with MoE expert LoRA. **Affected Precision models:** BF16, FP8 # Root Cause `PunicaWrapperGPU.moe_lora_align_block_size()` (`vllm/lora/punica_wrapper/punica_gpu.py`) allocates thre...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40044](https://github.com/vllm-project/vllm/pull/40044) | closes_keyword | 0.95 | [Bugfix][LoRA][MoE] Reuse MoE align buffers for CUDA graph replay | Fix the issue [Bug]: cudaErrorIllegalAddress during PIECEWISE CUDA graph replay with MoE LoRA: stale buffer addresses in moe_lora_align_block_size [#40038](https://github.com/vllm- |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
