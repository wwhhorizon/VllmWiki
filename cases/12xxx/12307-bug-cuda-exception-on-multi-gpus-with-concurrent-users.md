# vllm-project/vllm#12307: [Bug]: CUDA Exception on multi-gpus with concurrent users

| 字段 | 值 |
| --- | --- |
| Issue | [#12307](https://github.com/vllm-project/vllm/issues/12307) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: CUDA Exception on multi-gpus with concurrent users

### Issue 正文摘录

### Your current environment vllm version `v0.6.1.post2` ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running llama3.1-70-awq on 4 A10 GPUs on vllm version `v0.6.1.post2` with `--max-model-len 4096 --gpu-memory-utilization 0.8 --tensor-parallel-size 4 --distributed-executor-backend mp` I send 20 1k-requests at the same time, and I got this error: ``` [rank0]:[E122 07:39:51.324142902 ProcessGroupNCCL.cpp:1515] [PG 3 Rank 0] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at ../c10/cuda/CUDAException.cpp:43 (most recent call first): frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x96 (0x7694d8d77f86 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so) frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::string const&) + 0x64 (0x7694d8d26d10 in /usr/local/lib...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: -gpus with concurrent users bug;stale ### Your current environment vllm version `v0.6.1.post2` ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running llama3.1-70-awq on 4 A10 GPUs on vllm version `v0.6....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA Exception on multi-gpus with concurrent users bug;stale ### Your current environment vllm version `v0.6.1.post2` ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running llama3.1-70-awq on 4 A...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: bug;stale ### Your current environment vllm version `v0.6.1.post2` ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running llama3.1-70-awq on 4 A10 GPUs on vllm version `v0.6.1.post2` with `--max-model-l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: u-memory-utilization 0.8 --tensor-parallel-size 4 --distributed-executor-backend mp` I send 20 1k-requests at the same time, and I got this error: ``` [rank0]:[E122 07:39:51.324142902 ProcessGroupNCCL.cpp:1515] [PG 3 Ra...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at ../c10/cuda/...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 0x94ac3 (0x7694e5924ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #4: clone + 0x44 (0x7694e59b5a04 in /usr/lib/x86_64-linux-gnu/libc.so.6) (vllmworkerprocess pid=108) warning… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x10c (0x76941478d6fc in /usr/local/lib/python3.10/dist-pack… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | /local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdc253 (0x7694e499c253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unkn… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
