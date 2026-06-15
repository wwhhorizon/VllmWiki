# vllm-project/vllm#25929: [Bug]: Mismatched number of arguments

| 字段 | 值 |
| --- | --- |
| Issue | [#25929](https://github.com/vllm-project/vllm/issues/25929) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mismatched number of arguments

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash OMP_NUM_THREADS=8 VLLM_USE_AITER_UNIFIED_ATTENTION=1 VLLM_ATTENTION_BACKEND=FLASHINFER VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve --async-scheduling --gpu-memory-utilization 0.8 --enable-auto-tool-choice --tool-call-parser hermes --model=Qwen/Qwen3-30B-A3B-Instruct-2507 ``` ``` (Worker pid=2952) ERROR 09-30 13:16:20 [multiproc_executor.py:671] WorkerProc hit an exception. (Worker pid=2952) ERROR 09-30 13:16:20 [multiproc_executor.py:671] Traceback (most recent call last): (Worker pid=2952) ERROR 09-30 13:16:20 [multiproc_executor.py:671] File "/home/jasl/.venv/lib/python3.12/site-packages/vllm/v1/attention/backends/flashinfer.py", line 1132, in fast_plan_decode (Worker pid=2952) ERROR 09-30 13:16:20 [multiproc_executor.py:671] self._plan_info = self._cached_module.plan( (Worker pid=2952) ERROR 09-30 13:16:20 [multiproc_executor.py:671] ^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker pid=2952) ERROR 09-30 13:16:20 [multiproc_executor.py:671] File "python/tvm_ffi/cython/function.pxi", line 678, in core.Function.__call__ (Worker pid=2952) ERROR 09-30 13:16:20 [multiproc_executor.py:671] TypeError: Mismatched number of arguments when calling...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: vironment ### 🐛 Describe the bug ```bash OMP_NUM_THREADS=8 VLLM_USE_AITER_UNIFIED_ATTENTION=1 VLLM_ATTENTION_BACKEND=FLASHINFER VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve --async-scheduling --gpu-memory-utilization 0.8 --...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lib/python3.12/site-packages/vllm/v1/worker/gpu_worker.py", line 344, in compile_or_warm_up_model (Worker pid=2952) ERROR 09-30 13:16:20 [multiproc_executor.py:671] cuda_graph_memory_bytes = self.model_runner.capture_mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Mismatched number of arguments bug;stale ### Your current environment ### 🐛 Describe the bug ```bash OMP_NUM_THREADS=8 VLLM_USE_AITER_UNIFIED_ATTENTION=1 VLLM_ATTENTION_BACKEND=FLASHINFER VLLM_USE_FLASHINFER_MOE_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ED_ATTENTION=1 VLLM_ATTENTION_BACKEND=FLASHINFER VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve --async-scheduling --gpu-memory-utilization 0.8 --enable-auto-tool-choice --tool-call-parser hermes --model=Qwen/Qwen3-30B-A3B-In...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Mismatched number of arguments bug;stale ### Your current environment ### 🐛 Describe the bug ```bash OMP_NUM_THREADS=8 VLLM_USE_AITER_UNIFIED_ATTENTION=1 VLLM_ATTENTION_BACKEND=FLASHINFER VLLM_USE_FLASHINFER_MOE_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
