# vllm-project/vllm#40800: [Bug]: DeepSeek V4 intermittently leaks DSML fragments in auto + streaming mode, causing unstable tool-call parsing

| 字段 | 值 |
| --- | --- |
| Issue | [#40800](https://github.com/vllm-project/vllm/issues/40800) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V4 intermittently leaks DSML fragments in auto + streaming mode, causing unstable tool-call parsing

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main, Mar 4 2026, 09:23:07) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.15.0-119-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H20-3e GPU 1: NVIDIA H20-3e GPU 2: NVIDIA H20-3e GPU 3: NVIDIA H20-3e GPU 4: NVIDIA H20-3e GPU 5: NVIDIA H20-3e GPU 6: NVIDIA H20-3e GPU 7: NVIDIA H20-3e Nvidia driver version : 575.57.08 cuDNN version : Could not collect HIP runtime version : N/A M...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: DeepSeek V4 intermittently leaks DSML fragments in auto + streaming mode, causing unstable tool-call parsing bug ### Your current environment ============================== System Info ===========================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.8.post1 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.9.1.4 [pip3] nvidia-cuda-cupti-cu12==12.9.79 [pip3] nvidia-cuda-n...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: rch version : 2.11.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ====================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: DA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H20-3e GPU 1: NVIDIA H20-3e GPU 2: NVIDIA H20-3e GPU 3: NVIDIA H20-3e GPU 4: NVIDIA H20-3e GPU 5: NVIDIA H20-3e GPU...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
