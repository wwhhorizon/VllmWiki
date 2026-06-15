# vllm-project/vllm#17875: [Bug]: V1 on AMD MI300A complains that cupy is not present

| 字段 | 值 |
| --- | --- |
| Issue | [#17875](https://github.com/vllm-project/vllm/issues/17875) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 on AMD MI300A complains that cupy is not present

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running V1 on the AMD MI300A (this is an example with Ray, running distributed APUs), vLLM complains that cupy is missing. I'm confused as to why it would even need cupy since this is running on ROCm (latest rocm/vllm nightly docker image)? This invocation works perfectly fine with the same command line below with V0. Please note that even though this is on AMD APUs with ROCm, CUDA Graph optimizations performed by vllm do succeed. Setting `enforce_eager=True` in an attempt to disable in vllm anything having to do with CUDA whatsoever, still results in vllm failing on no module cupy found. Why would cupy be needed for ROCm here? `podman exec --env VLLM_USE_V1=1 --env VLLM_USE_AITER=1 --env VLLM_WORKER_MULTIPROC_METHOD=spawn --env VLLM_USE_MODELSCOPE=False --env VLLM_USE_TRITON_FLASH_ATTN=0 --env VLLM_NO_USAGE_STATS=1 --env DO_NOT_TRACK=1 --log-level=error ${CONTAINER_ID} vllm serve /app/models/${MODEL} --gpu_memory_utilization=${GPUMEMUTIL} --tensor-parallel-size ${TP} --pipeline-parallel-size ${PP} --distributed-executor-backend ray --max-num-seqs 64 --max-num-batched-tokens 320000 --max-model-len ${MAX_MODEL_LEN} --no-enabl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: d even need cupy since this is running on ROCm (latest rocm/vllm nightly docker image)? This invocation works perfectly fine with the same command line below with V0. Please note that even though this is on AMD APUs wit...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: V1 on AMD MI300A complains that cupy is not present bug;stale ### Your current environment ### 🐛 Describe the bug When running V1 on the AMD MI300A (this is an example with Ray, running distributed APUs), vLLM co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: rser='serve', model_tag='/app/models/Llama-4-Maverick-17B-128E-Instr uct-FP8', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, al lowed_origins=['*']...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: e needed for ROCm here? `podman exec --env VLLM_USE_V1=1 --env VLLM_USE_AITER=1 --env VLLM_WORKER_MULTIPROC_METHOD=spawn --env VLLM_USE_MODELSCOPE=False --env VLLM_USE_TRITON_FLASH_ATTN=0 --env VLLM_NO_USAGE_STATS=1 --e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: V1 on AMD MI300A complains that cupy is not present bug;stale ### Your current environment ### 🐛 Describe the bug When running V1 on the AMD MI300A (this is an example with Ray, running distributed APUs), vLLM co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
