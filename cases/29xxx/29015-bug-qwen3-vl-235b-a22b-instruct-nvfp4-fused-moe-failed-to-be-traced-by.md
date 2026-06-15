# vllm-project/vllm#29015: [Bug]: Qwen3-VL-235B-A22B-Instruct-NVFP4 fused moe failed to be traced by torch dynamo

| 字段 | 值 |
| --- | --- |
| Issue | [#29015](https://github.com/vllm-project/vllm/issues/29015) |
| 状态 | closed |
| 标签 | bug;nvidia |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-235B-A22B-Instruct-NVFP4 fused moe failed to be traced by torch dynamo

### Issue 正文摘录

### Your current environment - The output of python collect_env.py ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.2 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (main, Oct 31 2025, 23:00:46) [Clang 21.1.4 ] (64-bit runtime) Python platform : Linux-6.8.0-1028-nvidia-64k-aarch64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.48 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GB200 GPU 1: NVIDIA GB200 GPU 2: NVIDIA GB200 GPU 3: NVIDIA GB200 Nvidia driver version : 580.95.05 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNN...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ======== OS : Ubuntu 24.04.2 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.2 Libc version : glibc-2.39 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ==================== OS : Ubuntu 24.04.2 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.2 Libc version : glibc-2.39 ======
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Qwen3-VL-235B-A22B-Instruct-NVFP4 fused moe failed to be traced by torch dynamo bug;nvidia ### Your current environment - The output of python collect_env.py ```text Collecting environment information... ========...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.2 [pip3] numpy==2.2.6 [pip3] nvidia-cublas==13.0.0.19 [pip3] nvidia-cuda-cupti==13.0.48 [pip3] nvidia-cuda-nvrtc==13.0.48 [...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-VL-235B-A22B-Instruct-NVFP4 fused moe failed to be traced by torch dynamo bug;nvidia ### Your current environment - The output of python collect_env.py ```text Collecting environment information... ========...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
