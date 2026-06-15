# vllm-project/vllm#35593: [Bug]: CUDA Error 803 (system has unsupported display driver / cuda driver combination) when host driver is 590.48.01 due to cuda-compat conflict

| 字段 | 值 |
| --- | --- |
| Issue | [#35593](https://github.com/vllm-project/vllm/issues/35593) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA Error 803 (system has unsupported display driver / cuda driver combination) when host driver is 590.48.01 due to cuda-compat conflict

### Issue 正文摘录

### Your current environment **Description** When running the latest vLLM Docker image vllm/vllm-openai:v0.16.0-x86_64 on a host with NVIDIA driver 590.48.01 (which supports CUDA 13.1 according to nvidia-smi), the engine fails to initialize with the following error: RuntimeError: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 803: system has unsupported display driver / cuda driver combination The issue does not occur with older vLLM images like v0.11.0. After investigation, we found that the problem is caused by a conflict between the cuda-compat libraries bundled inside the vLLM image (located at /usr/local/cuda/compat/lib) and the high-version host driver (590.48.01). The cuda-compat layer is intended to allow newer CUDA toolkits to run on older drivers, but in this case it actually interferes with the proper driver libraries provided by the NVIDIA Container Toolkit. **Environment** Host OS: Ubuntu 22.04 NVIDIA Driver: 590.48.01 (shows CUDA Version: 13.1 in nvidia-smi) GPU: NVIDIA A800 80GB PCIe (Arch 8.0) Docker: with nvidia runtime and nvidia-container-toolkit 1.18.2 vLLM...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: # Your current environment **Description** When running the latest vLLM Docker image vllm/vllm-openai:v0.16.0-x86_64 on a host with NVIDIA driver 590.48.01 (which supports CUDA 13.1 according to nvidia-smi), the engine...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA Error 803 (system has unsupported display driver / cuda driver combination) when host driver is 590.48.01 due to cuda-compat conflict bug ### Your current environment **Description** When running the latest...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: (failing): docker run --runtime nvidia --gpus "device=1" \ -v /home/models/:/home/models \ -p 8001:8000 \ --ipc=host \ -d \ --name Qwen3-30B-A3B-Instruct-2507 \ docker.1ms.run/vllm/vllm-openai:v0.16.0-x86_64 \ --model /...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: y either lack cuda-compat or it does not conflict. The same error can be reproduced with the official nvidia/cuda:12.8.1-base-ubuntu22.04 image, confirming that it's a general cuda-compat vs. driver issue, not specific...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ict bug ### Your current environment **Description** When running the latest vLLM Docker image vllm/vllm-openai:v0.16.0-x86_64 on a host with NVIDIA driver 590.48.01 (which supports CUDA 13.1 according to nvidia-smi), t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
