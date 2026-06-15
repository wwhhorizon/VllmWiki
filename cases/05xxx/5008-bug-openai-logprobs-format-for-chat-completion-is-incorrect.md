# vllm-project/vllm#5008: [Bug]: OpenAI LogProbs format for Chat-Completion is incorrect

| 字段 | 值 |
| --- | --- |
| Issue | [#5008](https://github.com/vllm-project/vllm/issues/5008) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OpenAI LogProbs format for Chat-Completion is incorrect

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.8.18 (default, Oct 2 2023, 15:02:11) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-5.15.0-101-generic-x86_64-with-glibc2.2.5 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 Nvidia driver version: 545.23.08 cuDNN version: Probably one of the following: /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn.so.8.9.5 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.5 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.5 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.9.5 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.9.5 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8...

## 现有链接修复摘要

#5029 [BUGFIX] [FRONTEND] Correct chat logprobs | #5032 [FRONTEND] OpenAI `tools` support named functions

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: OpenAI LogProbs format for Chat-Completion is incorrect bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Mitigation; IBRS Vulnerability Spec rstack overflow: Not affected Vulnerabil...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: numpy==1.24.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] triton==2.3.0 [pip3] vllm-nccl-cu12==2.18.1.0.2.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5029](https://github.com/vllm-project/vllm/pull/5029) | closes_keyword | 0.95 | [BUGFIX] [FRONTEND] Correct chat logprobs | FIX #5008 – correct `logprobs` format **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> se |
| [#5032](https://github.com/vllm-project/vllm/pull/5032) | closes_keyword | 0.95 | [FRONTEND] OpenAI `tools` support named functions | FIX #1869 (and #5008) -- only named tools **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
