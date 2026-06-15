# vllm-project/vllm#25677: [Bug]: v0.8.6 Qwen3-30B-A3B The prefill phase takes 10 times longer when chunked prefill is enabled compared to when it is disabled.

| 字段 | 值 |
| --- | --- |
| Issue | [#25677](https://github.com/vllm-project/vllm/issues/25677) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.8.6 Qwen3-30B-A3B The prefill phase takes 10 times longer when chunked prefill is enabled compared to when it is disabled.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I compared the TTFT (Time to First Token) of a long request (10K tokens) with and without chunked prefill enabled. I found that even though the request is scheduled completely in one go in both scenarios, the time consumed in the prefill phase is 11 times slower when chunked prefill is turned on than when it is turned off. I run vllm serve with following script: ```bash # enable chunked prefill VLLM_USE_V1=0 VLLM_ENGINE_ITERATION_TIMEOUT_S=600 VLLM_USE_RAY_SPMD_WORKER=1 VLLM_USE_RAY_COMPILED_DAG=1 VLLM_LOGGING_LEVEL=DEBUG vllm serve /mnt/lab-nfs/wangyifeng/models/Qwen3-30B-A3B --distributed-executor-backend ray --dtype float32 --gpu-memory-utilization 0.9 --served-model-name qwen3-30b --max-model-len 16834 --enforce-eager -tp 2 -pp 3 --max-num-batched-tokens 16834 --enable-chunked-prefill --max-num-partial-prefills 8 --long-prefill-token-threshold 1024 --max-long-partial-prefills 8 # disable chunked prefill VLLM_USE_V1=0 VLLM_ENGINE_ITERATION_TIMEOUT_S=600 VLLM_USE_RAY_SPMD_WORKER=1 VLLM_USE_RAY_COMPILED_DAG=1 VLLM_LOGGING_LEVEL=DEBUG vllm serve /mnt/lab-nfs/wangyifeng/models/Qwen3-30B-A3B --distributed-executor-backend ray --dty...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: v0.8.6 Qwen3-30B-A3B The prefill phase takes 10 times longer when chunked prefill is enabled compared to when it is disabled. bug;stale ### Your current environment ### 🐛 Describe the bug I compared the TTFT (Tim...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: M_ENGINE_ITERATION_TIMEOUT_S=600 VLLM_USE_RAY_SPMD_WORKER=1 VLLM_USE_RAY_COMPILED_DAG=1 VLLM_LOGGING_LEVEL=DEBUG vllm serve /mnt/lab-nfs/wangyifeng/models/Qwen3-30B-A3B --distributed-executor-backend ray --dtype float32...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ic kernels parameters +# BASE_BLOCK = 128 if current_platform.has_device_capability(80) else 64 BASE_BLOCK = 128 if current_platform.has_device_capability(80) else 64 NUM_WARPS = 4 if current_platform.is_rocm() else 8 @...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: v0.8.6 Qwen3-30B-A3B The prefill phase takes 10 times longer when chunked prefill is enabled compared to when it is disabled. bug;stale ### Your current environment ### 🐛 Describe the bug I compared the TTFT (Tim...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: if this change is the cause of the performance discrepancy. I run vllm benchmark_serving to get benchmark: ```bash python3 vllm/benchmarks/benchmark_serving.py --backend vllm --model /mnt/lab-nfs/wangyifeng/models/Qwen3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
