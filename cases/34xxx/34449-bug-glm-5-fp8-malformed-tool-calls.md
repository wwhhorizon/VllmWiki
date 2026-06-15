# vllm-project/vllm#34449: [Bug]: GLM-5-FP8 malformed tool calls

| 字段 | 值 |
| --- | --- |
| Issue | [#34449](https://github.com/vllm-project/vllm/issues/34449) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-5-FP8 malformed tool calls

### Issue 正文摘录

``` ### Your current environment ============================== System Info ============================== OS : Rocky Linux 9.7 (Blue Onyx) (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-11) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jul 11 2025, 22:43:48) [Clang 20.1.4 ] (64-bit runtime) Python platform : Linux-5.14.0-611.13.1.el9_7.x86_64-x86_64-with-glibc2.34 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.1.80 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H200 GPU 1: NVIDIA H200 GPU 2: NVIDIA H200 GPU 3: NVIDIA H200 GPU 4: NVIDIA H200 GPU 5: NVIDIA H200 GPU 6: NVIDIA H200 GPU 7: NVIDIA H200 Nvidia driver version : 590.44.01 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime versi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: OS : Rocky Linux 9.7 (Blue Onyx) (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-11) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.34 ==========
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: GLM-5-FP8 malformed tool calls bug ``` ### Your current environment ============================== System Info ============================== OS : Rocky Linux 9.7 (Blue Onyx) (x86_64) GCC ver
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.3 [pip3] numpy==2.4.2 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: UDA runtime version : 13.1.80 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H200 GPU 1: NVIDIA H200 GPU 2: NVIDIA H200 GPU 3: NVIDIA H200 GPU 4: NVIDIA H200 GPU 5: NVIDIA H200 GPU 6: NVIDIA H...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
