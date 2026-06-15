# vllm-project/vllm#28669: vLLM 0.11.0 CUDA Library Mismatch on ARM64 with CUDA 13.x

| 字段 | 值 |
| --- | --- |
| Issue | [#28669](https://github.com/vllm-project/vllm/issues/28669) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vLLM 0.11.0 CUDA Library Mismatch on ARM64 with CUDA 13.x

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.31.2 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cpu Is debug build : False CUDA used to build PyTorch : Could not collect ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:17:47) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.11.0-1016-nvidia-aarch64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : N/A GPU models and configuration : GPU 0: NVIDIA GB10 Nvidia driver version : 580.95.05 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ====...

## 现有链接修复摘要

#41746 [Bugfix] find_loaded_library: skip stub libraries and continue iterating

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: vLLM 0.11.0 CUDA Library Mismatch on ARM64 with CUDA 13.x installation;stale ### Your current environment Collecting environment information... ============================== System Info ============================== O...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: vLLM 0.11.0 CUDA Library Mismatch on ARM64 with CUDA 13.x installation;stale ### Your current environment Collecting environment information... ============================== System Info ============================== OS
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nstallation;stale ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (aarch64) GCC version : (Ubuntu 13.3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: vLLM 0.11.0 CUDA Library Mismatch on ARM64 with CUDA 13.x installation;stale ### Your current environment Collecting environment information... ============================== System Info ============================== O...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: p sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh bti ecv afp wfxt Model name: Cortex-A725 Model: 1 Thread(s) per core: 1 Core(s) per socket: 10 Socket(s):

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41746](https://github.com/vllm-project/vllm/pull/41746) | mentioned | 0.6 | [Bugfix] find_loaded_library: skip stub libraries and continue iterating | `libcudart` in the filename triggers the same trap. Related issues: #28669 (CUDA library mismatch on ARM64 + CUDA 13.x — different failure mode but adjacent class), #39923 (broken… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
