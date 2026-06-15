# vllm-project/vllm#21986: [Bug]: There is an issue with speculative inference in Eagle mode, where the context length of vLLM inference is constrained by the draft model.

| 字段 | 值 |
| --- | --- |
| Issue | [#21986](https://github.com/vllm-project/vllm/issues/21986) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: There is an issue with speculative inference in Eagle mode, where the context length of vLLM inference is constrained by the draft model.

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.0.2 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.10 (main, Apr 9 2025, 08:55:05) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.15.0-50-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20 ============================== CPU Info ============================== Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 208 On-line CPU(s) list: 0-207 Flags...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.0.2 Libc version : glibc-2.35 ==================
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: There is an issue with speculative inference in Eagle mode, where the context length of vLLM inference is constrained by the draft model. bug;stale ### Your current environment Collecting environment information....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.10 (...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: orch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: , where the context length of vLLM inference is constrained by the draft model. bug;stale ### Your current environment Collecting environment information... ============================== System Info ===================...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #4: <unknown function> + 0x102ee8b (0x7fe595c44e8b in /usr/local/lib/python3.12/dist-packages/torch/lib/libto… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0x44d2a2 (0x7fe5e2dc82a2 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtor… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | ocal/lib/python3.12/dist-packages/torch/lib/libtorch_python.so) frame #7: c10::tensorimpl::~tensorimpl() + 0x9 (0x7fe5eb352f39 in /usr/local/lib/python3.12/dist-packages/torch/lib… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | on3.12() [0x59be14] frame #11: /usr/bin/python3.12() [0x57ccc0] frame #12: /usr/bin/python3.12() [0x57bcf6] frame #13: /usr/bin/python3.12() [0x57bcef] frame #14: /usr/bin/python3… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | on3.12() [0x57bcef] frame #15: /usr/bin/python3.12() [0x57bcef] frame #16: /usr/bin/python3.12() [0x57bcef] frame #17: /usr/bin/python3.12() [0x57bcef] frame #18: /usr/bin/python3… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | on3.12() [0x57bcef] frame #19: /usr/bin/python3.12() [0x57bcef] frame #20: /usr/bin/python3.12() [0x57bcef] frame #21: /usr/bin/python3.12() [0x57bcef] frame #22: /usr/bin/python3… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | on3.12() [0x57bcef] frame #20: /usr/bin/python3.12() [0x57bcef] frame #21: /usr/bin/python3.12() [0x57bcef] frame #22: /usr/bin/python3.12() [0x57bcef] frame #23: /usr/bin/python3… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | on3.12() [0x57bcef] frame #26: /usr/bin/python3.12() [0x57bcef] frame #27: /usr/bin/python3.12() [0x57bcef] frame #28: /usr/bin/python3.12() [0x57bcef] frame #29: /usr/bin/python3… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | on3.12() [0x57bcef] frame #28: /usr/bin/python3.12() [0x57bcef] frame #29: /usr/bin/python3.12() [0x594cd7] frame #30: _pyeval_evalframedefault + 0x50e7 (0x54cb27 in /usr/bin/pyth… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | e #31: pyeval_evalcode + 0x99 (0x61d5b9 in /usr/bin/python3.12) frame #32: /usr/bin/python3.12() [0x6591db] frame #33: /usr/bin/python3.12() [0x654346] frame #34: pyrun_stringflag… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
