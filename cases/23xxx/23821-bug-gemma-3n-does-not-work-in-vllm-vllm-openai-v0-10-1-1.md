# vllm-project/vllm#23821: [Bug]: Gemma 3n does not work in vllm/vllm-openai:v0.10.1.1

| 字段 | 值 |
| --- | --- |
| Issue | [#23821](https://github.com/vllm-project/vllm/issues/23821) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Gemma 3n does not work in vllm/vllm-openai:v0.10.1.1

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 4 2025, 08:56:18) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.14.0-503.35.1.el9_5.x86_64-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA L40S Nvidia driver version : 570.124.06 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Archite...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Cou
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma 3n does not work in vllm/vllm-openai:v0.10.1.1 bug;stale ### Your current environment Collecting environment information...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Gemma 3n does not work in vllm/vllm-openai:v0.10.1.1 bug;stale ### Your current environment Collecting environment information...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: u128 [pip3] torchvision==0.22.1+cu128 [pip3] transformers==4.55.2 [pip3] triton==3.3.1 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect N...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23826: Should have ROCm label: NO (0 matches) #23821: Should have ROCm label: NO (0 matches) #23820: Should have ROCm label: NO (0 matches) #23816: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
