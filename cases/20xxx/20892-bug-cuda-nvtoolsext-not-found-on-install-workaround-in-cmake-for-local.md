# vllm-project/vllm#20892: [Bug]: CUDA::nvToolsExt not found on install workaround in CMake for local build

| 字段 | 值 |
| --- | --- |
| Issue | [#20892](https://github.com/vllm-project/vllm/issues/20892) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA::nvToolsExt not found on install workaround in CMake for local build

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Tried to a local build of vllm in WSL2 Ubuntu to get it to compile with the nightly PyTorch for CUDA 12.9 on my Blackwell NVIDIA GPU. Currently have PyTorch stable of 2.7.1 with CUDA 12.8 installed because its working with vllm 0.9.2. ```python export TORCH_CUDA_ARCH_LIST="12.0+PTX" pip install -e . ``` Ran into the issue with nvToolsExt not found because CUDA 12.9 no longer has this. I had to put the following into the CMakeLists.txt to both add nvtx3 as a library for CUDA::nvtx3 to work and then link nvToolsExt to nvtx3 right before the `find_package(Torch REQUIRED)` . ``` # # Import torch cmake configuration. # Torch also imports CUDA (and partially HIP) languages with some customizations, # so there is no need to do this explicitly with check_language/enable_language, # etc. # # Workaround for PyTorch NVTX headers issue with newer CUDA Toolkits # Assumes find_package(CUDAToolkit) was already done message(STATUS "Applying custom PyTorch NVTX headers workaround...") if(NOT TARGET CUDA::nvToolsExt) message(STATUS "--> nvToolsExt Not found, looking for nvtx3.") if (NOT TARGET CUDA::nvtx3) message(STATUS "--> nvtx3 not found, addi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: CUDA::nvToolsExt not found on install workaround in CMake for local build bug;stale ### Your current environment ### 🐛 Describe the bug Tried to a local build of vllm in WSL2 Ubuntu to get it to compile with the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CUDA::nvToolsExt not found on install workaround in CMake for local build bug;stale ### Your current environment ### 🐛 Describe the bug Tried to a local build of vllm in WSL2 Ubuntu to get it to compile with the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: before the `find_package(Torch REQUIRED)` . ``` # # Import torch cmake configuration. # Torch also imports CUDA (and partially HIP) languages with some customizations, # so there is no need to do this explicitly with ch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: :nvToolsExt not found on install workaround in CMake for local build bug;stale ### Your current environment ### 🐛 Describe the bug Tried to a local build of vllm in WSL2 Ubuntu to get it to compile with the nightly PyTo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
