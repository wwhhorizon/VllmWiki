# vllm-project/vllm#17893: [Bug]: Regarding the CUDA error/no_thinking that occurred during pressure testing

| 字段 | 值 |
| --- | --- |
| Issue | [#17893](https://github.com/vllm-project/vllm/issues/17893) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;moe;quantization |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Regarding the CUDA error/no_thinking that occurred during pressure testing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```text During the model stress testing, using 256 concurrent threads and conducting 10 rounds of tests, the following error was reported when the test was nearly completed: INFO 05-09 16:18:30 [engine.py:310] Added request chatcmpl-2035ef7739b84f7e823caec00b0c5d7f. INFO 05-09 16:18:30 [engine.py:310] Added request chatcmpl-c4a6d3b158944c1895b0d2f0f9df02db. INFO 05-09 16:18:30 [engine.py:310] Added request chatcmpl-58f32d39b35c47d9b5d708a97e4aa010. [rank1]:[E509 16:18:30.801728316 ProcessGroupNCCL.cpp:1895] [PG ID 2 PG GUID 3 Rank 1] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at /pytorch/c10/cuda/CUDAException.cpp:43 (most recent call first): frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x96 (0x7f1192f6c1b6 in /usr/local/lib/python3.12/dist-packages/torch/l...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ight be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at /pytorch/c10/cuda/CUDAE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Regarding the CUDA error/no_thinking that occurred during pressure testing bug;stale ### Your current environment ### 🐛 Describe the bug ```text During the model stress testing, using 256 concurrent threads and c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: gnu/libc.so.6) terminate called after throwing an instance of 'c10::DistBackendError' what(): [PG ID 2 PG GUID 3 Rank 1] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Your current environment ### 🐛 Describe the bug ```text During the model stress testing, using 256 concurrent threads and conducting 10 rounds of tests, the following error was reported when the test was nearly complete...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ing the CUDA error/no_thinking that occurred during pressure testing bug;stale ### Your current environment ### 🐛 Describe the bug ```text During the model stress testing, using 256 concurrent threads and conducting 10...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #4: c10d::processgroupnccl::worknccl::iscompleted() + 0xa0 (0x7f11412228c0 in /usr/local/lib/python3.12/dist-… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x14d (0x7f11412256ed in /usr/local/lib/python3.12/dist-pack… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0x145c0 (0x7f119341a5c0 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorc… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
