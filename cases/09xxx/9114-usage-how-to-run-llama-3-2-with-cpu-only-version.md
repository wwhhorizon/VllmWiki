# vllm-project/vllm#9114: [Usage]: How to run llama 3.2 with CPU only version

| 字段 | 值 |
| --- | --- |
| Issue | [#9114](https://github.com/vllm-project/vllm/issues/9114) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to run llama 3.2 with CPU only version

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 10-07 03:01:24 _core_ext.py:180] Failed to import from vllm._core_C with ImportError('libtorch_cuda.so: cannot open shared object file: No such file or directory') WARNING 10-07 03:01:24 _core_ext.py:180] Failed to import from vllm._core_C with ImportError('libtorch_cuda.so: cannot open shared object file: No such file or directory') PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.4 Libc version: glibc-2.35 Python version: 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-122-generic-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 Nvidia driver version: 560.35.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcu...

## 现有链接修复摘要

#9089 [Hardware][CPU] Cross-attention and Encoder-Decoder models support on CPU backend

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Usage]: How to run llama 3.2 with CPU only version usage ### Your current environment ```text Collecting environment information... WARNING 10-07 03:01:24 _core_ext.py:180] Failed to import from vllm._core_C with Impor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: xt.py:180] Failed to import from vllm._core_C with ImportError('libtorch_cuda.so: cannot open shared object file: No such file or directory') WARNING 10-07 03:01:24 _core_ext.py:180] Failed to import from vllm._core_C w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: How to run llama 3.2 with CPU only version usage ### Your current environment ```text Collecting environment information... WARNING 10-07 03:01:24 _core_ext.py:180] Failed to import from vllm._core_C with Impor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Mitigation; Clear Register File Vulnerability Retbleed: Not affected Vulnerability Spec rstack ov...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: .0+cpu [pip3] torchvision==0.19.0+cpu [pip3] transformers==4.45.1 [pip3] triton==2.2.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A vLLM Build Flags: CUDA Archs: No...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9089](https://github.com/vllm-project/vllm/pull/9089) | closes_keyword | 0.95 | [Hardware][CPU] Cross-attention and Encoder-Decoder models support on CPU backend | FIX #9114 - Add cross-attention support for SDPA backend. - Add Encoder-Decoder models support for CPU backend. **TODO** - [x] Clean up the code - [x] Enable bart test for C |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
