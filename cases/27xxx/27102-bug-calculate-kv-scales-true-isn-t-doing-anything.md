# vllm-project/vllm#27102: [Bug]: calculate_kv_scales=True isn't doing anything

| 字段 | 值 |
| --- | --- |
| Issue | [#27102](https://github.com/vllm-project/vllm/issues/27102) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: calculate_kv_scales=True isn't doing anything

### Issue 正文摘录

### Your current environment ``` ============================== System Info ============================== OS : CentOS Stream 9 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-11) Clang version : 20.1.8 (CentOS 20.1.8-3.el9) CMake version : version 3.26.5 Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Aug 14 2025, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-11)] (64-bit runtime) Python platform : Linux-5.14.0-620.el9.x86_64-x86_64-with-glibc2.34 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ============ OS : CentOS Stream 9 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-11) Clang version : 20.1.8 (CentOS 20.1.8-3.el9) CMake version : version 3.26.5 Libc version : glibc-2.34 ==
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.4.0 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: untime version : 12.9.86 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: calculate_kv_scales=True isn't doing anything bug;stale ### Your current environment ``` ============================== System Info ============================== OS : CentOS Stream 9 (x86_64) GCC v

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
