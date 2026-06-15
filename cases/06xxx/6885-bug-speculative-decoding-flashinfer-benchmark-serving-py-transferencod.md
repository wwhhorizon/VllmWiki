# vllm-project/vllm#6885: [Bug]: Speculative Decoding + FlashInfer + benchmark_serving.py TransferEncodingError ISSUE

| 字段 | 值 |
| --- | --- |
| Issue | [#6885](https://github.com/vllm-project/vllm/issues/6885) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;moe;operator;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative Decoding + FlashInfer + benchmark_serving.py TransferEncodingError ISSUE

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-72-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.5.40 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.183.01 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops.so.9.1.0 HIP runtime version: N/A MIOpen runtime version...

## 现有链接修复摘要

#6926 [SpecDecode] Support FlashInfer in DraftModelRunner

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Your current environment Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Speculative Decoding + FlashInfer + benchmark_serving.py TransferEncodingError ISSUE bug ### Your current environment Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: Speculative Decoding + FlashInfer + benchmark_serving.py TransferEncodingError ISSUE bug ### Your current environment Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: Speculative Decoding + FlashInfer + benchmark_serving.py TransferEncodingError ISSUE bug ### Your current environment Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6926](https://github.com/vllm-project/vllm/pull/6926) | closes_keyword | 0.95 | [SpecDecode] Support FlashInfer in DraftModelRunner | FIX #6885 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** This PR resolves the `benchmark_serving.py` error for Speculative Decoding |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
