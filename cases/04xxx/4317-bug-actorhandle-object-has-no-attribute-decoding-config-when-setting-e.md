# vllm-project/vllm#4317: [Bug]: 'ActorHandle' object has no attribute 'decoding_config' when setting `--engine-use-ray`

| 字段 | 值 |
| --- | --- |
| Issue | [#4317](https://github.com/vllm-project/vllm/issues/4317) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 'ActorHandle' object has no attribute 'decoding_config' when setting `--engine-use-ray`

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.10.14 (main, Mar 21 2024, 16:24:04) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-91-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L20 GPU 1: NVIDIA L20 GPU 2: NVIDIA L20 GPU 3: NVIDIA L20 GPU 4: NVIDIA L20 GPU 5: NVIDIA L20 GPU 6: NVIDIA L20 GPU 7: NVIDIA L20 Nvidia driver version: 550.54.14 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.6.0 HIP runtime version...

## 现有链接修复摘要

#4335 [Bugfix][Core] Fix get decoding config from ray

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ing `--engine-use-ray` bug ### Your current environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: 'ActorHandle' object has no attribute 'decoding_config' when setting `--engine-use-ray` bug ### Your current environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Unknown: No mitigations Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: Mit...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.19.3 [pip3] torch==2.2.1 [pip3] triton==2.2.0 [pip3] vllm-nccl-cu12==2.18.1.0.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.19.3 pypi_0 pypi [conda] torch

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4335](https://github.com/vllm-project/vllm/pull/4335) | closes_keyword | 0.95 | [Bugfix][Core] Fix get decoding config from ray | FIX #4317 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering do |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
