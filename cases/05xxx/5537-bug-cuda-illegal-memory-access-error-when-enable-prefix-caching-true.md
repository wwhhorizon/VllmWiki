# vllm-project/vllm#5537: [Bug]: CUDA illegal memory access error when `enable_prefix_caching=True`

| 字段 | 值 |
| --- | --- |
| Issue | [#5537](https://github.com/vllm-project/vllm/issues/5537) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: CUDA illegal memory access error when `enable_prefix_caching=True`

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.31 Python version: 3.11.9 (main, Apr 6 2024, 17:59:24) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-5.15.0-107-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 GPU 2: NVIDIA RTX A6000 GPU 3: NVIDIA RTX A6000 GPU 4: NVIDIA RTX A6000 GPU 5: NVIDIA RTX A6000 GPU 6: NVIDIA RTX A6000 GPU 7: NVIDIA RTX A6000 Nvidia driver version: 535.161.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 43 bits physical, 48 bits virtual CPU(s): 256 On-line CPU(s) list: 0-254 Off-line CPU(s) list: 255 Thread(s) per core: 1 Core(s)...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text The output of `python collect_env.py` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: CUDA illegal memory access error when `enable_prefix_caching=True` bug;stale ### Your current environment ```text The output of `python collect_env.py` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.41.1 [pip3] triton==2.3.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.0.post1 vLLM Build Flags: CUDA A...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 GPU 2: NVIDIA RTX A6000 GPU 3: NVIDIA RTX A6000 GPU 4: NVIDIA RTX A6000 G...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: : CUDA illegal memory access error when `enable_prefix_caching=True` bug;stale ### Your current environment ```text The output of `python collect_env.py` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to b...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | xtral-20240612-2-1 \| esc[36m(rayworkerwrapper pid=14390)esc[0m frame #4: clone + 0x43 (0x7fec92cef353 in /usr/lib/x86_64-linux-gnu/libc.so.6) llm-inference-mixtral-20240612-2-1 \| |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | xtral-20240612-2-1 \| esc[36m(rayworkerwrapper pid=14390)esc[0m frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x10c (0x7fbcd598331c in /usr/local/lib/python3.11/dist-packa… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | xtral-20240612-2-1 \| esc[36m(rayworkerwrapper pid=14390)esc[0m frame #7: <unknown function> + 0xd6df4 (0x7fec90c95df4 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) llm-inference-mix |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
