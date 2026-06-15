# vllm-project/vllm#20227: [Usage]: How to use custom reasoning parser?

| 字段 | 值 |
| --- | --- |
| Issue | [#20227](https://github.com/vllm-project/vllm/issues/20227) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use custom reasoning parser?

### Issue 正文摘录

### Your current environment ```text NCCL_VERSION=2.25.1-1 NVIDIA_DRIVER_CAPABILITIES=compute,utility NVIDIA_PRODUCT_NAME=CUDA VLLM_USAGE_SOURCE=production-docker-image CUDA_VERSION=12.8.1 LD_LIBRARY_PATH=/usr/local/cuda/lib64 NCCL_CUMEM_ENABLE=0 PYTORCH_NVML_BASED_CUDA_CHECK=1 TORCHINDUCTOR_COMPILE_THREADS=1 CUDA_MODULE_LOADING=LAZY ``` ### How would you like to use vllm I want to use a custom reasoning parser but not sure how to register it. I saw the docs on how to write the code for a custom reasoning parser, but its not clear where to define that code or how to show vllm that path. For the tool parser there is a arg named `--tool-parser-plugin` but couldnt find any for reasoning parser. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: reasoning parser? usage;stale ### Your current environment ```text NCCL_VERSION=2.25.1-1 NVIDIA_DRIVER_CAPABILITIES=compute,utility NVIDIA_PRODUCT_NAME=CUDA VLLM_USAGE_SOURCE=production-docker-image CUDA_VERSION=12.8.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: =2.25.1-1 NVIDIA_DRIVER_CAPABILITIES=compute,utility NVIDIA_PRODUCT_NAME=CUDA VLLM_USAGE_SOURCE=production-docker-image CUDA_VERSION=12.8.1 LD_LIBRARY_PATH=/usr/local/cuda/lib64 NCCL_CUMEM_ENABLE=0 PYTORCH_NVML_BASED_CU...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to use custom reasoning parser? usage;stale ### Your current environment ```text NCCL_VERSION=2.25.1-1 NVIDIA_DRIVER_CAPABILITIES=compute,utility NVIDIA_PRODUCT_NAME=CUDA VLLM_USAGE_SOURCE=production-docker...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
