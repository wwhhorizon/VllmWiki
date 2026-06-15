# vllm-project/vllm#20170: [Bug]:RuntimeError: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#20170](https://github.com/vllm-project/vllm/issues/20170) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]:RuntimeError: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment vllm/vllm-openai：v0.9.1 ### 🐛 Describe the bug (VllmWorker rank=3 pid=226) ERROR 06-26 23:10:17 [multiproc_executor.py:527] WorkerProc hit an exception. (VllmWorker rank=3 pid=226) ERROR 06-26 23:10:17 [multiproc_executor.py:527] Traceback (most recent call last): (VllmWorker rank=3 pid=226) ERROR 06-26 23:10:17 [multiproc_executor.py:527] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 522, in worker_busy_loop (VllmWorker rank=3 pid=226) ERROR 06-26 23:10:17 [multiproc_executor.py:527] output = func(*args, **kwargs) (VllmWorker rank=3 pid=226) ERROR 06-26 23:10:17 [multiproc_executor.py:527] ^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=3 pid=226) ERROR 06-26 23:10:17 [multiproc_executor.py:527] File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context (VllmWorker rank=3 pid=226) ERROR 06-26 23:10:17 [multiproc_executor.py:527] return func(*args, **kwargs) (VllmWorker rank=3 pid=226) ERROR 06-26 23:10:17 [multiproc_executor.py:527] ^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=3 pid=226) ERROR 06-26 23:10:17 [multiproc_executor.py:527] File "/usr/local/lib/python3.12/dist-pac...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: ]:RuntimeError: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment vllm/vllm-openai：v0.9.1 ### 🐛 Describe the bug (VllmWorker rank=3 pid=226) ERROR 06-26 23:10:17 [multiproc_exec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: mWorker rank=3 pid=226) ERROR 06-26 23:10:17 [multiproc_executor.py:527] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. (VllmWorker rank=3 pid=226) ERROR 06-26 23:10:17 [multiproc_executor.py:527] (...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disabl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: on3.12/dist-packages/vllm/v1/worker/gpu_worker.py", line 293, in execute_model (VllmWorker rank=3 pid=226) ERROR 06-26 23:10:17 [multiproc_executor.py:527] output = self.model_runner.execute_model(scheduler_output, (Vll...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: gnu/libc.so.6) terminate called after throwing an instance of 'c10::DistBackendError' (VllmWorker rank=0 pid=223) ERROR 06-26 23:10:17 [multiproc_executor.py:527] WorkerProc hit an exception. (VllmWorker rank=0 pid=223)...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 53 (0x7f481cbb3253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #4: <unknown function> + 0x94ac3 (0x7f489d793ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #5: clone + 0x… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x14d (0x7f482c89ee8d in /usr/local/lib/python3.12/dist-pack… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdc253 (0x7f481cbb3253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unkn… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
