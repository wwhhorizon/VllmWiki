# vllm-project/vllm#6762: [Doc]: ROCm installation instructions do not work

| 字段 | 值 |
| --- | --- |
| Issue | [#6762](https://github.com/vllm-project/vllm/issues/6762) |
| 状态 | closed |
| 标签 | documentation;rocm |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: ROCm installation instructions do not work

### Issue 正文摘录

### 📚 The doc issue Following the instructions at https://docs.vllm.ai/en/latest/getting_started/amd-installation.html#build-from-source-rocm, using the exact Docker image mentioned (pytorch_rocm6.1.2_ubuntu20.04_py3.9_pytorch_staging.sif, although with a custom Python venv and Pytorch install), and run into the following error when running `python setup.py develop`: ``` Building PyTorch for GPU arch: gfx90a -- Could NOT find HIP: Found unsuitable version "0.0.0", but required is at least "1.0" (found /opt/rocm) HIP VERSION: 0.0.0 CMake Warning at .venv/lib/python3.10/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message): static library kineto_LIBRARY-NOTFOUND not found. Call Stack (most recent call first): .venv/lib/python3.10/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:120 (append_torchlib_if_found) CMakeLists.txt:67 (find_package) CMake Error at CMakeLists.txt:108 (message): Can't find CUDA or HIP installation. ``` The docker image should have a proper HIP setup, right? `hipconfig` says: `HIP version : 6.1.40093-bd86f1708`. ### Suggest a potential alternative/fix _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Doc]: ROCm installation instructions do not work documentation;rocm ### 📚 The doc issue Following the instructions at https://docs.vllm.ai/en/latest/getting_started/amd-installation.html#build-from-source-rocm, using t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Doc]: ROCm installation instructions do not work documentation;rocm ### 📚 The doc issue Following the instructions at https://docs.vllm.ai/en/latest/getting_started/amd-installation.html#build-from-source-rocm, using t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rning at .venv/lib/python3.10/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message): static library kineto_LIBRARY-NOTFOUND not found. Call Stack (most recent call first): .venv/lib/python3.10/site-packag...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 📚 The doc issue Following the instructions at https://docs.vllm.ai/en/latest/getting_started/amd-installation.html#build-from-source-rocm, using the exact Docker image mentioned (pytorch_rocm6.1.2_ubuntu20.04_py3.9_pyto...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
