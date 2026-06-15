# vllm-project/vllm#5457: [Installation]: M2 Mac Dependency Torch 2.1.2 (Incompatible) 

| 字段 | 值 |
| --- | --- |
| Issue | [#5457](https://github.com/vllm-project/vllm/issues/5457) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
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

> [Installation]: M2 Mac Dependency Torch 2.1.2 (Incompatible) 

### Issue 正文摘录

### Your current environment PyTorch version: 2.3.1 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: macOS 14.1.1 (arm64) GCC version: Could not collect Clang version: 15.0.0 (clang-1500.0.40.1) CMake version: version 3.29.5 Libc version: N/A Python version: 3.12.3 | packaged by Anaconda, Inc. | (main, May 6 2024, 14:46:42) [Clang 14.0.6 ] (64-bit runtime) Python platform: macOS-14.1.1-arm64-arm-64bit Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Apple M2 Max Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] torch==2.3.1 [pip3] transformers==4.41.2 [pip3] transformers==4.41.2 [conda] numpy 1.26.4 pypi_0 pypi [conda] torch 2.3.1 pypi_0 pypi [conda] transformers 4.41.2 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: Could not collect ### How you are installing vllm ```sh git clone https://github....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: M2 Mac Dependency Torch 2.1.2 (Incompatible) installation ### Your current environment PyTorch version: 2.3.1 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: m
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: # Your current environment PyTorch version: 2.3.1 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: macOS 14.1.1 (arm64) GCC version: Could not collect Clang version: 15.0.0 (cla...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNN...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ution found for torch==2.1.2 # i have also found issues with installing triton so I have built it from source but similarly run into issues with "sentencepiece" requiring "ray" which requires "torch=2.1.2". I am install...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: variable is not set. Please set it to your CUDA install root. # I can't reproduce the error if I run it again. It does seem to run. VLLM_TARGET_DEVICE=cpu python3 setup.py install # note that the following error message...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
