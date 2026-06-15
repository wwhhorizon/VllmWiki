# vllm-project/vllm#33364: [Bug]: Qwen3-Next speculative decoding (DeepSeek MTP) fails for num_speculative_tokens>=3 on H100 with FlashInfer + FP8 KV cache (GMMA operator JIT compile error)

| 字段 | 值 |
| --- | --- |
| Issue | [#33364](https://github.com/vllm-project/vllm/issues/33364) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next speculative decoding (DeepSeek MTP) fails for num_speculative_tokens>=3 on H100 with FlashInfer + FP8 KV cache (GMMA operator JIT compile error)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # 🐛 Bug report When running **Qwen3-Next** with **speculative decoding (DeepSeek MTP)** on an **H100**, inference works with `num_speculative_tokens = 2`, but **fails for `num_speculative_tokens >= 3`**. The failure is caused by a **FlashInfer JIT compilation error** when building a CUDA kernel at runtime. The engine crashes immediately after the kernel compilation fails. This appears to be a **kernel-level compatibility issue** involving: * FlashInfer backend * FP8 KV cache (`e4m3`) * `head_dim = 256` * Hopper (SM90a) --- ## Minimal reproduction ### vLLM serve command ```bash export VLLM_LOGGING_LEVEL=DEBUG export VLLM_ATTENTION_BACKEND=FLASHINFER export KV_CACHE_DTYPE=fp8 # Works vllm serve \ --dtype bfloat16 \ --kv-cache-dtype fp8 \ --speculative-config '{"method":"deepseek_mtp","num_speculative_tokens":2}' # Fails vllm serve \ --dtype bfloat16 \ --kv-cache-dtype fp8 \ --speculative-config '{"method":"deepseek_mtp","num_speculative_tokens":3}' ``` --- ### Python reproduction ```python from vllm import LLM, SamplingParams sampling_params = SamplingParams( temperature=0.0, max_tokens=32, ) llm = LLM( model=" ", dtype="bfloat16",...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: tive_tokens>=3 on H100 with FlashInfer + FP8 KV cache (GMMA operator JIT compile error) bug ### Your current environment ### 🐛 Describe the bug # 🐛 Bug report When running **Qwen3-Next** with **speculative decoding (Dee...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: pSeek MTP) fails for num_speculative_tokens>=3 on H100 with FlashInfer + FP8 KV cache (GMMA operator JIT compile error) bug ### Your current environment ### 🐛 Describe the bug # 🐛 Bug report When running **Qwen3-Next**...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: eculative decoding (DeepSeek MTP) fails for num_speculative_tokens>=3 on H100 with FlashInfer + FP8 KV cache (GMMA operator JIT compile error) bug ### Your current environment ### 🐛 Describe the bug # 🐛 Bug report When...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: decoding (DeepSeek MTP) fails for num_speculative_tokens>=3 on H100 with FlashInfer + FP8 KV cache (GMMA operator JIT compile error) bug ### Your current environment ### 🐛 Describe the bug # 🐛 Bug report When running **...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: k MTP) fails for num_speculative_tokens>=3 on H100 with FlashInfer + FP8 KV cache (GMMA operator JIT compile error) bug ### Your current environment ### 🐛 Describe the bug # 🐛 Bug report When running **Qwen3-Next** with...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
