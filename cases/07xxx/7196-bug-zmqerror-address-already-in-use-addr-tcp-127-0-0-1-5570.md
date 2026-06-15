# vllm-project/vllm#7196: [Bug]: ZMQError: Address already in use (addr='tcp://127.0.0.1:5570')

| 字段 | 值 |
| --- | --- |
| Issue | [#7196](https://github.com/vllm-project/vllm/issues/7196) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ZMQError: Address already in use (addr='tcp://127.0.0.1:5570')

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: 10.0.0-4ubuntu1 CMake version: version 3.30.0 Libc version: glibc-2.31 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-187-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 10.1.243 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-32GB GPU 1: Tesla V100-SXM2-32GB GPU 2: Tesla V100-SXM2-32GB GPU 3: Tesla V100-SXM2-32GB GPU 4: Tesla V100-SXM2-32GB GPU 5: Tesla V100-SXM2-32GB GPU 6: Tesla V100-SXM2-32GB GPU 7: Tesla V100-SXM2-32GB Nvidia driver version: 535.183.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 64 On-line CPU(s) list: 0-63 Thread(s) per core: 2 Core(s) per socket: 16 Socket(s): 2 NUMA node(s): 2...

## 现有链接修复摘要

#41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #41859 Bump the minor-update group across 1 directory with 141 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: tcp://127.0.0.1:5570') bug ### Your current environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 10.1.243 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-32GB GPU 1: Tesla V100-SXM2-32GB GPU 2: Tesla V100-SXM2-32GB GPU 3: Tesla V100-SXM2-32GB GPU 4: T...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ransformers 4.43.3 pypi_0 pypi [conda] triton 2.3.1 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.4 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU To
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Mitigation; Enhanced IBRS Vulnerability Spec store bypass: Mitigation; Specu...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 140 updates | port. (<a href="https://redirect.github.com/psf/requests/issues/7196">#7196</a>)</li> </ul> <p><strong>Documentation</strong></p> <ul> <li>Various typo fixes and doc improvements.… |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | port. (<a href="https://redirect.github.com/psf/requests/issues/7196">#7196</a>)</li> </ul> <p><strong>Documentation</strong></p> <ul> <li>Various typo fixes and doc improvements.… |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | port. (<a href="https://redirect.github.com/psf/requests/issues/7196">#7196</a>)</li> </ul> <p><strong>Documentation</strong></p> <ul> <li>Various typo fixes and doc improvements.… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
