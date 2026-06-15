# vllm-project/vllm#21979: [Bug]: cuda version of `vllm/vllm-openai:latest` older than k8s node cuda 12.9 Incompatibility error

| 字段 | 值 |
| --- | --- |
| Issue | [#21979](https://github.com/vllm-project/vllm/issues/21979) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cuda version of `vllm/vllm-openai:latest` older than k8s node cuda 12.9 Incompatibility error

### Issue 正文摘录

### Your current environment GKE version: `1.33.2-gke.1111000` I am deploying a model from HF using vllm-server on GKE. My node is running: Driver `575.57.08` with reported CUDA Version: `12.9`. ``` containers: - name: vllm image: vllm/vllm-openai:latest command: ["/bin/sh", "-c"] args: - | pip install -r /mnt/requirements/requirements.txt \ && vllm serve google/gemma-4b-it \ --host 0.0.0.0 \ --port 8000 \ ``` ### 🐛 Describe the bug I am running into No platform detected / CUDA initialization error. Error 803: system has unsupported display driver / cuda driver combination. Is the `vllm/vllm-openai:latest` image not compatible with `cuda 12.9` ? ``` INFO 07-30 15:32:48 [__init__.py:239] No platform detected, vLLM is running on UnspecifiedPlatform /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:991: UserWarning: CUDA initialization: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 803: system has unsupported display driver / cuda driver combination (Triggered internally at /pytorch/c10/cuda/CUDAFunctions.cpp:109.) r = torch._C._cuda_getDeviceCount() if nvml_count sy...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: cuda version of `vllm/vllm-openai:latest` older than k8s node cuda 12.9 Incompatibility error bug;stale ### Your current environment GKE version: `1.33.2-gke.1111000` I am deploying a model from HF using vllm-ser...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: urrent environment GKE version: `1.33.2-gke.1111000` I am deploying a model from HF using vllm-server on GKE. My node is running: Driver `575.57.08` with reported CUDA Version: `12.9`. ``` containers: - name: vllm image...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: cuda version of `vllm/vllm-openai:latest` older than k8s node cuda 12.9 Incompatibility error bug;stale ### Your current environment GKE version: `1.33.2-gke.1111000` I am deploying a model from HF using vllm-ser...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: /mnt/requirements/requirements.txt \ && vllm serve google/gemma-4b-it \ --host 0.0.0.0 \ --port 8000 \ ``` ### 🐛 Describe the bug I am running into No platform detected / CUDA initialization error. Error 803: system has...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: m-openai:latest` older than k8s node cuda 12.9 Incompatibility error bug;stale ### Your current environment GKE version: `1.33.2-gke.1111000` I am deploying a model from HF using vllm-server on GKE. My node is running:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
