# vllm-project/vllm#18483: [Usage]: Unrecognized argument --enable-prompt-embeds during Online inferencing

| 字段 | 值 |
| --- | --- |
| Issue | [#18483](https://github.com/vllm-project/vllm/issues/18483) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Unrecognized argument --enable-prompt-embeds during Online inferencing

### Issue 正文摘录

### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.0.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (main, Feb 4 2025, 14:57:36) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.8.0-1027-aws-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.6.85 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A10G Nvidia driver version : 570.133.20 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: sage]: Unrecognized argument --enable-prompt-embeds during Online inferencing usage;stale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 22.04....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: untime version : 12.6.85 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A10G Nvidia driver version : 570.133.20 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cognized argument --enable-prompt-embeds during Online inferencing usage;stale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: orch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
