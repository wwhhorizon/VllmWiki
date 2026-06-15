# vllm-project/vllm#33859: [Bug]: DeepSeek V3.2-NVFP4 with flashinfer moe reports `q must have dtype torch::kBFloat16`

| 字段 | 值 |
| --- | --- |
| Issue | [#33859](https://github.com/vllm-project/vllm/issues/33859) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;moe |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V3.2-NVFP4 with flashinfer moe reports `q must have dtype torch::kBFloat16`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Reproducible command: ``` VLLM_USE_FLASHINFER_MOE_FP4=1 vllm serve --gpu-memory-utilization=0.85 --tokenizer-mode=deepseek_v32 --no-enable-expert-parallel --enable-sleep-mode --model /root/workspaces/models/DeepSeek-V3.2-NVFP4 --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_buffer_device":"cuda"}' -tp 2 -dp 2 -dpl 2 -dpa 10.0.8.10 -dpr 0 ``` ``` (Worker_DP0_TP0 pid=139413) ERROR 02-05 02:55:30 [multiproc_executor.py:852] return func(*args, **kwargs) (Worker_DP0_TP0 pid=139413) ERROR 02-05 02:55:30 [multiproc_executor.py:852] ^^^^^^^^^^^^^^^^^^^^^ (Worker_DP0_TP0 pid=139413) ERROR 02-05 02:55:30 [multiproc_executor.py:852] File "/root/workspaces/kebe/vllm-824058076c56164a3772a5f5829bd9662507e5a3/vllm/model_executor/layers/attention/mla_attention.py", line 868, in unified_mla_attention_with_output (Worker_DP0_TP0 pid=139413) ERROR 02-05 02:55:30 [multiproc_executor.py:852] layer.forward_impl( (Worker_DP0_TP0 pid=139413) ERROR 02-05 02:55:30 [multiproc_executor.py:852] File "/root/workspaces/kebe/vllm-824058076c56164a3772a5f5829bd9662507e5a3/vllm/model_executor/layers/attention/mla_attention.py", line 6...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: DeepSeek V3.2-NVFP4 with flashinfer moe reports `q must have dtype torch::kBFloat16` bug ### Your current environment ### 🐛 Describe the bug Reproducible command: ``` VLLM_USE_FLASHINFER_MOE_FP4=1 vllm serve --gp...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: DeepSeek V3.2-NVFP4 with flashinfer moe reports `q must have dtype torch::kBFloat16` bug ### Your current environment ### 🐛 Describe the bug Reproducible command: ``` VLLM_USE_FLASHINFER_MOE_FP4=1 vllm serve --gp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [multiproc_executor.py:852] attn_out = self._forward_fp8_kv_separate_prefill_decode( (Worker_DP0_TP0 pid=139413) ERROR 02-05 02:55:30 [multiproc_executor.py:852] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_DP0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: DeepSeek V3.2-NVFP4 with flashinfer moe reports `q must have dtype torch::kBFloat16` bug ### Your current environment ### 🐛 Describe the bug Reproducible command: ``` VLLM_USE_FLASHINFER_MOE_FP4=1 vllm serve --gp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t16` bug ### Your current environment ### 🐛 Describe the bug Reproducible command: ``` VLLM_USE_FLASHINFER_MOE_FP4=1 vllm serve --gpu-memory-utilization=0.85 --tokenizer-mode=deepseek_v32 --no-enable-expert-parallel --e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
