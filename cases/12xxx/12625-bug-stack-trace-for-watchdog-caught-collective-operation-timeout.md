# vllm-project/vllm#12625: [Bug]: stack trace for "Watchdog caught collective operation timeout"

| 字段 | 值 |
| --- | --- |
| Issue | [#12625](https://github.com/vllm-project/vllm/issues/12625) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: stack trace for "Watchdog caught collective operation timeout"

### Issue 正文摘录

### Your current environment ### Model Input Dumps Unfortunately, the problematic inputs cannot be pickled for some reason, here is what happens after `Error in model execution`: ``` (VllmWorkerProcess pid=350) ERROR 01-29 20:00:47 multiproc_worker_utils.py:240] RuntimeError: Error in model execution: NCCL error: unhandled cuda error (run with NCCL_DEBUG=INFO for details) (VllmWorkerProcess pid=351) INFO 01-29 20:00:47 model_runner_base.py:120] Writing input of failed execution to /tmp/err_execute_model_input_20250129-200047.pkl... (VllmWorkerProcess pid=351) WARNING 01-29 20:00:47 model_runner_base.py:143] Failed to pickle inputs of failed execution: CUDA error: an illegal memory access was encountered (VllmWorkerProcess pid=351) WARNING 01-29 20:00:47 model_runner_base.py:143] CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. (VllmWorkerProcess pid=351) WARNING 01-29 20:00:47 model_runner_base.py:143] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 (VllmWorkerProcess pid=351) WARNING 01-29 20:00:47 model_runner_base.py:143] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` ### 🐛 Des...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: mWorkerProcess pid=351) WARNING 01-29 20:00:47 model_runner_base.py:143] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` ### 🐛 Describe the bug This is a follow-up to this issue https://github.co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ective operation timeout" bug;stale ### Your current environment ### Model Input Dumps Unfortunately, the problematic inputs cannot be pickled for some reason, here is what happens after `Error in model execution`: ```...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Bug]: stack trace for "Watchdog caught collective operation timeout" bug;stale ### Your current environment ### Model Input Dumps Unfortunately, the problematic inputs cannot be pickled for some reason, here is what hap...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --host=0.0.0.0 --port=8080 --model=Llama-3.3-70B-Instruct-FP8-Dynamic --disable-log-requests --dtype=auto --gpu-memory-utilization=0.92 --kv-cache-dtype=auto --load-format=safetensors --max-num-seqs=32 --num_scheduler_s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ls.py:240] RuntimeError: Error in model execution: NCCL error: unhandled cuda error (run with NCCL_DEBUG=INFO for details) (VllmWorkerProcess pid=351) INFO 01-29 20:00:47 model_runner_base.py:120] Writing input of faile...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 0x94ac3 (0x7f31b3193ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #4: clone + 0x44 (0x7f31b3224a04 in /usr/lib/x86_64-linux-gnu/libc.so.6) critical 01-29 20:00:47 launcher.py:… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x14d (0x7f316842c61d in /usr/local/lib/python3.12/dist-pack… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0x145c0 (0x7f31b294e5c0 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorc… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
