# vllm-project/vllm#32053: [Model Bash]: DeepSeek NVFP4 B200

| 字段 | 值 |
| --- | --- |
| Issue | [#32053](https://github.com/vllm-project/vllm/issues/32053) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Model Bash]: DeepSeek NVFP4 B200

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # DeepSeek-R1 NVFP4 Model Bash ``` launch_trtllm_moe_trtllm_attn_fused_ar_rope_fp8_kv_ep_spec_decode_mpt3: VLLM_USE_FLASHINFER_MOE_FP16=1 VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_FLASHINFER_MOE_BACKEND="latency" CUDA_VISIBLE_DEVICES=1,3,0,5 vllm serve {{MODEL}} -tp {{GPUS}} --port {{PORT}} \ --attention-config.use_trtllm_ragged_deepseek_prefill=True --attention-backend FLASHINFER_MLA \ --compilation_config.pass_config.fuse_allreduce_rms true \ --compilation_config.custom_ops+=+rotary_embedding \ --kv-cache-dtype fp8 --compilation_config.pass_config.fuse_attn_quant true \ --enable-expert-parallel \ --speculative-config '{"num_speculative_tokens": 3, "method":"deepseek_mtp"}' \ --async-scheduling ``` Key optimizations: - [ ] Write to KV Cache + ROPE can be fused (unwrapping MLA required --- see #24678) - [ ] AR + RMS + Quant (to discuss with flashinfer team) - [ ] RMS Norm + Quant (https://github.com/vllm-project/vllm/pull/32957) - [ ] k nope, k pe copy op (https://github.com/vllm-project/vllm/pull/32734) - [x] SiluAndMul in shared expert is running TORCH NATIVE --- need to run silu_mul_quant (#32059) - [x] Currently using improper nvfp4 quantize in...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Model Bash]: DeepSeek NVFP4 B200 feature request;stale ### 🚀 The feature, motivation and pitch # DeepSeek-R1 NVFP4 Model Bash ``` launch_trtllm_moe_trtllm_attn_fused_ar_rope_fp8_kv_ep_spec_decode_mpt3: VLLM_USE_FLASHIN...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Model Bash]: DeepSeek NVFP4 B200 feature request;stale ### 🚀 The feature, motivation and pitch # DeepSeek-R1 NVFP4 Model Bash ``` launch_trtllm_moe_trtllm_attn_fused_ar_rope_fp8_kv_ep_spec_decode_mpt3: VLLM_USE_FLASHIN...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tllm_moe_trtllm_attn_fused_ar_rope_fp8_kv_ep_spec_decode_mpt3: VLLM_USE_FLASHINFER_MOE_FP16=1 VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_FLASHINFER_MOE_BACKEND="latency" CUDA_VISIBLE_DEVICES=1,3,0,5 vllm serve {{MODEL}} -tp {{G...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Model Bash]: DeepSeek NVFP4 B200 feature request;stale ### 🚀 The feature, motivation and pitch # DeepSeek-R1 NVFP4 Model Bash ``` launch_trtllm_moe_trtllm_attn_fused_ar_rope_fp8_kv_ep_spec_decode_mpt3: VLLM_USE_FLASHIN...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ce_rms true \ --compilation_config.custom_ops+=+rotary_embedding \ --kv-cache-dtype fp8 --compilation_config.pass_config.fuse_attn_quant true \ --enable-expert-parallel \ --speculative-config '{"num_speculative_tokens":...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
