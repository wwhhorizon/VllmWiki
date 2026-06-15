# vllm-project/vllm#6550: [Usage]: How to invoke all the tests in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#6550](https://github.com/vllm-project/vllm/issues/6550) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to invoke all the tests in vLLM

### Issue 正文摘录

### Your current environment ```text GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.31 Python version: 3.10.14 (main, Apr 6 2024, 18:45:05) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-6.2.0-26-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB Nvidia driver version: 525.125.06 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.0 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 48 bits physical, 48...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: the tests in vLLM usage;stale ### Your current environment ```text GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.31 Python versio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: untime) Python platform: Linux-6.2.0-26-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB Nvidi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: How to invoke all the tests in vLLM usage;stale ### Your current environment ```text GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc versio...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.3.0 [pip3] torchvision==0.18.0 [pip3] transformers==4.42.3 [pip3] triton==2.3.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.0.post1 vLLM Build Flags: CUDA A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
