# vllm-project/vllm#30387: [Bug]: illegal memory access countered when using kv-cache-type=fp8  loading  a weight-fp8 model for evaltest  in flash-attn backend

| 字段 | 值 |
| --- | --- |
| Issue | [#30387](https://github.com/vllm-project/vllm/issues/30387) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;fp8 |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: illegal memory access countered when using kv-cache-type=fp8  loading  a weight-fp8 model for evaltest  in flash-attn backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug lm_eval --model vllm \ --model_args pretrained=mymodel,tensor_parallel_size=8,gpu_memory_utilization=0.80,trust_remote_code=true,enforce_eager=true,max_model_len=128001,kv_cache_dtype=fp8 \ --tasks ceval-valid \ --confirm_run_unsafe_code \ --trust_remote_code \ --batch_size 8 \ --num_fewshot 5 \ --log_samples \ when I didn't add kv_cache_dtype=fp8,it could run correctly, but when I added that it ran to Running loglikelihood requests or generate progress, it soon ended by job-55s085tswg-master-0:832:2092 [5] include/alloc.h:388 NCCL WARN Cuda failure 'an illegal memory access was encountered' 2025-12-10 16:43:22.580444297 master-0 >> 2025-12-10 16:43:22.580446154 master-0 >> [2025-12-10 00:43:22] job-55s085tswg-master-0:833:2091 [6] include/alloc.h:388 NCCL WARN Cuda failure 'an illegal memory access was encountered' 2025-12-10 16:43:22.580447413 master-0 >> 2025-12-10 16:43:22.580448844 master-0 >> [2025-12-10 00:43:22] job-55s085tswg-master-0:827:2475 [0] init.cc:1896 NCCL WARN commDestroySync: comm 0x3b8e6e80 rank 0 sync hostStream error 1 2025-12-10 16:43:22.580450374 master-0 >> 2025-12-10 16:43:22.580451319 master-0 >> 2025-...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: illegal memory access countered when using kv-cache-type=fp8 loading a weight-fp8 model for evaltest in flash-attn backend bug;stale ### Your current environment ### 🐛 Describe the bug lm_eval --model vllm \ --mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed by job-55s085tswg-master-0:832:2092 [5] include/alloc.h:388 NCCL WARN Cuda failure 'an illegal memory access was encountered' 2025-12-10 16:43:22.580444297 master-0 >> 2025-12-10 16:43:22.580446154 master-0 >> [2025-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: fp8 loading a weight-fp8 model for evaltest in flash-attn backend bug;stale ### Your current environment ### 🐛 Describe the bug lm_eval --model vllm \ --model_args pretrained=mymodel,tensor_parallel_size=8,gpu_memory_ut...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: countered when using kv-cache-type=fp8 loading a weight-fp8 model for evaltest in flash-attn backend bug;stale ### Your current environment ### 🐛 Describe the bug lm_eval --model vllm \ --model_args pretrained=mymodel,t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -cache-type=fp8 loading a weight-fp8 model for evaltest in flash-attn backend bug;stale ### Your current environment ### 🐛 Describe the bug lm_eval --model vllm \ --model_args pretrained=mymodel,tensor_parallel_size=8,g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
