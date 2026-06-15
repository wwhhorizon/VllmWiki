# vllm-project/vllm#27430: [Bug]: vLLM (TP=8) on 235B model triggers "CUDA error: unspecified launch failure" and persistent "ERR!" state in nvidia-smi

| 字段 | 值 |
| --- | --- |
| Issue | [#27430](https://github.com/vllm-project/vllm/issues/27430) |
| 状态 | open |
| 标签 | bug;stale;nvidia |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: vLLM (TP=8) on 235B model triggers "CUDA error: unspecified launch failure" and persistent "ERR!" state in nvidia-smi

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running the vLLM API server with a very large model (`Qwen3-VL-235B-A22B-Instruct`) using 8-way tensor parallelism. The server starts and can successfully process some requests. However, after a period of operation (or when handling a specific request), the service encounters a catastrophic CUDA error and crashes the entire engine. ### The Crash The failure sequence is as follows: 1. The first critical error appears from `rank4`: `[rank4]:[E1023 17:16:46.022239569 ProcessGroupNCCL.cpp:2068] ... Process group watchdog thread terminated with exception: CUDA error: unspecified launch failure`. This originates from `ProcessGroupNCCL`. 2. The API server immediately begins returning `500 Internal Server Error` to all incoming requests. 3. Approximately 60 seconds later, the `EngineCore` reports a timeout from the shared memory broadcast: `shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds.` 4. This is immediately followed by the error: `ERROR ... [multiproc_executor.py:154] Worker proc VllmWorker-4 died unexpectedly, shutting down executor.` 5. All other workers then terminate (`Parent process exi...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vLLM (TP=8) on 235B model triggers "CUDA error: unspecified launch failure" and persistent "ERR!" state in nvidia-smi bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug I am running the vLLM API...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: vLLM (TP=8) on 235B model triggers "CUDA error: unspecified launch failure" and persistent "ERR!" state in nvidia-smi bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug I am running the vLLM API...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vLLM (TP=8) on 235B model triggers "CUDA error: unspecified launch failure" and persistent "ERR!" state in nvidia-smi bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug I am running the vLLM API...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: nspecified launch failure" and persistent "ERR!" state in nvidia-smi bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug I am running the vLLM API server with a very large model (`Qwen3-VL-235B-A22B-Ins...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: uantization;scheduler_memory cache;cuda;kernel;moe;operator;quantization;triton build_error;crash;mismatch;slowdown dtype;env_dependency;memory_layout;shape #4 Use FlashAttention for `multi_query_kv_attention` | #6 Auto...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | qwenvl/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #4: c10d::processgroupnccl::watchdog::runloop() + 0x978 (0x7f6bc76d6f48 in /home/lt_08321/miniconda3/envs/qwe… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | qwenvl/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xdbbf4 (0x7f6bab05abf4 in /home/lt_08321/miniconda3/envs/qwenvl/bin/../lib/libstdc+… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | home/lt_08321/miniconda3/envs/qwenvl/bin/../lib/libstdc++.so.6) frame #7: <unknown function> + 0x94ac3 (0x7f6c24e63ac3 in /lib/x86_64-linux-gnu/libc.so.6) frame #8: clone + 0x44 (… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
