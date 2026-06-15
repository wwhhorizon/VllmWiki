# vllm-project/vllm#31782: [Feature]: Support compressed-tensors NVFP4 quantization for MoE models (Nemotron-H non-gated MoE)

| 字段 | 值 |
| --- | --- |
| Issue | [#31782](https://github.com/vllm-project/vllm/issues/31782) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;fp8;moe;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support compressed-tensors NVFP4 quantization for MoE models (Nemotron-H non-gated MoE)

### Issue 正文摘录

### Your current environment Using nightly-0d4044edd85de30d7d4558aeea4d1e95c7c556d6 * CUDA: 13.0 (also reproduced on 12.8) * GPU: RTX Pro 6000 Blackwell ### 🐛 Describe the bug Compressed-tensors (llm-compressor) **NVFP4-quantized MoE models** fail to initialize in vLLM due to a hard-coded limitation in the fused MoE layer when `is_act_and_mul=False`. This affects **Nemotron-H / Nemotron-3-Nano-30B-A3B** style MoE models that use a *non-gated* MoE path. The failure occurs even though NVFP4 is supported for dense models and even though NVFP4 is explicitly allowed for MoE *only* when the checkpoint is detected as **ModelOpt NVFP4**. Compressed-tensors NVFP4 is currently not recognized as a supported MoE quantization backend. ## Reproduction ### Model * `Firworks/NVIDIA-Nemotron-3-Nano-30B-A3B-nvfp4` * Quantized using **llm-compressor / compressed-tensors** * Quantization recipe: ```python recipe = QuantizationModifier( targets="Linear", scheme="NVFP4", ignore=[ "lm_head", "re:visual.*", "re:.*vision_tower.*", "re:.*video_tower.*", "re:.*audio_tower.*", "re:.*multi_modal_projector.*", ], ) ``` ### Command ```bash docker run --runtime nvidia --gpus all \ -p 8000:8000 --ipc=host \ vllm/...

## 现有链接修复摘要

#32080 Add support for compressed-tensors NVFP4 in non-gated MoE layers #31782 | #33518 [Bugfix] Fix NVFP4 MoE weight shapes for non-gated MLPs (Nemotron-Nano)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Feature]: Support compressed-tensors NVFP4 quantization for MoE models (Nemotron-H non-gated MoE) feature request;stale ### Your current environment Using nightly-0d4044edd85de30d7d4558aeea4d1e95c7c556d6 * CUDA: 13.0 (...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: though NVFP4 is supported for dense models and even though NVFP4 is explicitly allowed for MoE *only* when the checkpoint is detected as **ModelOpt NVFP4**. Compressed-tensors NVFP4 is currently not recognized as a supp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: nt environment Using nightly-0d4044edd85de30d7d4558aeea4d1e95c7c556d6 * CUDA: 13.0 (also reproduced on 12.8) * GPU: RTX Pro 6000 Blackwell ### 🐛 Describe the bug Compressed-tensors (llm-compressor) **NVFP4-quantized MoE...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature]: Support compressed-tensors NVFP4 quantization for MoE models (Nemotron-H non-gated MoE) feature request;stale ### Your current environment Using nightly-0d4044edd85de30d7d4558aeea4d1e95c7c556d6 * CUDA: 13.0 (...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ensors NVFP4 is currently not recognized as a supported MoE quantization backend. ## Reproduction ### Model * `Firworks/NVIDIA-Nemotron-3-Nano-30B-A3B-nvfp4` * Quantized using **llm-compressor / compressed-tensors** * Q...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32080](https://github.com/vllm-project/vllm/pull/32080) | mentioned | 0.6 | Add support for compressed-tensors NVFP4 in non-gated MoE layers #31782 | r compressed-tensors NVFP4 in non-gated MoE layers #31782 ## Purpose #31782 This PR adds support for **compressed-tensors NVFP4-quantized MoE models** in vLLM, specifically addres… |
| [#33518](https://github.com/vllm-project/vllm/pull/33518) | closes_keyword | 0.95 | [Bugfix] Fix NVFP4 MoE weight shapes for non-gated MLPs (Nemotron-Nano) | Fixes #31782 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
