# vllm-project/vllm#17078: [Bug]: noop elimination for slice errors when end = -1

| 字段 | 值 |
| --- | --- |
| Issue | [#17078](https://github.com/vllm-project/vllm/issues/17078) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: noop elimination for slice errors when end = -1

### Issue 正文摘录

### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Stream 9 (x86_64) GCC version: (GCC) 11.5.0 20240719 (Red Hat 11.5.0-5) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.34 Python version: 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.4.3-0_fbk14_hardened_2601_gcd42476b84e9-x86_64-with-glibc2.34 Is CUDA available: True CUDA runtime version: 12.6.85 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 GPU 1: NVIDIA H100 GPU 2: NVIDIA H100 GPU 3: NVIDIA H100 Nvidia driver version: 550.90.07 cuDNN version: Probably one of the following: /usr/lib64/libcudnn.so.9.1.1 /usr/lib64/libcudnn_adv.so.9.1.1 /usr/lib64/libcudnn_cnn.so.9.1.1 /usr/lib64/libcudnn_engines_precompiled.so.9.1.1 /usr/lib64/libcudnn_engines_runtime_compiled.so.9.1.1 /usr/lib64/libcudnn_graph.so.9.1.1 /usr/lib64/libcudnn_heuristic.so.9.1.1 /usr/lib64/libcudnn_ops.so.9.1.1 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ice errors when end = -1 bug;stale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Stream 9 (x86_64) GCC versio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Stream 9 (x86_64) GCC version: (GCC) 11.5.0 20240719 (Red Hat 11.5.0-5)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 12.6.85 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 GPU 1: NVIDIA H100 GPU 2: NVIDIA H100 GPU 3: NVIDIA H100 Nvidia driver version: 550.90.07 cuDNN versio...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx512_bf16 clzero xsaveerptr wbnoinvd arat npt lbrv nrip_save tsc_scale vmcb_clean pausefilter pfthreshold v_vmsave_vmload vgif vnmi avx512vbmi umip pku...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.49.0 [pip3] triton==3.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
