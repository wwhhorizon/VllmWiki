# vllm-project/vllm#35922: [Bug]: Marlin MoE kernels crash on A100 (SM80) with compressed-tensors quantized Qwen3-30B-A3B

| 字段 | 值 |
| --- | --- |
| Issue | [#35922](https://github.com/vllm-project/vllm/issues/35922) |
| 状态 | open |
| 标签 | stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;moe;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Marlin MoE kernels crash on A100 (SM80) with compressed-tensors quantized Qwen3-30B-A3B

### Issue 正文摘录

### Your current environment ``` vLLM Version: 0.16.0 (vllm/vllm-openai:v0.16.0 Docker image) GPU: NVIDIA A100 80GB PCIe (SM80, Ampere) Model: Qwen/Qwen3-30B-A3B (MoE, 30B params, 3B active) Quantization: compressed-tensors via llm-compressor 0.9.0.2 ``` ### Describe the bug All compressed-tensors quantized Qwen3-30B-A3B checkpoints crash during `profile_run()` on A100 (SM80) with CUDA errors in the Marlin MoE kernel path. Both INT4 (W4A16) and FP4 (NVFP4A16, MXFP4A16, NVFP4) modes fail, but with different errors: **W4A16 INT4** — `cudaErrorIllegalAddress` (illegal memory access) in `fused_marlin_moe`: ``` compressed_tensors_moe.py:1715, in apply return fused_marlin_moe( fused_marlin_moe.py:363, in fused_marlin_moe return torch.sum(moe_output.view(-1, topk, K), dim=1, out=output) torch.AcceleratorError: CUDA error: an illegal memory access was encountered ``` **NVFP4A16 / MXFP4A16 / NVFP4 (W4A4)** — `cudaErrorNoKernelImageForDevice` in FP4 Marlin MoE: ``` compressed_tensors_moe.py:354, in apply (NVFP4A16) compressed_tensors_moe.py:665, in apply (NVFP4 W4A4) return self.moe_mk( modular_kernel.py:1333, in forward output = torch.zeros_like(hidden_states) torch.AcceleratorError: CUDA...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [Bug]: Marlin MoE kernels crash on A100 (SM80) with compressed-tensors quantized Qwen3-30B-A3B stale ### Your current environment ``` vLLM Version: 0.16.0 (vllm/vllm-openai:v0.16.0 Docker image) GPU: NVIDIA A100 80GB PC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: [Bug]: Marlin MoE kernels crash on A100 (SM80) with compressed-tensors quantized Qwen3-30B-A3B stale ### Your current environment ``` vLLM Version: 0.16.0 (vllm/vllm-openai:v0.16.0 Docker image) GPU: NVIDIA A100 80GB PC...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ors quantized Qwen3-30B-A3B stale ### Your current environment ``` vLLM Version: 0.16.0 (vllm/vllm-openai:v0.16.0 Docker image) GPU: NVIDIA A100 80GB PCIe (SM80, Ampere) Model: Qwen/Qwen3-30B-A3B (MoE, 30B params, 3B ac...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: arlin MoE kernels crash on A100 (SM80) with compressed-tensors quantized Qwen3-30B-A3B stale ### Your current environment ``` vLLM Version: 0.16.0 (vllm/vllm-openai:v0.16.0 Docker image) GPU: NVIDIA A100 80GB PCIe (SM80...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Marlin MoE kernels crash on A100 (SM80) with compressed-tensors quantized Qwen3-30B-A3B stale ### Your current environment ``` vLLM Version: 0.16.0 (vllm/vllm-openai:v0.16.0 Docker image) GPU: NVIDIA A100 80GB PC...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
