# vllm-project/vllm#6153: 加载Baichuan2-13B-Chat时出异常，torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 50.00 MiB. GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#6153](https://github.com/vllm-project/vllm/issues/6153) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> 加载Baichuan2-13B-Chat时出异常，torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 50.00 MiB. GPU

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.31 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-156-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A40-24Q Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.2 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.2 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.2 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.2 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.2 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.2 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.2 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 加载Baichuan2-13B-Chat时出异常，torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 50.00 MiB. GPU usage;stale ### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: . GPU usage;stale ### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: fMemoryError: CUDA out of memory. Tried to allocate 50.00 MiB. GPU usage;stale ### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyT...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] transformers==4.42.3 [pip3] triton==2.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.0

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
