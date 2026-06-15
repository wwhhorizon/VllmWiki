# vllm-project/vllm#18188: [Installation]: Unable to install vllm in WSL2

| 字段 | 值 |
| --- | --- |
| Issue | [#18188](https://github.com/vllm-project/vllm/issues/18188) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;import_error;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Unable to install vllm in WSL2

### Issue 正文摘录

### Your current environment ```text # SPDX-License-Identifier: Apache-2.0 # ruff: noqa # code borrowed from https://github.com/pytorch/pytorch/blob/main/torch/utils/collect_env.py import datetime import locale import os import re import subprocess import sys # Unlike the rest of the PyTorch this file must be python2 compliant. # This script outputs relevant system environment info # Run it with `python collect_env.py` or `python -m torch.utils.collect_env` from collections import namedtuple from vllm.envs import environment_variables try: import torch TORCH_AVAILABLE = True except (ImportError, NameError, AttributeError, OSError): TORCH_AVAILABLE = False # System Environment Information SystemEnv = namedtuple( 'SystemEnv', [ 'torch_version', 'is_debug_build', 'cuda_compiled_version', 'gcc_version', 'clang_version', 'cmake_version', 'os', 'libc_version', 'python_version', 'python_platform', 'is_cuda_available', 'cuda_runtime_version', 'cuda_module_loading', 'nvidia_driver_version', 'nvidia_gpu_models', 'cudnn_version', 'pip_version', # 'pip' or 'pip3' 'pip_packages', 'conda_packages', 'hip_compiled_version', 'hip_runtime_version', 'miopen_runtime_version', 'caching_allocator_confi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: Unable to install vllm in WSL2 installation ### Your current environment ```text # SPDX-License-Identifier: Apache-2.0 # ruff: noqa # code borrowed from https://github.com/pytorch/pytorch/blob/main/torch
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: mEnv', [ 'torch_version', 'is_debug_build', 'cuda_compiled_version', 'gcc_version', 'clang_version', 'cmake_version', 'os', 'libc_version', 'python_version', 'python_platform', 'is_cuda_available',
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: buteError, OSError): TORCH_AVAILABLE = False # System Environment Information SystemEnv = namedtuple( 'SystemEnv', [ 'torch_version', 'is_debug_build', 'cuda_compiled_version', 'gcc_version', 'clang_version', 'cmake_ver...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: t: return None # Alphabetize the result because the order is non-deterministic otherwise files = sorted(files_set) if len(files) == 1: return files[0] result = '\n'.join(files) return 'Probably one of the following:\n{}...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: lse: enc = locale.getpreferredencoding() output = raw_output.decode(enc) if command == 'nvidia-smi topo -m': # don't remove the leading whitespace of `nvidia-smi topo -m` # because they are meaningful output = output.rs...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
