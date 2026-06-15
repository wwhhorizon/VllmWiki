# vllm-project/vllm#4785: [Bug]: multi-gpu for baichuan2-13B-Chat benchmark_serving

| 字段 | 值 |
| --- | --- |
| Issue | [#4785](https://github.com/vllm-project/vllm/issues/4785) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: multi-gpu for baichuan2-13B-Chat benchmark_serving

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.35 Python version: 3.9.19 (main, May 6 2024, 19:43:03) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.2.0-36-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 GPU 2: NVIDIA GeForce RTX 4090 GPU 3: NVIDIA GeForce RTX 4090 GPU 4: NVIDIA GeForce RTX 4090 GPU 5: NVIDIA GeForce RTX 4090 GPU 6: NVIDIA GeForce RTX 4090 GPU 7: NVIDIA GeForce RTX 4090 Nvidia driver version: 525.147.05 cuDNN version: Probably one of the following: /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn.so.8 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_adv_train.so.8 /usr/l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ython collect_env.py` ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] triton==2.3.0 [pip3] vllm_nccl_cu11==2.18.1.0.4.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: multi-gpu for baichuan2-13B-Chat benchmark_serving bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is de...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
