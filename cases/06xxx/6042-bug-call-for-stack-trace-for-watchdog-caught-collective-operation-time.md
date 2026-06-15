# vllm-project/vllm#6042: [Bug]: call for stack trace for "Watchdog caught collective operation timeout"

| 字段 | 值 |
| --- | --- |
| Issue | [#6042](https://github.com/vllm-project/vllm/issues/6042) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;moe |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: call for stack trace for "Watchdog caught collective operation timeout"

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug We received quite a lot report about "Watchdog caught collective operation timeout", which is flaky and difficult to reproduce. It happens after running for some time. To analyze the error, we need to collect enough stack trace. If you encounter a similar problem, please paste enough stack trace for us to debug. Example: https://buildkite.com/vllm/ci-aws/builds/3548#01906e81-54c6-4713-beb7-d08f3c873200 caught one such error. Please include the first line of error, together with the Python stack trace. In the following example, it seems one process has illegal memory access. It dies, but the rest process is still in allreduce, and is waiting for it, causing the timeout problem. From the python level stack trace, it happens when we profile the run, and it seems to be related with moe layer. ```text [rank3]:[E ProcessGroupNCCL.cpp:1414] [PG 2 Rank 3] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered -- | CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. |...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: blem, please paste enough stack trace for us to debug. Example: https://buildkite.com/vllm/ci-aws/builds/3548#01906e81-54c6-4713-beb7-d08f3c873200 caught one such error. Please include the first line of error, together...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ] [PG 2 Rank 3] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered -- | CUDA kernel errors might be asynchronously reported at some other API call, so the stack...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: l for stack trace for "Watchdog caught collective operation timeout" bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug We received quite a lot report about "...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: e timeout problem. From the python level stack trace, it happens when we profile the run, and it seems to be related with moe layer. ```text [rank3]:[E ProcessGroupNCCL.cpp:1414] [PG 2 Rank 3] Process group watchdog thr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: so.6) | | terminate called after throwing an instance of 'c10::DistBackendError' | what(): [PG 2 Rank 3] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered | CU...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | c3 (0x7f9f821e3ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) \| frame #4: <unknown function> + 0x126850 (0x7f9f82275850 in /usr/lib/x86_64-linux-gnu/libc.so.6) \| \| fatal pyth |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | c3 (0x7f9f821e3ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) \| frame #6: <unknown function> + 0x126850 (0x7f9f82275850 in /usr/lib/x86_64-linux-gnu/libc.so.6) \| \| exception |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | l/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) \| frame #7: <unknown function> + 0xdc253 (0x7fd5c76b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) \| frame #8: <un |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
