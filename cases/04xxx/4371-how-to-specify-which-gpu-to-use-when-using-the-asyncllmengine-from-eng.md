# vllm-project/vllm#4371: How to specify which GPU to use when using the AsyncLLMEngine.from_engine_args method for inference

| 字段 | 值 |
| --- | --- |
| Issue | [#4371](https://github.com/vllm-project/vllm/issues/4371) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> How to specify which GPU to use when using the AsyncLLMEngine.from_engine_args method for inference

### Issue 正文摘录

Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.16.3 Libc version: glibc-2.31 Python version: 3.10.0 (default, Mar 3 2022, 09:58:08) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-5.4.0-177-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 Ti GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3090 GPU 4: NVIDIA GeForce RTX 3090 Nvidia driver version: 535.54.03 cuDNN version: Probably one of the following: /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn.so.8.5.0 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.5.0 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.5.0 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.5.0 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.5.0 /us...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: How to specify which GPU to use when using the AsyncLLMEngine.from_engine_args method for inference usage Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ine.from_engine_args method for inference usage Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Vulnerable Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and secco...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.18.1 [pip3] torch==2.1.2 [pip3] triton==2.1.0 [conda] galore-torch 1.0 pypi_0 pypi [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.18.1

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
