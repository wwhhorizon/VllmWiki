# vllm-project/vllm#445: pip install stucked in nvidia pytorch image

| 字段 | 值 |
| --- | --- |
| Issue | [#445](https://github.com/vllm-project/vllm/issues/445) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> pip install stucked in nvidia pytorch image

### Issue 正文摘录

I am following the installation guide here https://vllm.readthedocs.io/en/latest/getting_started/installation.html It will stuck at Installing build dependencies ... \ for hours, I have tried both build from source and using pip install vllm, both of them would stuck at the same place, does someone know how to achieve install? There is all command and outputs from terminal ``` # docker run --gpus all -it --rm --shm-size=8g nvcr.io/nvidia/pytorch:22.12-py3 ============= == PyTorch == ============= NVIDIA Release 22.12 (build 49968248) PyTorch Version 1.14.0a0+410ce96 Container image Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES. All rights reserved. Copyright (c) 2014-2022 Facebook Inc. Copyright (c) 2011-2014 Idiap Research Institute (Ronan Collobert) Copyright (c) 2012-2014 Deepmind Technologies (Koray Kavukcuoglu) Copyright (c) 2011-2012 NEC Laboratories America (Koray Kavukcuoglu) Copyright (c) 2011-2013 NYU (Clement Farabet) Copyright (c) 2006-2010 NEC Laboratories America (Ronan Collobert, Leon Bottou, Iain Melvin, Jason Weston) Copyright (c) 2006 Idiap Research Institute (Samy Bengio) Copyright (c) 2001-2004 Idiap Research Institute (Ronan Collobert, Samy Bengio, Johnn...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: pip install stucked in nvidia pytorch image installation I am following the installation guide here https://vllm.readthedocs.io/en/latest/getting_started/installation.html It will stuck at Installing build dependencies...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Copyright (c) 2014-2022 Facebook Inc. Copyright (c) 2011-2014 Idiap Research Institute (Ronan Collobert) Copyright (c) 2012-2014 Deepmind Technologies (Koray Kavukcuoglu) Copyright (c) 2011-2012 NEC Laboratories America...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: m following the installation guide here https://vllm.readthedocs.io/en/latest/getting_started/installation.html It will stuck at Installing build dependencies ... \ for hours, I have tried both build from source and usi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
