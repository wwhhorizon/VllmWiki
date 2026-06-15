# vllm-project/vllm#10813: [Usage]: How to use llava-hf/llava-1.5-7b-hf with bitsandbytes quantization in vllm serve? 

| 字段 | 值 |
| --- | --- |
| Issue | [#10813](https://github.com/vllm-project/vllm/issues/10813) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to use llava-hf/llava-1.5-7b-hf with bitsandbytes quantization in vllm serve? 

### Issue 正文摘录

### Your current environment ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04.1) 11.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.9.19 (main, May 6 2024, 19:43:03) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.19.0-051900-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.7.64 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3060 Laptop GPU Nvidia driver version: 535.104.05 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pip3] nvidia-cufft-cu12==11.2.1.3 [pip3] nvidia-curand-cu12==10.3.5.147 [pip3] nvidia-cusolver-cu12==11.6.1.9 [pip3] nvidia-cusparse-cu12==12.3.1.170 [pip3] nvidia-ml-py==1...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Usage]: How to use llava-hf/llava-1.5-7b-hf with bitsandbytes quantization in vllm serve? usage;stale ### Your current environment ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: on in vllm serve? usage;stale ### Your current environment ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: rent environment ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04.1) 11.3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: How to use llava-hf/llava-1.5-7b-hf with bitsandbytes quantization in vllm serve? usage;stale ### Your current environment ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: current environment ``` PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04.1) 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
