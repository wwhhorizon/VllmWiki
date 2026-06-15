# vllm-project/vllm#3300: Error compiling kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#3300](https://github.com/vllm-project/vllm/issues/3300) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;moe |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;moe;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Error compiling kernels

### Issue 正文摘录

I'm getting the following error after `pip install -e .` I am using CUDA 12.1. Any ideas? ``` FAILED: /tmp/tmp9dt48qcq.build-temp/csrc/moe/topk_softmax_kernels.o /usr/local/cuda-12.1/bin/nvcc -I/tmp/pip-build-env-msum09y4/overlay/lib/python3.11/site-packages/torch/include -I/tmp/pip-build-env-msum09y4/overlay/lib/python3.11/site-packages/torch/include/torch/csrc/api/include -I/tmp/pip-build-env-msum09y4/overlay/lib/python3.11/site-packages/torch/include/TH -I/tmp/pip-build-env-msum09y4/overlay/lib/python3.11/site-packages/torch/include/THC -I/usr/local/cuda-12.1/include -I/home/dan/.pyenv/versions/3.11.8/include/python3.11 -c -c /home/dan/vllm/csrc/moe/topk_softmax_kernels.cu -o /tmp/tmp9dt48qcq.build-temp/csrc/moe/topk_softmax_kernels.o --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O2 -std=c++17 -D_GLIBCXX_USE_CXX11_ABI=0 -gencode arch=compute_86,code=sm_86 --threads 8 -DENABLE_FP8_E5M2 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr -DTORCH_API_INCLUDE_EXTENSION_H '-DPYBIND11_COMPILER_TYPE="_gcc"' '-DPYBIND11_STDLIB="_libstdcpp"' '-DPYBIND11_BUILD_ABI="_cxxabi10...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Error compiling kernels stale I'm getting the following error after `pip install -e .` I am using CUDA 12.1. Any ideas? ``` FAILED: /tmp/tmp9dt48qcq.build-temp/csrc/moe/topk_softmax_kernels.o /usr/local/cuda-12.1/bin/nv...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: USE_CXX11_ABI=0 -gencode arch=compute_86,code=sm_86 --threads 8 -DENABLE_FP8_E5M2 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relax...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tale I'm getting the following error after `pip install -e .` I am using CUDA 12.1. Any ideas? ``` FAILED: /tmp/tmp9dt48qcq.build-temp/csrc/moe/topk_softmax_kernels.o /usr/local/cuda-12.1/bin/nvcc -I/tmp/pip-build-env-m...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: sing CUDA 12.1. Any ideas? ``` FAILED: /tmp/tmp9dt48qcq.build-temp/csrc/moe/topk_softmax_kernels.o /usr/local/cuda-12.1/bin/nvcc -I/tmp/pip-build-env-msum09y4/overlay/lib/python3.11/site-packages/torch/include -I/tmp/pi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Error compiling kernels stale I'm getting the following error after `pip install -e .` I am using CUDA 12.1. Any ideas? ``` FAILED: /tmp/tmp9dt48qcq.build-temp/csrc/moe/topk_softmax_kernels.o /usr/local/cuda-12.1/bin/nv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
