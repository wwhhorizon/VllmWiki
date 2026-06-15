# vllm-project/vllm#38619: [Bug]: Kimi-K2.5 compressed-tensors MoE Marlin repack fails with PTX toolchain error on H200 (CUDA 12.8, driver 570.133.20)

| 字段 | 值 |
| --- | --- |
| Issue | [#38619](https://github.com/vllm-project/vllm/issues/38619) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;moe;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel;moe;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Kimi-K2.5 compressed-tensors MoE Marlin repack fails with PTX toolchain error on H200 (CUDA 12.8, driver 570.133.20)

### Issue 正文摘录

### Your current environment - **vLLM versions tested**: 0.17.1 and 0.18.0 (both fail identically) - **GPU**: NVIDIA H200 (144GB) x 32 (4 nodes, TP8 x PP4) - **Driver**: 570.133.20 - **CUDA**: 12.8 - **PyTorch**: 2.10.0+cu128 - **Python**: 3.12.13 - **OS**: Linux Ubuntu 22.04.5 LTS running kernel 5.15.0-153-generic on x86_64 - **Install method**: `pip install vllm` (prebuilt wheel) ### Describe the bug Serving `moonshotai/Kimi-K2.5` fails during `process_weights_after_loading` when the Marlin MoE repack kernel (`gptq_marlin_moe_repack`) attempts to execute. The model uses `compressed-tensors` quantization (WNA16, INT4, group_size=32) with MoE (384 experts). The checkpoint shards load successfully (64/64), but the subsequent Marlin weight repacking crashes with: ``` torch.AcceleratorError: CUDA error: the provided PTX was compiled with an unsupported toolchain. ``` **Key observation**: A standard (non-MoE) GPTQ-INT4 model (`Qwen/Qwen2.5-7B-Instruct-GPTQ-Int4`) loads and serves correctly on the same cluster with the same vLLM install. The `gptq_marlin` path for dense models works; only the `gptq_marlin_moe_repack` path for MoE models fails. This suggests the PTX incompatibility is s...

## 现有链接修复摘要

#38669 Fix Marlin repack PTX incompatibility on H100/H200 (CUDA 12.8)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 00 (CUDA 12.8, driver 570.133.20) ### Your current environment - **vLLM versions tested**: 0.17.1 and 0.18.0 (both fail identically) - **GPU**: NVIDIA H200 (144GB) x 32 (4 nodes, TP8 x PP4) - **Driver**: 570.133.20 - **...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: in_moe_repack`) attempts to execute. The model uses `compressed-tensors` quantization (WNA16, INT4, group_size=32) with MoE (384 experts). The checkpoint shards load successfully (64/64), but the subsequent Marlin weigh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ressed-tensors MoE Marlin repack fails with PTX toolchain error on H200 (CUDA 12.8, driver 570.133.20) ### Your current environment - **vLLM versions tested**: 0.17.1 and 0.18.0 (both fail identically) - **GPU**: NVIDIA...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: in MoE repack kernel (`gptq_marlin_moe_repack`) attempts to execute. The model uses `compressed-tensors` quantization (WNA16, INT4, group_size=32) with MoE (384 experts). The checkpoint shards load successfully (64/64),...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Kimi-K2.5 compressed-tensors MoE Marlin repack fails with PTX toolchain error on H200 (CUDA 12.8, driver 570.133.20) ### Your current environment - **vLLM versions tested**: 0.17.1 and 0.18.0 (both fail identical...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38669](https://github.com/vllm-project/vllm/pull/38669) | closes_keyword | 0.95 | Fix Marlin repack PTX incompatibility on H100/H200 (CUDA 12.8) | Fixes #38619. The Marlin MoE repack kernel (`gptq_marlin_moe_repack`) crashes with `CUDA error: the provided PTX was compiled with an unsupported toolchain` when serving quantized |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
