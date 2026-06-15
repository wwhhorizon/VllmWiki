# vllm-project/vllm#36828: [Bug]: vLLm 0.17.1 (docker) crash with Qwen 3.5 27B-FP8 in BatchPrefillWithPagedKVCache

| 字段 | 值 |
| --- | --- |
| Issue | [#36828](https://github.com/vllm-project/vllm/issues/36828) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;quantization;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;fp8;operator |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLm 0.17.1 (docker) crash with Qwen 3.5 27B-FP8 in BatchPrefillWithPagedKVCache

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug bug occurs after the first inference attempt. started with CUDA_VISIBLE_DEVICES=1 (A100 80GB) ``` command: /models/Qwen_Qwen3.5-27B-FP8 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_coder --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":5}' --served-model-name qwen-3.5-27b home gpt-3.5-turbo default --gpu-memory-utilization=0.97 --enable-prefix-caching --attention-backend FLASHINFER ``` container logs: https://gist.github.com/matatonic/f08eb26807b7ecb7a63ef7aaad7fd476 Ends with: ``` vllm | (EngineCore_DP0 pid=142) File "/usr/local/lib/python3.12/dist-packages/flashinfer/prefill.py", line 666, in paged_run vllm | (EngineCore_DP0 pid=142) paged_run_func( vllm | (EngineCore_DP0 pid=142) File "python/tvm_ffi/cython/function.pxi", line 929, in tvm_ffi.core.Function.__call__ vllm | (EngineCore_DP0 pid=142) File " ", line 0, in __tvm_ffi_paged_run vllm | (EngineCore_DP0 pid=142) File "/workspace/build/aot/generated/batch_prefill_with_kv_cache_dtype_q_bf16_dtype_kv_bf16_dtype_o_bf16_dtype_idx_i32_head_dim_qk_256_head_dim_vo_256_posenc_0_use_swa_False_use_logits_cap_False_f16qk_False/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: vLLm 0.17.1 (docker) crash with Qwen 3.5 27B-FP8 in BatchPrefillWithPagedKVCache bug ### Your current environment ### 🐛 Describe the bug bug occurs after the first inference attempt. started with CUDA_VISIBLE_DEV...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: vLLm 0.17.1 (docker) crash with Qwen 3.5 27B-FP8 in BatchPrefillWithPagedKVCache bug ### Your current environment ### 🐛 Describe the bug bug occurs after the first inference attempt. started with CUDA_VISIBLE_DEV...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ibe the bug bug occurs after the first inference attempt. started with CUDA_VISIBLE_DEVICES=1 (A100 80GB) ``` command: /models/Qwen_Qwen3.5-27B-FP8 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vLLm 0.17.1 (docker) crash with Qwen 3.5 27B-FP8 in BatchPrefillWithPagedKVCache bug ### Your current environment ### 🐛 Describe the bug bug occurs after the first inference attempt. started with CUDA_VISIBLE_DEV...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: efault --gpu-memory-utilization=0.97 --enable-prefix-caching --attention-backend FLASHINFER ``` container logs: https://gist.github.com/matatonic/f08eb26807b7ecb7a63ef7aaad7fd476 Ends with: ``` vllm | (EngineCore_DP0 pi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
