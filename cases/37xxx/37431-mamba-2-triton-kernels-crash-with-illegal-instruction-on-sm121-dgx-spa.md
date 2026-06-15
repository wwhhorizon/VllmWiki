# vllm-project/vllm#37431: Mamba-2 Triton kernels crash with illegal instruction on SM121 (DGX Spark) without CUDA_LAUNCH_BLOCKING=1

| 字段 | 值 |
| --- | --- |
| Issue | [#37431](https://github.com/vllm-project/vllm/issues/37431) |
| 状态 | open |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | activation;attention;cuda;fp8;kernel;moe;operator;quantization;triton |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Mamba-2 Triton kernels crash with illegal instruction on SM121 (DGX Spark) without CUDA_LAUNCH_BLOCKING=1

### Issue 正文摘录

## Bug: Mamba-2 Triton ops produce `cudaErrorIllegalInstruction` in async mode on SM121 ### Environment - **GPU:** NVIDIA GB10 (SM121) — DGX Spark - **Driver:** 580.126.09 - **CUDA:** 13.0 (forward compat 13.1) - **vLLM:** 0.17.2rc1.dev7+g9c7cab5eb (eugr/spark-vllm-docker prebuilt wheels, March 17 2026) - **PyTorch:** 2.10.0a0+a36e1d3 (NGC 26.01) - **Triton:** 3.6.0 - **Model:** `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` (NemotronHForCausalLM, hybrid Mamba-2 + Transformer + MoE) - **Platform:** aarch64 (Grace CPU) ### Description NemotronH models that use Mamba-2 layers crash with `CUDA error: an illegal instruction was encountered` during inference on SM121 GPUs. The crash originates in vLLM's **Triton-based** Mamba ops (not the `causal-conv1d` / `mamba-ssm` packages, which are not used by vLLM). Setting `CUDA_LAUNCH_BLOCKING=1` makes the model fully stable but **degrades throughput from ~14 tok/s (expected) to ~8.8 tok/s** (~37% penalty) and limits GPU utilization to ~60%. ### Crash location The error surfaces at `mamba_mixer2.py:127` in `forward_native`: ``` x_grouped = x_grouped * torch.rsqrt(variance + self.variance_epsilon) ``` But with `CUDA_LAUNCH_BLOCKING=1` we conf...

## 现有链接修复摘要

#35947 fix: Software E2M1 conversion for SM12x NVFP4 activation quantization

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ward compat 13.1) - **vLLM:** 0.17.2rc1.dev7+g9c7cab5eb (eugr/spark-vllm-docker prebuilt wheels, March 17 2026) - **PyTorch:** 2.10.0a0+a36e1d3 (NGC 26.01) - **Triton:** 3.6.0 - **Model:** `nvidia/NVIDIA-Nemotron-3-Supe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: **Triton:** 3.6.0 - **Model:** `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` (NemotronHForCausalLM, hybrid Mamba-2 + Transformer + MoE) - **Platform:** aarch64 (Grace CPU) ### Description NemotronH models that use Ma...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: Mamba-2 Triton kernels crash with illegal instruction on SM121 (DGX Spark) without CUDA_LAUNCH_BLOCKING=1 ## Bug: Mamba-2 Triton ops produce `cudaErrorIllegalInstruction` in async mode on SM121 ### Environment - **GPU:*...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Mamba-2 Triton kernels crash with illegal instruction on SM121 (DGX Spark) without CUDA_LAUNCH_BLOCKING=1 ## Bug: Mamba-2 Triton ops produce `cudaErrorIllegalInstruction` in async mode on SM121 ### Environment - **GPU:*...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 026) - **PyTorch:** 2.10.0a0+a36e1d3 (NGC 26.01) - **Triton:** 3.6.0 - **Model:** `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` (NemotronHForCausalLM, hybrid Mamba-2 + Transformer + MoE) - **Platform:** aarch64 (Grac...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35947](https://github.com/vllm-project/vllm/pull/35947) | mentioned | 0.45 | fix: Software E2M1 conversion for SM12x NVFP4 activation quantization | on aarch64 - #35519 — nvfp4 illegal instruction on sm121 (fixed by pr #35947 for e2m1, but mamba ops remain broken) - #31128 — add support of blackwell sm121 - #37030 — marlin ker… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
