# vllm-project/vllm#37908: [RFC]: Add Nunchaku SVDQuant W4A4 quantization backend

| 字段 | 值 |
| --- | --- |
| Issue | [#37908](https://github.com/vllm-project/vllm/issues/37908) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;distributed_parallel;gemm_linear;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;kernel;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Add Nunchaku SVDQuant W4A4 quantization backend

### Issue 正文摘录

### Motivation. [SVDQuant](https://arxiv.org/abs/2411.05007) (W4A4 with low-rank correction) is currently the only practical quantization method for diffusion transformers, delivering 2x+ speedup with minimal quality loss. It is implemented by the [Nunchaku](https://github.com/nunchaku-ai/nunchaku) library, which provides custom CUDA kernels for W4A4 GEMM with fused low-rank projection. We are working on Nunchaku integration in [vllm-omni](https://github.com/vllm-project/vllm-omni) ([PR #1986](https://github.com/vllm-project/vllm-omni/pull/1986)). During review, the vllm-omni maintainer [raised the concern](https://github.com/vllm-project/vllm-omni/pull/1986#issuecomment-4087165544) that implementing this entirely on the omni side involves invasive changes to model pipeline files, and [asked us to identify](https://github.com/vllm-project/vllm-omni/pull/1986#issuecomment-4087688296) which parts can be reused from vLLM upstream to keep the omni-side integration lightweight. After analysis, the core quantization backend — `QuantizationConfig` + `LinearMethodBase` implementing `create_weights()` / `apply()` / `process_weights_after_loading()` — follows the exact same pattern as exist...

## 现有链接修复摘要

#43471 [Feature][Quantization] Add SVDQuant W4A4 (nunchaku backend)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [RFC]: Add Nunchaku SVDQuant W4A4 quantization backend ### Motivation. [SVDQuant](https://arxiv.org/abs/2411.05007) (W4A4 with low-rank correction) is currently the only practical quantization method for diffusion trans...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: (https://github.com/nunchaku-ai/nunchaku) library, which provides custom CUDA kernels for W4A4 GEMM with fused low-rank projection. We are working on Nunchaku integration in [vllm-omni](https://github.com/vllm-project/v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: implementing this entirely on the omni side involves invasive changes to model pipeline files, and [asked us to identify](https://github.com/vllm-project/vllm-omni/pull/1986#issuecomment-4087688296) which parts can be r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: lin (for GPTQ/AWQ) and DeepGEMM (for FP8). This part has no diffusion-specific logic and can live in vLLM upstream. Placing it here would allow vllm-omni to import and use it directly, keeping only diffusion-specific gl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [RFC]: Add Nunchaku SVDQuant W4A4 quantization backend ### Motivation. [SVDQuant](https://arxiv.org/abs/2411.05007) (W4A4 with low-rank correction) is currently the only practical quantization method for diffusion trans...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43471](https://github.com/vllm-project/vllm/pull/43471) | closes_keyword | 0.95 | [Feature][Quantization] Add SVDQuant W4A4 (nunchaku backend) | Closes / Refs - Implements RFC #37908 (open) - Replaces the design from the closed vllm-project/vllm-omni#1986 (which tried to do this entirely on the omni side) --- **AI assist |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
