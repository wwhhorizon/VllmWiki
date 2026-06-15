# vllm-project/vllm#35845: [Bug]: llm serve "Qwen/Qwen3.5-27B"     --quantization bitsandbytes

| 字段 | 值 |
| --- | --- |
| Issue | [#35845](https://github.com/vllm-project/vllm/issues/35845) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: llm serve "Qwen/Qwen3.5-27B"     --quantization bitsandbytes

### Issue 正文摘录

### Your current environment The output of python collect_env.py --- **NOTE** Collecting environment information... ============================== System Info ============================== OS : Alibaba Cloud Linux 3 (Soaring Falcon) (x86_64) GCC version : (GCC) 10.2.1 20200825 (Alibaba 10.2.1-3.8 2.32) Clang version : Could not collect CMake version : version 4.2.1 Libc version : glibc-2.32 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 | packaged by conda-forge | (main, Jan 26 2026, 23:51:32) [GCC 14.3.0] (64-bit runtime) Python platform : Linux-5.10.134-010.ali5000.al8.x86_64-x86_64-with-glibc2.32 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.61 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA L20 GPU 1: NVIDIA L20 Nvidia driver version : 535.161.08 cuDNN version : Probably one of the following: /usr/lib64/libcudnn.so.9...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : Alibaba Cloud Linux 3 (Soaring Falcon) (x86_64) GCC version : (GCC) 10.2.1 20200825 (Alibaba 10.2.1-3.8 2.32) Clang version : Could not collect CMake version : version 4.2.1 Libc version : glibc-2.32 ========
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: llm serve "Qwen/Qwen3.5-27B" --quantization bitsandbytes bug;rocm ### Your current environment The output of python collect_env.py --- **NOTE** Collecting environment information... ==============================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: llm serve "Qwen/Qwen3.5-27B" --quantization bitsandbytes bug;rocm ### Your current environment The output of python collect_env.py --- **NOTE** Collecting environment information... ==============================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.4 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: llm serve "Qwen/Qwen3.5-27B" --quantization bitsandbytes bug;rocm ### Your current environment The output of python collect_env.py --- **NOTE** Collecting environment information... ==============================...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
