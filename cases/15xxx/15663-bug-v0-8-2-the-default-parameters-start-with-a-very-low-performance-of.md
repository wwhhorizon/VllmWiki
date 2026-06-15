# vllm-project/vllm#15663: [Bug]: v0.8.2 The default parameters start with a very low performance of 9.8 tokens/s with deepseek-r1:671b

| 字段 | 值 |
| --- | --- |
| Issue | [#15663](https://github.com/vllm-project/vllm/issues/15663) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.8.2 The default parameters start with a very low performance of 9.8 tokens/s with deepseek-r1:671b

### Issue 正文摘录

### Your current environment ``` root@vllm-0:~# vi collect_env.py root@vllm-0:~# python3 collect_env.py INFO 03-28 09:50:00 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.31.6 Libc version: glibc-2.35 Python version: 3.12.9 (main, Feb 5 2025, 08:49:00) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-126-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver version: 560.35.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ly detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: py INFO 03-28 09:50:00 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: async abort: Not affected Versions of relevant libraries: [pip3] flashinfer-python==0.2.1.post2+cu124torch2.6 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rt with a very low performance of 9.8 tokens/s with deepseek-r1:671b bug;stale ### Your current environment ``` root@vllm-0:~# vi collect_env.py root@vllm-0:~# python3 collect_env.py INFO 03-28 09:50:00 [__init__.py:239...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
