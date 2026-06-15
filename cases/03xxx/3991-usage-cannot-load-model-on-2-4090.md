# vllm-project/vllm#3991: [Usage]: Cannot load model on 2 4090 

| 字段 | 值 |
| --- | --- |
| Issue | [#3991](https://github.com/vllm-project/vllm/issues/3991) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Cannot load model on 2 4090 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.29.0 Libc version: glibc-2.31 Python version: 3.9.19 (main, Mar 21 2024, 17:11:28) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-78-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 11.3.109 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.2.0 HIP runtime version: N/A MIOpen runtime version: N/A Is XNN...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: t environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: n collect_env.py` ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Cannot load model on 2 4090 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM us...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Cannot load model on 2 4090 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM us...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 1.26.4 [pip3] torch==2.1.2+cu121 [pip3] torchvision==0.16.2+cu121 [pip3] triton==2.1.0 [conda] blas 1.0 mkl defaults [conda] cudatoolkit 11.8.0 h6a678d5_0 defaults [conda] ffmpeg 4.3

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
