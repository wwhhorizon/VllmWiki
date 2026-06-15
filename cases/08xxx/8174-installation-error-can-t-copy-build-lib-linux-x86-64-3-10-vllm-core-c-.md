# vllm-project/vllm#8174: [Installation]: error: can't copy 'build/lib.linux-x86_64-3.10/vllm/_core_C.abi3.so': doesn't exist or not a regular file

| 字段 | 值 |
| --- | --- |
| Issue | [#8174](https://github.com/vllm-project/vllm/issues/8174) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: error: can't copy 'build/lib.linux-x86_64-3.10/vllm/_core_C.abi3.so': doesn't exist or not a regular file

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.26.0 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-102-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.5.40 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 D Nvidia driver version: 555.58.02 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.1.3.1 [pip3] nvidia-cuda-cupti-cu12==12.1.105 [pip3] nvidia-cuda-nvrtc-cu12==12.1.105 [pip3] nvidia-cuda-runtime-cu12==12.1.105 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pip3] nvidia-cufft-cu12==11.0.2.54 [pip3] nvidia-curand-cu12==10.3.2.106 [pip3] nvidia-cusolver-cu12==11...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: error: can't copy 'build/lib.linux-x86_64-3.10/vllm/_core_C.abi3.so': doesn't exist or not a regular file installation;stale ### Your current environment ```text The output of `python collect_env.py` ```
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: `text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.44.2 [pip3] triton==3.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A vLLM Build Flags: CUDA Archs: No...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nvironment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
