# vllm-project/vllm#44211: [RFC]: vLLM NaN Reporting

| 字段 | 值 |
| --- | --- |
| Issue | [#44211](https://github.com/vllm-project/vllm/issues/44211) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cache;cuda;fp8;kernel;moe;operator;quantization |
| 症状 | mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: vLLM NaN Reporting

### Issue 正文摘录

# RFC: KV Cache NaN Detection ## Motivation We discovered that R1 NVFP4 had issues with NaNs in the forward pass. While debugging, https://github.com/vllm-project/vllm/pull/43318 was created to aid debugging, which helped us find and fix the following NaN-inducing bugs: * https://github.com/vllm-project/vllm/pull/39444: dummy run writing NaN to KV cache null block * https://github.com/vllm-project/vllm/pull/38148: FP8 scale buffers allocated with torch.empty instead of torch.zeros * https://github.com/vllm-project/vllm/pull/42984: SiLU-Mul quant kernel spreading NaN across row boundaries * https://github.com/vllm-project/vllm/issues/40047: broader sweep of kernels spreading NaN across rows (silu_and_mul_scaled_nvfp4_experts_quantize, scaled_fp4_grouped_quantize) * https://github.com/deepseek-ai/DeepEP/issues/621: DeepEP low-latency combine race condition producing incorrect results at batch size 512+ * https://github.com/deepseek-ai/DeepEP/pull/632: proposed fix for the above * https://github.com/flashinfer-ai/flashinfer/issues/2861: FlashInfer mm_fp4 NaN sensitivity with 8x4 SF layout * https://github.com/flashinfer-ai/flashinfer/issues/3103: grouped_gemm_nt_masked spreading NaN...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: RFC # RFC: KV Cache NaN Detection ## Motivation We discovered that R1 NVFP4 had issues with NaNs in the forward pass. While debugging, https://github.com/vllm-project/vllm/pull/43318 was created to aid debugging, which...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: t_masked spreading NaN across row boundaries * https://github.com/tlrmchlsmth/vllm/pull/33: CUDA graph NaN padding tests for attention/MoE/per-token ops Also related: https://github.com/Dao-AILab/flash-attention/issues/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ted to aid debugging, which helped us find and fix the following NaN-inducing bugs: * https://github.com/vllm-project/vllm/pull/39444: dummy run writing NaN to KV cache null block * https://github.com/vllm-project/vllm/...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: er sweep of kernels spreading NaN across rows (silu_and_mul_scaled_nvfp4_experts_quantize, scaled_fp4_grouped_quantize) * https://github.com/deepseek-ai/DeepEP/issues/621: DeepEP low-latency combine race condition produ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: seek-ai/DeepEP/pull/632: proposed fix for the above * https://github.com/flashinfer-ai/flashinfer/issues/2861: FlashInfer mm_fp4 NaN sensitivity with 8x4 SF layout * https://github.com/flashinfer-ai/flashinfer/issues/31...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
