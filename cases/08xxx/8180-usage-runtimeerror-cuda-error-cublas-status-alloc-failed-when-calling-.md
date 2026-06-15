# vllm-project/vllm#8180: [Usage]: "RuntimeError: CUDA error: CUBLAS_STATUS_ALLOC_FAILED when calling `cublasCreate(handle)`" when serving w8a8

| 字段 | 值 |
| --- | --- |
| Issue | [#8180](https://github.com/vllm-project/vllm/issues/8180) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: "RuntimeError: CUDA error: CUBLAS_STATUS_ALLOC_FAILED when calling `cublasCreate(handle)`" when serving w8a8

### Issue 正文摘录

### Your current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: **** Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC) 9.2.1 20200522 (**** 9.2.1-3 2.17) Clang version: Could not collect CMake version: version 3.30.2 Libc version: glibc-2.30 Python version: 3.8.18 (default, Sep 11 2023, 13:40:15) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.9.151-015.ali3000.alios7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 470.82.01 cuDNN version: Probably one of the following: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: e)`" when serving w8a8 usage;stale ### Your current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: **** Group Enterprise Linux Server...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: "RuntimeError: CUDA error: CUBLAS_STATUS_ALLOC_FAILED when calling `cublasCreate(handle)`" when serving w8a8 usage;stale ### Your current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 470.82.01 cuDNN version: Probably one of the following: /usr/local/cu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .1+cecc4fc [pip3] torchvision==0.19.0 [pip3] transformers==4.44.2 [pip3] triton==3.0.0 [conda] atorch 1.2.1 pypi_0 pypi [conda] numpy 1.23.5 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nter this runtime error when I try serving neuralmagic/Qwen2-7B-Instruct-quantized.w8a8 downloaded from HF. The command is as followed: python -m vllm.entrypoints.openai.api_server --served-model-name Qwen2-7B-Instruct-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
