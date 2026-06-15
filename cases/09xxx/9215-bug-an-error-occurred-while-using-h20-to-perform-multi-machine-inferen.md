# vllm-project/vllm#9215: [Bug]: An error occurred while using H20 to perform multi machine inference 405B through the ray cluster, causing inference to crash.

| 字段 | 值 |
| --- | --- |
| Issue | [#9215](https://github.com/vllm-project/vllm/issues/9215) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: An error occurred while using H20 to perform multi machine inference 405B through the ray cluster, causing inference to crash.

### Issue 正文摘录

### Your current environment ### Model Input Dumps There are no relevant files, but I have captured the relevant error call stack logs: ``` INFO 10-10 00:24:11 async_llm_engine.py:174] Added request cmpl-ea7ce76a97a84141911213d6779c3f25-0. end] via NET/IBext/0/GDRDMA VM-16-5-centos:39923:78857 [0] NCCL INFO Channel 07/0 : 0[0] -> 8[0] [send] via NET/IBext/0/GDRDMA VM-16-5-centos:39923:78857 [0] NCCL INFO Channel 09/0 : 0[0] -> 8[0] [send] via NET/IBext/0/GDRDMA VM-16-5-centos:39923:78857 [0] NCCL INFO Channel 10/0 : 0[0] -> 8[0] [send] via NET/IBext/0/GDRDMA VM-16-5-centos:39923:78857 [0] NCCL INFO Channel 11/0 : 0[0] -> 8[0] [send] via NET/IBext/0/GDRDMA VM-16-5-centos:39923:78857 [0] NCCL INFO Channel 12/0 : 0[0] -> 8[0] [send] via NET/IBext/0/GDRDMA VM-16-5-centos:39923:78857 [0] NCCL INFO Channel 13/0 : 0[0] -> 8[0] [send] via NET/IBext/0/GDRDMA VM-16-5-centos:39923:78857 [0] NCCL INFO Channel 14/0 : 0[0] -> 8[0] [send] via NET/IBext/0/GDRDMA VM-16-5-centos:39923:78857 [0] NCCL INFO Channel 15/0 : 0[0] -> 8[0] [send] via NET/IBext/0/GDRDMA VM-16-5-centos:39923:78857 [0] NCCL INFO Connected NVLS tree VM-16-5-centos:39923:78857 [0] NCCL INFO threadThresholds 8/8/64 | 128/8/64 |...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 24:11,686 E 39923 41512] logging.cc:108: Unhandled exception: N3c1016DistBackendErrorE. what(): [PG 3 Rank 0] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ight be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at ../c10/cuda/CUDAExcepti...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: inference 405B through the ray cluster, causing inference to crash. bug;stale ### Your current environment ### Model Input Dumps There are no relevant files, but I have captured the relevant error call stack logs: ``` I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: -5-centos:39923:78857 [0] NCCL INFO comm 0x56501150c320 rank 0 nranks 16 cudaDev 0 nvmlDev 0 busId 3000 commId 0x1c6daa4f776f8e93 - Init COMPLETE VM-16-5-centos:39923:78896 [0] NCCL INFO Channel 08/1 : 15[7] -> 0[0] [re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: using inference to crash. bug;stale ### Your current environment ### Model Input Dumps There are no relevant files, but I have captured the relevant error call stack logs: ``` INFO 10-10 00:24:11 async_llm_engine.py:174...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | x94ac3 (0x7f8ef10a6ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #4: <unknown function> + 0x126850 (0x7f8ef1138850 in /usr/lib/x86_64-linux-gnu/libc.so.6) error 10-10 00:24:1 |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x10c (0x7f8ea1d616fc in /usr/local/lib/python3.10/dist-packa… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdc253 (0x7f8eef4b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unknow |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
