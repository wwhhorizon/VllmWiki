# vllm-project/vllm#32009: [Bug]: 0% Acceptance rate with FI Cutlass DeepSeekR1 NVFP4 with mtp ep

| 字段 | 值 |
| --- | --- |
| Issue | [#32009](https://github.com/vllm-project/vllm/issues/32009) |
| 状态 | closed |
| 标签 | bug;help wanted;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 0% Acceptance rate with FI Cutlass DeepSeekR1 NVFP4 with mtp ep

### Issue 正文摘录

### Your current environment b200 ### 🐛 Describe the bug ``` launch_cutlass_moe_trtllm_attn_fused_ar_rope_fp8_kv_ep_spec_decode: VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_FLASHINFER_MOE_BACKEND="throughput" CUDA_VISIBLE_DEVICES=1,3,0,5 vllm serve {{MODEL}} -tp {{GPUS}} --port {{PORT}} \ --attention-config.use_trtllm_ragged_deepseek_prefill=True --attention-backend FLASHINFER_MLA \ --compilation_config.pass_config.fuse_allreduce_rms true \ --compilation_config.custom_ops+=+rotary_embedding \ --kv-cache-dtype fp8 --compilation_config.pass_config.fuse_attn_quant true \ --enable-expert-parallel --speculative-config '{"num_speculative_tokens": 3, "method":"deepseek_mtp"}' ``` ``` (APIServer pid=2660027) INFO 01-08 23:07:23 [metrics.py:100] SpecDecoding metrics: Mean acceptance length: 1.02, Accepted throughput: 10.00 tokens/s, Drafted throughput: 1363.65 tokens/s, Accepted: 100 tokens, Drafted: 13638 tokens, Per-position acceptance rate: 0.022, 0.000, 0.000, Avg Draft acceptance rate: 0.7% ``` It works fine with either: - `VLLM_FLASHINFER_MOE_BACKEND="latency"` - no `--enable-expert-parallel` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and as...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: 0% Acceptance rate with FI Cutlass DeepSeekR1 NVFP4 with mtp ep bug;help wanted;stale ### Your current environment b200 ### 🐛 Describe the bug ``` launch_cutlass_moe_trtllm_attn_fused_ar_rope_fp8_kv_ep_spec_decod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ptance rate with FI Cutlass DeepSeekR1 NVFP4 with mtp ep bug;help wanted;stale ### Your current environment b200 ### 🐛 Describe the bug ``` launch_cutlass_moe_trtllm_attn_fused_ar_rope_fp8_kv_ep_spec_decode: VLLM_USE_FL...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: 0% Acceptance rate with FI Cutlass DeepSeekR1 NVFP4 with mtp ep bug;help wanted;stale ### Your current environment b200 ### 🐛 Describe the bug ``` launch_cutlass_moe_trtllm_attn_fused_ar_rope_fp8_kv_ep_spec_decod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: R1 NVFP4 with mtp ep bug;help wanted;stale ### Your current environment b200 ### 🐛 Describe the bug ``` launch_cutlass_moe_trtllm_attn_fused_ar_rope_fp8_kv_ep_spec_decode: VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_FLASHINFER_M...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: spec_decode: VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_FLASHINFER_MOE_BACKEND="throughput" CUDA_VISIBLE_DEVICES=1,3,0,5 vllm serve {{MODEL}} -tp {{GPUS}} --port {{PORT}} \ --attention-config.use_trtllm_ragged_deepseek_prefill=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
