# vllm-project/vllm#6103: [Bug]: fused_moe_kernel compile bug

| 字段 | 值 |
| --- | --- |
| Issue | [#6103](https://github.com/vllm-project/vllm/issues/6103) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: fused_moe_kernel compile bug

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.26.0 Libc version: glibc-2.31 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-107-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800 80GB PCIe GPU 1: NVIDIA A800 80GB PCIe GPU 2: NVIDIA A800 80GB PCIe GPU 3: NVIDIA A800 80GB PCIe GPU 4: NVIDIA A800 80GB PCIe GPU 5: NVIDIA A800 80GB PCIe GPU 6: NVIDIA A800 80GB PCIe GPU 7: NVIDIA A800 80GB PCIe Nvidia driver version: 550.54.15 cuDNN version: Probably one of the following: /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn.so.8.9.6 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.6 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.6 /usr/local/cuda-12.1/targets/x86_64-linux/lib/lib...

## 现有链接修复摘要

#5036 [Kernel][RFC] Refactor the punica kernel based on Triton | #6140 [Bugfix] Add custom Triton cache manager to resolve MoE MP issue

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: fused_moe_kernel compile bug bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build P...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: e bug bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rch==2.3.0 [pip3] torchvision==0.18.0 [pip3] transformers==4.42.1 [pip3] triton==2.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.0

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5036](https://github.com/vllm-project/vllm/pull/5036) | mentioned | 0.45 | [Kernel][RFC] Refactor the punica kernel based on Triton | of # nvlinks ``` ### 🐛 describe the bug ## description #5036 will raise the following error when using tp>1. similar issues also persisted when i tested the qwen1.5-moe m |
| [#6140](https://github.com/vllm-project/vllm/pull/6140) | closes_keyword | 0.95 | [Bugfix] Add custom Triton cache manager to resolve MoE MP issue  | Fixes #6103 We have been using this fix via our fork (see [here](https://github.com/IBM/vllm/pull/35/files)) for a while and it seems stable. ~~Note, this will only resolve |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
