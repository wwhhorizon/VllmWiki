# vllm-project/vllm#41702: [Usage]:  ValueError: mismatch of LoRA layer names for Gemma4 E2B trained with unsloth

| 字段 | 值 |
| --- | --- |
| Issue | [#41702](https://github.com/vllm-project/vllm/issues/41702) |
| 状态 | open |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]:  ValueError: mismatch of LoRA layer names for Gemma4 E2B trained with unsloth

### Issue 正文摘录

### Your current environment ```text Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Mar 23 2026, 19:04:32) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.8.0-107-generic-x86_64-with-glibc2.39 Is CUDA available : True 08:29:20 [90/140] CUDA runtime version : 13.2.51 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 GPU 2: NVIDIA GeForce RTX 4090 GPU 3: NVIDIA GeForce RTX 4090 Nvidia driver version : 575.51.03 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.7 /usr/lib/x86_64-linux-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could n
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: ValueError: mismatch of LoRA layer names for Gemma4 E2B trained with unsloth usage ### Your current environment ```text Collecting environment information...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: ValueError: mismatch of LoRA layer names for Gemma4 E2B trained with unsloth usage ### Your current environment ```text Collecting environment information...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [pip3] flashinfer-python==0.6.8.post1 [pip3] numpy==2.3.5
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ValueError: mismatch of LoRA layer names for Gemma4 E2B trained with unsloth usage ### Your current environment ```text Collecting environment information...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
