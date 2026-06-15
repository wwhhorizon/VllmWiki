# vllm-project/vllm#4446: [Misc]: Installation on CUDA machines

| 字段 | 值 |
| --- | --- |
| Issue | [#4446](https://github.com/vllm-project/vllm/issues/4446) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Installation on CUDA machines

### Issue 正文摘录

### Question on `torch==2.2.1` requirment It seems from `requirements-cuda.txt` that `vllm` requires the specific version of `torch`, namely 2.2.1. Unless I create a separate environment, this would require me to switch my torch installation to 2.2.1. Is there a reason that the requirement is not set to `torch >= 2.2.1` instead? ```txt # Common dependencies -r requirements-common.txt # Dependencies for NVIDIA GPUs ray >= 2.9 nvidia-ml-py # for pynvml package vllm-nccl-cu12>=2.18,<2.19 # for downloading nccl library torch == 2.2.1 xformers == 0.0.25 # Requires PyTorch 2.2.1 ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Misc]: Installation on CUDA machines ### Question on `torch==2.2.1` requirment It seems from `requirements-cuda.txt` that `vllm` requires the specific version of `torch`, namely 2.2.1. Unless I create a separate enviro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Misc]: Installation on CUDA machines ### Question on `torch==2.2.1` requirment It seems from `requirements-cuda.txt` that `vllm` requires the specific version of `torch`, namely 2.2.1. Unless I create a separate enviro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
