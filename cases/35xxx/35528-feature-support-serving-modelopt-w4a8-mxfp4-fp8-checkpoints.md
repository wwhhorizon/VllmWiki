# vllm-project/vllm#35528: [Feature]: Support serving ModelOpt W4A8 MXFP4+FP8 checkpoints

| 字段 | 值 |
| --- | --- |
| Issue | [#35528](https://github.com/vllm-project/vllm/issues/35528) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;kernel;moe;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: Support serving ModelOpt W4A8 MXFP4+FP8 checkpoints

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Some users have interest in w4a8 quantization configurations, in mxfp4-mxfp8 weight and activation storage. And are not interested in the GPTOSS model family. modelopt allows for this configuration and provides support to quantize to this format, but vllm is unable to use the quantized weights via vllmconfig. Models tested: (qwen3-30B-A3B) vLLM v0.16.0 has FlashInfer MXFP4+MXFP8 MoE kernels for Blackwell (SM100), but the only tools that can produce compatible checkpoints are: | Quantizer | Checkpoint Format | vLLM Path | Native MXFP4 MoE on B200? | |---|---|---|---| | **OpenAI (native training)** | gpt-oss OCP MX format | `quantization="mxfp4"` | Yes — designed for gpt-oss | | **AMD Quark** | OCP MX (HF export) | `quantization="quark"` | Yes — [Quark MXFP4 docs](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/gpu_dev_optimize/mxfp4_quantization_quark_vllm.html) | | **llm-compressor** | compressed-tensors MXFP4 | auto-detected → Marlin | No — `CompressedTensorsW4A4Mxfp4MoEMethod` hardcodes `NvFp4MoeBackend.MARLIN` | | **NVIDIA ModelOpt** | `W4A8_MXFP4_FP8_CFG` | Rejected by `QUANT_ALGOS` | No — blocked at config parsin...

## 现有链接修复摘要

#33786 Add support for ModelOpt MXFP8 dense models

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [Feature]: Support serving ModelOpt W4A8 MXFP4+FP8 checkpoints feature request;stale ### 🚀 The feature, motivation and pitch Some users have interest in w4a8 quantization configurations, in mxfp4-mxfp8 weight and activa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: (qwen3-30B-A3B) vLLM v0.16.0 has FlashInfer MXFP4+MXFP8 MoE kernels for Blackwell (SM100), but the only tools that can produce compatible checkpoints are: | Quantizer | Checkpoint Format | vLLM Path | Native MXFP4 MoE o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Feature]: Support serving ModelOpt W4A8 MXFP4+FP8 checkpoints feature request;stale ### 🚀 The feature, motivation and pitch Some users have interest in w4a8 quantization configurations, in mxfp4-mxfp8 weight and activa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: eights via vllmconfig. Models tested: (qwen3-30B-A3B) vLLM v0.16.0 has FlashInfer MXFP4+MXFP8 MoE kernels for Blackwell (SM100), but the only tools that can produce compatible checkpoints are: | Quantizer | Checkpoint F...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: on Blackwell. ## Current Behavior **Quantization (works):** ```python import modelopt.torch.quantization as mtq mtq.quantize(model, mtq.W4A8_MXFP4_FP8_CFG, forward_loop) export_hf_checkpoint(model, export_dir="./checkpo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33786](https://github.com/vllm-project/vllm/pull/33786) | mentioned | 0.45 | Add support for ModelOpt MXFP8 dense models | e=argskwargs] ``` in v0.16.0, `mxfp8` was added to the whitelist (pr #33786), but the quant_algo produced by `w4a8_mxfp4_fp8_cfg` still doesn't match any entry ### additional cont… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
