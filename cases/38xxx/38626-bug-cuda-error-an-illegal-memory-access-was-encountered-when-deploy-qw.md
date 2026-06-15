# vllm-project/vllm#38626: [Bug]: CUDA error: an illegal memory access was encountered when deploy Qwen3.5-35B-A3B-FP8 on A100

| 字段 | 值 |
| --- | --- |
| Issue | [#38626](https://github.com/vllm-project/vllm/issues/38626) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: CUDA error: an illegal memory access was encountered when deploy Qwen3.5-35B-A3B-FP8 on A100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug server command ``` vllm serve Qwen/Qwen3.5-35B-A3B-FP8 --max-log-len=200 --served-model-name=atom --gpu-memory-utilization=0.9 --port=8011 --root-path=/openai --trust-remote-code --enable-auto-tool-choice --tool-call-parser=qwen3_coder --reasoning-parser=qwen3 -tp=2 ``` error log ``` (APIServer pid=144) INFO: 127.0.0.6:45561 - "GET /health HTTP/1.1" 200 OK (Worker pid=899) (Worker_TP1 pid=899) ERROR 03-31 10:11:24 [multiproc_executor.py:880] WorkerProc hit an exception. (Worker pid=899) (Worker_TP1 pid=899) ERROR 03-31 10:11:24 [multiproc_executor.py:880] Traceback (most recent call last): (Worker pid=899) (Worker_TP1 pid=899) ERROR 03-31 10:11:24 [multiproc_executor.py:880] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 875, in worker_busy_loop (Worker pid=899) (Worker_TP1 pid=899) ERROR 03-31 10:11:24 [multiproc_executor.py:880] output = func(*args, **kwargs) (Worker pid=899) (Worker_TP1 pid=899) ERROR 03-31 10:11:24 [multiproc_executor.py:880] ^^^^^^^^^^^^^^^^^^^^^ (Worker pid=899) (Worker_TP1 pid=899) ERROR 03-31 10:11:24 [multiproc_executor.py:880] File "/usr/local/lib/python3.12/...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: 0:11:24 [multiproc_executor.py:880] return self.worker.execute_model(scheduler_output) (Worker pid=899) (Worker_TP1 pid=899) ERROR 03-31 10:11:24 [multiproc_executor.py:880] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: gnu/libc.so.6) terminate called after throwing an instance of 'c10::DistBackendError' what(): [PG ID 2 PG GUID 3 Rank 1] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 9) (Worker_TP1 pid=899) ERROR 03-31 10:11:24 [multiproc_executor.py:880] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. (Worker pid=899) (Worker_TP1 pid=899) ERROR 03-31 10:11:24 [multiproc_executor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: or: an illegal memory access was encountered when deploy Qwen3.5-35B-A3B-FP8 on A100 bug ### Your current environment ### 🐛 Describe the bug server command ``` vllm serve Qwen/Qwen3.5-35B-A3B-FP8 --max-log-len=200 --ser...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: CUDA error: an illegal memory access was encountered when deploy Qwen3.5-35B-A3B-FP8 on A100 bug ### Your current environment ### 🐛 Describe the bug server command ``` vllm serve Qwen/Qwen3.5-35B-A3B-FP8 --max-lo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 0x94ac3 (0x7f1e2f473ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #4: <unknown function> + 0x1268d0 (0x7f1e2f5058d0 in /usr/lib/x86_64-linux-gnu/libc.so.6) (enginecore_dp0 pid… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xdc253 (0x7f1def8b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unkn… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | 53 (0x7f1def8b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown function> + 0x94ac3 (0x7f1e2f473ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #8: <unknown f… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
