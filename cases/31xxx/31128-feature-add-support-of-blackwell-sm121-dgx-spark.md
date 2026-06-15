# vllm-project/vllm#31128: [Feature]: Add support of Blackwell SM121(DGX Spark)

| 字段 | 值 |
| --- | --- |
| Issue | [#31128](https://github.com/vllm-project/vllm/issues/31128) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;kernel |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Add support of Blackwell SM121(DGX Spark)

### Issue 正文摘录

## 🚀 Feature Request ### Summary Request native support for NVIDIA DGX Spark platform running Blackwell (GB10) GPU with CUDA 13.0 and ARM64 architecture. ### Environment - **Hardware**: NVIDIA DGX Spark with GB10 GPU (Blackwell architecture) - **Architecture**: ARM64 (aarch64) - **CUDA Version**: 13.0 - **PyTorch Version**: 2.10.0a0 (from `nvcr.io/nvidia/pytorch:25.11-py3`) - **vLLM Version**: 0.13.0 ### Current Issue vLLM 0.13.0 requires `torch==2.9.0`, but: 1. **PyTorch 2.9.0 CUDA wheels are not available for ARM64** - The official PyTorch cu124 index only has x86_64 wheels 2. **NVIDIA NGC PyTorch 25.11 image ships with PyTorch 2.10** - This is the only source of ARM64 + CUDA-enabled PyTorch for Blackwell GPUs 3. **vLLM's pre-compiled CUDA kernels expect CUDA 12** - Causes `libcudart.so.12` errors on CUDA 13 systems ### Current Workaround Using `--enforce-eager` flag with `--no-deps` installation: pip install vllm==0.13.0 --no-deps pip install [vllm dependencies except torch] python -m vllm.entrypoints.openai.api_server --model ... --enforce-eagerThis works but disables CUDA graph optimizations, resulting in ~20-30% slower inference. ### Requested Features 1. **Support PyTorch 2...

## 现有链接修复摘要

#37700 [Bugfix] Fix FLA Hopper/TMA misclassification on SM12x desktop Blackwell

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: PU (Blackwell architecture) - **Architecture**: ARM64 (aarch64) - **CUDA Version**: 13.0 - **PyTorch Version**: 2.10.0a0 (from `nvcr.io/nvidia/pytorch:25.11-py3`) - **vLLM Version**: 0.13.0 ### Current Issue vLLM 0.13.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Feature]: Add support of Blackwell SM121(DGX Spark) feature request ## 🚀 Feature Request ### Summary Request native support for NVIDIA DGX Spark platform running Blackwell (GB10) GPU with CUDA 13.0 and ARM64 architectu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ependencies except torch] python -m vllm.entrypoints.openai.api_server --model ... --enforce-eagerThis works but disables CUDA graph optimizations, resulting in ~20-30% slower inference. ### Requested Features 1. **Supp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add support of Blackwell SM121(DGX Spark) feature request ## 🚀 Feature Request ### Summary Request native support for NVIDIA DGX Spark platform running Blackwell (GB10) GPU with CUDA 13.0 and ARM64 architectu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: uiring `--enforce-eager` ### Additional Context DGX Spark is NVIDIA's latest edge AI platform targeting enterprise deployment. Native vLLM support would greatly benefit users deploying LLM inference on this hardware. ##...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37700](https://github.com/vllm-project/vllm/pull/37700) | closes_keyword | 0.95 | [Bugfix] Fix FLA Hopper/TMA misclassification on SM12x desktop Blackwell | Fixes #31128 (partial — FLA component) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
