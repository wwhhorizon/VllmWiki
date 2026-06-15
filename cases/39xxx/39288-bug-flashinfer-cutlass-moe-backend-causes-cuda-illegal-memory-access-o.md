# vllm-project/vllm#39288: [Bug]: FlashInfer CUTLASS MoE backend causes CUDA illegal memory access on H100 during CUDA graph capture (Qwen3-Next-80B BF16)

| 字段 | 值 |
| --- | --- |
| Issue | [#39288](https://github.com/vllm-project/vllm/issues/39288) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;triton |
| 症状 | crash;nan_inf;nondeterministic;slowdown |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: FlashInfer CUTLASS MoE backend causes CUDA illegal memory access on H100 during CUDA graph capture (Qwen3-Next-80B BF16)

### Issue 正文摘录

### Your current environment - **GPU**: NVIDIA H100 80GB HBM3 (8x per node, NVLink connected) - **Platform**: DGX H100 (Eos cluster) - **vLLM version**: v0.18.2rc1.dev54+g73f48ce55 - **CUDA**: 12.x - **PyTorch**: 2.9.0+cu129 - **Model**: Qwen/Qwen3-Next-80B-A3B-Instruct - **Precision**: BF16 (torch.bfloat16) - **Tensor parallel**: TP=4 and TP=8 (both crash) ### 🐛 Describe the bug The FlashInfer CUTLASS Unquantized MoE backend triggers a **deterministic** CUDA illegal memory access during PIECEWISE CUDA graph capture for Qwen3-Next-80B-A3B-Instruct (BF16) on NVIDIA H100 GPUs. The crash occurs at `custom_all_reduce.cuh:455` at approximately step 143/147 of CUDA graph capture. This regression was introduced by #36286 ("Migrate Unquantized to Full Oracle Flow"), which changed the default unquantized MoE backend priority to prefer **FlashInfer CUTLASS** over **TRITON**. The same model serves correctly with `--moe-backend triton`. ### Related Issues - #30579 — Same model/crash on B200, closed by stale bot without a fix - #37758 — FlashInfer CUTLASS/TRTLLM failures for Qwen3.5 BF16 DP/EP (separate configurations, same underlying kernel issue) ### Regression Range - **Last working**: vLLM...

## 现有链接修复摘要

#36286 [MoE Refactor] Migrate Unquantized to Full Oracle Flow

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: FlashInfer CUTLASS MoE backend causes CUDA illegal memory access on H100 during CUDA graph capture (Qwen3-Next-80B BF16) ### Your current environment - **GPU**: NVIDIA H100 80GB HBM3 (8x per node, NVLink connecte...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ur current environment - **GPU**: NVIDIA H100 80GB HBM3 (8x per node, NVLink connected) - **Platform**: DGX H100 (Eos cluster) - **vLLM version**: v0.18.2rc1.dev54+g73f48ce55 - **CUDA**: 12.x - **PyTorch**: 2.9.0+cu129...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: illegal memory access on H100 during CUDA graph capture (Qwen3-Next-80B BF16) ### Your current environment - **GPU**: NVIDIA H100 80GB HBM3 (8x per node, NVLink connected) - **Platform**: DGX H100 (Eos cluster) - **vLLM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: FlashInfer CUTLASS MoE backend causes CUDA illegal memory access on H100 during CUDA graph capture (Qwen3-Next-80B BF16) ### Your current environment - **GPU**: NVIDIA H100 80GB HBM3 (8x per node, NVLink connecte...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: on`. ### Related Issues - #30579 — Same model/crash on B200, closed by stale bot without a fix - #37758 — FlashInfer CUTLASS/TRTLLM failures for Qwen3.5 BF16 DP/EP (separate configurations, same underlying kernel issue)...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36286](https://github.com/vllm-project/vllm/pull/36286) | mentioned | 0.45 | [MoE Refactor] Migrate Unquantized to Full Oracle Flow | vllm v0.18.1rc1.dev266 (flashinfer cutlass selected by default after #36286) - **still failing**: vllm v0.19.1rc1.dev45 > **note**: the fix shipped in v0.19.1rc1.dev29-35 resolved… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
