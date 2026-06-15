# vllm-project/vllm#20410: [Usage]: Does vllm support NVFP4 deepseek-R1?

| 字段 | 值 |
| --- | --- |
| Issue | [#20410](https://github.com/vllm-project/vllm/issues/20410) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Does vllm support NVFP4 deepseek-R1?

### Issue 正文摘录

### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0a0+5228986c39.nv25.06 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, May 26 2025, 18:50:19) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.8.0-1021-nvidia-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA B200 GPU 1: NVIDIA B200 GPU 2: NVIDIA B200 GPU 3: NVIDIA B200 GPU 4: NVIDIA B200 GPU 5: NVIDIA B200 GPU 6: NVIDIA B200 GPU 7: NVIDIA B200 Nvidia driver version : 580.40 cuDNN version : Probably one of the following: /us...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : Could not collect Libc version : glibc-2.39 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: : 2.8.0a0+5228986c39.nv25.06 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: Does vllm support NVFP4 deepseek-R1? usage ### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: R1? usage ### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affecte...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
