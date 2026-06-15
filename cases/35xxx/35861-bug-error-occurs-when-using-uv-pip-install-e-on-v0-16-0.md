# vllm-project/vllm#35861: [Bug]: error occurs when using uv pip install -e . on v0.16.0

| 字段 | 值 |
| --- | --- |
| Issue | [#35861](https://github.com/vllm-project/vllm/issues/35861) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: error occurs when using uv pip install -e . on v0.16.0

### Issue 正文摘录

### Your current environment Driver: NVIDIA-SMI 590.48.01 Driver Version: 590.48.01 CUDA Version: 13.1 docker images: nvcr.io/nvidia/cuda:12.9.1-cudnn-devel-ubuntu22.04 ### 🐛 Describe the bug My install as: ``` git clone https://github.com/vllm-project/vllm.git cd vllm git checkout v0.16.0 VLLM_USE_PRECOMPILED=1 uv pip install --editable . ``` when i run offline, error always occurs as: ``` File "/home/gaoruimin/vllm/vllm/platforms/cuda.py", line 16, in import vllm._C # noqa ^^^^^^^^^^^^^^ ImportError: /home/gaoruimin/vllm/vllm/_C.abi3.so: undefined symbol: _ZN3c104cuda29c10_cuda_check_implementationEiPKcS2_jb ``` I try to install v0.16.0 at the same uv venv using: `uv pip install vllm --torch-backend=auto` and offline inference program finished as expected. I use the same method to install v0.13.0 editable about 1 month ago, it runs well. seem like something in new version introduced this error. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: error occurs when using uv pip install -e . on v0.16.0 bug;stale ### Your current environment Driver: NVIDIA-SMI 590.48.01 Driver Version: 590.48.01 CUDA Version: 13.1 docker images: nvcr.io/nvidia/cuda:12.9.1-cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: l -e . on v0.16.0 bug;stale ### Your current environment Driver: NVIDIA-SMI 590.48.01 Driver Version: 590.48.01 CUDA Version: 13.1 docker images: nvcr.io/nvidia/cuda:12.9.1-cudnn-devel-ubuntu22.04 ### 🐛 Describe the bug...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: install v0.16.0 at the same uv venv using: `uv pip install vllm --torch-backend=auto` and offline inference program finished as expected. I use the same method to install v0.13.0 editable about 1 month ago, it runs well...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: error occurs when using uv pip install -e . on v0.16.0 bug;stale ### Your current environment Driver: NVIDIA-SMI 590.48.01 Driver Version: 590.48.01 CUDA Version: 13.1 docker images: nvcr.io/nvidia/cuda:12.9.1-cu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda import_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
