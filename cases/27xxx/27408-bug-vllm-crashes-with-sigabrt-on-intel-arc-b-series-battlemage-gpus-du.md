# vllm-project/vllm#27408: [Bug]: vLLM crashes with SIGABRT on Intel Arc B-series (Battlemage) GPUs during model inspection

| 字段 | 值 |
| --- | --- |
| Issue | [#27408](https://github.com/vllm-project/vllm/issues/27408) |
| 状态 | closed |
| 标签 | bug;intel-gpu |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error;crash;import_error;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM crashes with SIGABRT on Intel Arc B-series (Battlemage) GPUs during model inspection

### Issue 正文摘录

### Your current environment vLLM Version: 0.11.0 PyTorch Version: 2.5.1+cxx11.abi Intel Extension for PyTorch: 2.5.10+xpu OS: Fedora 42 (kernel 6.16.12-200.fc42.x86_64) GPU: 2x Intel Arc Pro B60 (24GB each, device ID 0xe211) Container Runtime: Podman 5.x (rootless) Base Image: intel/intel-extension-for-pytorch:2.8.10-xpu Python: 3.11 Driver versions: - Level-Zero: 1.6.32224.5 - Intel OpenCL: 24.52.32224.5 - Intel Compute Runtime: NEO 24.52.32224 # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project # ruff: noqa # code borrowed from https://github.com/pytorch/pytorch/blob/main/torch/utils/collect_env.py import datetime import locale import os import subprocess import sys # Unlike the rest of the PyTorch this file must be python2 compliant. # This script outputs relevant system environment info # Run it with `python collect_env.py` or `python -m torch.utils.collect_env` from collections import namedtuple import regex as re from vllm.envs import environment_variables try: import torch TORCH_AVAILABLE = True except (ImportError, NameError, AttributeError, OSError): TORCH_AVAILABLE = False # System Environment Information SystemEnv...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: during model inspection bug;intel-gpu ### Your current environment vLLM Version: 0.11.0 PyTorch Version: 2.5.1+cxx11.abi Intel Extension for PyTorch: 2.5.10+xpu OS: Fedora 42 (kernel 6.16.12-200.fc42.x86_64) GPU: 2x Int...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: vLLM crashes with SIGABRT on Intel Arc B-series (Battlemage) GPUs during model inspection bug;intel-gpu ### Your current environment vLLM Version: 0.11.0 PyTorch Version: 2.5.1+cxx11.abi Intel Extension for PyTorch: 2.5...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: mEnv", [ "torch_version", "is_debug_build", "cuda_compiled_version", "gcc_version", "clang_version", "cmake_version", "os", "libc_version", "python_version", "python_platform", "is_cuda_available",
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: t: return None # Alphabetize the result because the order is non-deterministic otherwise files = sorted(files_set) if len(files) == 1: return files[0] result = "\n".join(files) return "Probably one of the following:\n{}...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: "numpy", "cudatoolkit", "soumith", "mkl", "magma", "triton", "optree", "nccl", "transformers", "zmq", "nvidia", "pynvml", "flashinfer-python", } DEFAULT_PIP_PATTERNS = { "torch", "numpy", "mypy", "flake8", "triton", "op

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
