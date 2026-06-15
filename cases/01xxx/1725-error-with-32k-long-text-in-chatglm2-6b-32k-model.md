# vllm-project/vllm#1725: Error with 32k Long Text in chatglm2-6b-32k Model

| 字段 | 值 |
| --- | --- |
| Issue | [#1725](https://github.com/vllm-project/vllm/issues/1725) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Error with 32k Long Text in chatglm2-6b-32k Model

### Issue 正文摘录

python3 api_server.py --model /hbox2dir/chatglm2-6b-32k --trust-remote-code --host 0.0.0.0 --port 7070 --tensor-parallel-size 2 ``` 2023-11-20 09:55:13,313 INFO worker.py:1642 -- Started a local Ray instance. INFO: Started server process [278296] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://0.0.0.0:7070 (Press CTRL+C to quit) (RayWorker pid=281502) [2023-11-20 09:55:58,328 E 281502 281502] logging.cc:97: Unhandled exception: N3c105ErrorE. what(): CUDA error: an illegal memory access was encountered (RayWorker pid=281502) CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. (RayWorker pid=281502) For debugging consider passing CUDA_LAUNCH_BLOCKING=1. (RayWorker pid=281502) Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. (RayWorker pid=281502) (RayWorker pid=281502) Exception raised from c10_cuda_check_implementation at ../c10/cuda/CUDAException.cpp:44 (most recent call first): (RayWorker pid=281502) frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x57 (0x7f5026eea617 in /root/miniconda3/envs/vllm/lib/python3.8/site-pack...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search | #53 Refactor attention kernels

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ebugging consider passing CUDA_LAUNCH_BLOCKING=1. (RayWorker pid=281502) Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. (RayWorker pid=281502) (RayWorker pid=281502) Exception raised from c10_cuda_c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: local Ray instance. INFO: Started server process [278296] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://0.0.0.0:7070 (Press CTRL+C to quit) (RayWorker pid=281...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: File "/root/miniconda3/envs/vllm/lib/python3.8/site-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/root/miniconda3/envs/vllm/lib/python3.8/site-packages/starlette/r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 281502 281502] logging.cc:97: Unhandled exception: N3c105ErrorE. what(): CUDA error: an illegal memory access was encountered (RayWorker pid=281502) CUDA kernel errors might be asynchronously reported at some other API...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected erro...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | te-packages/torch/lib/libtorch_cuda.so) (rayworker pid=281502) frame #4: c10d::processgroupnccl::worknccl::iscompleted() + 0x58 (0x7f44659e1918 in /root/miniconda3/envs/vllm/lib/p… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | te-packages/torch/lib/libtorch_cuda.so) (rayworker pid=281502) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x78 (0x7f44659f8468 in /root/miniconda3/envs/vllm/lib/python… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | te-packages/torch/lib/libtorch_cuda.so) (rayworker pid=281502) frame #7: <unknown function> + 0xdbbf4 (0x7f5030c81bf4 in /root/miniconda3/envs/vllm/bin/../lib/libstdc++.so.6) (rayw |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | -packages/torch/lib/libtorch_python.so) (rayworker pid=281502) frame #12: ray::rayworker.execute_method() [0x4e0970] (rayworker pid=281502) frame #13: ray::rayworker.execute_metho… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | ::rayworker.execute_method() [0x4f1811] (rayworker pid=281502) frame #16: ray::rayworker.execute_method() [0x4f1811] (rayworker pid=281502) frame #17: ray::rayworker.execute_metho… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | ::rayworker.execute_method() [0x4f1811] (rayworker pid=281502) frame #20: ray::rayworker.execute_method() [0x4f1811] (rayworker pid=281502) frame #21: ray::rayworker.execute_metho… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | ::rayworker.execute_method() [0x4f1811] (rayworker pid=281502) frame #21: ray::rayworker.execute_method() [0x4f1811] (rayworker pid=281502) frame #22: ray::rayworker.execute_metho… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | ::rayworker.execute_method() [0x4f1811] (rayworker pid=281502) frame #27: ray::rayworker.execute_method() [0x4f1811] (rayworker pid=281502) frame #28: ray::rayworker.execute_metho… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | ::rayworker.execute_method() [0x4f1811] (rayworker pid=281502) frame #29: ray::rayworker.execute_method() [0x4f1811] (rayworker pid=281502) frame #30: ray::rayworker.execute_metho… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | ::rayworker.execute_method() [0x4f1811] (rayworker pid=281502) frame #32: ray::rayworker.execute_method() [0x4f1811] (rayworker pid=281502) frame #33: ray::rayworker.execute_metho… |
| [#53](https://github.com/vllm-project/vllm/pull/53) | mentioned | 0.45 | Refactor attention kernels | python3.8/site-packages/ray/_raylet.so) (rayworker pid=281502) frame #53: ray::core::coreworkerprocessimpl::runworkertaskexecutionloop() + 0x8c (0x7f503154025c in /root/miniconda3… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
