# vllm-project/vllm#43858: [Feature]: DFlash Partial Multimodal Token Full Attention with Gemma MoE + Drafter

| 字段 | 值 |
| --- | --- |
| Issue | [#43858](https://github.com/vllm-project/vllm/issues/43858) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | attention;cuda;kernel;moe;quantization;sampling |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: DFlash Partial Multimodal Token Full Attention with Gemma MoE + Drafter

### Issue 正文摘录

- **The issue:** Gemma4 MoE (26B) is an incredible model both in regards to light-weightedness as well as it's high thinking & reasoning capabilities. For end users on top-line consumer cards (5090, (maybe 5080) or above only), Blackwell, this model remains the top-of-the-line choice for users running non-GGUF variations of local LLMs (using vLLM). With Windows, users may gravitate to either WSL or, (from the officially recognized repo on vLLM docs) SystemPanic vLLM fork (SystemPanic/vllm-windows) for getting their first inference with CUDA on Windows, which maintains a heavily up-to-date architecture for builds, as well as prebuilt's for Blackwell support with Windows. Gemma4's MoE architecture was patched as of the latest updates to vLLM, including heavily optimized forks that minimally adjust architecture like SystemPanic's (which runs on the latest vLLM version), meaning, any user attempting to run the 26B MoE, with Nvfp4 (modelopt as opposed to compressed tensors) will have a very easy experience getting their model up and running with the known setup recipes for the heterogenous head-dimensions. That is (tl;dr) $env:VLLM_ALLOW_LONG_MAX_MODEL_LEN = "1" $env:TORCH_MATMUL_PRECI...

## 现有链接修复摘要

#42175 [Core][Model] Gemma4: Unified FA4 for all layers + FlashAttention mm_prefix support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: LLM). With Windows, users may gravitate to either WSL or, (from the officially recognized repo on vLLM docs) SystemPanic vLLM fork (SystemPanic/vllm-windows) for getting their first inference with CUDA on Windows, which...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: est vLLM version), meaning, any user attempting to run the 26B MoE, with Nvfp4 (modelopt as opposed to compressed tensors) will have a very easy experience getting their model up and running with the known setup recipes...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Feature]: DFlash Partial Multimodal Token Full Attention with Gemma MoE + Drafter feature request - **The issue:** Gemma4 MoE (26B) is an incredible model both in regards to light-weightedness as well as it's high thin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: eature]: DFlash Partial Multimodal Token Full Attention with Gemma MoE + Drafter feature request - **The issue:** Gemma4 MoE (26B) is an incredible model both in regards to light-weightedness as well as it's high thinki...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: $env:PYTORCH_CUDA_ALLOC_CONF = "expandable_segments:True" $env:VLLM_USE_FLASHINFER_MOE_FP4 = "0" $env:VLLM_TEST_FORCE_FP8_MARLIN = "0" $env:VLLM_NVFP4_GEMM_BACKEND = "flashinfer-cutlass" $env:VLLM_USE_FLASHINFER_SAMPLER...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42175](https://github.com/vllm-project/vllm/pull/42175) | mentioned | 0.45 | [Core][Model] Gemma4: Unified FA4 for all layers + FlashAttention mm_prefix support | , the path to implementation is not documented. a note to tracking pr #42175 (relates to gemma‑4 speculative decoding). there are two routes. using prepatched docker images, one c… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
