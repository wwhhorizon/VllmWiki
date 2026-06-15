# vllm-project/vllm#3253: When I set tensor_parallel_size=2, a time error occurred

| 字段 | 值 |
| --- | --- |
| Issue | [#3253](https://github.com/vllm-project/vllm/issues/3253) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> When I set tensor_parallel_size=2, a time error occurred

### Issue 正文摘录

My device is A800. When I do not set the tensor_parallel_size parameter, the vllm+qwen14b api can start normally and automatically use card 0. ![image](https://github.com/vllm-project/vllm/assets/73686733/a7c42c0c-67ba-487f-88e9-f85fa9496572) When I set tensor_parallel_size=2, a RunTimeError occurs. ![image](https://github.com/vllm-project/vllm/assets/73686733/500e945a-0500-43a1-9766-75a886c8c536) The main contents are: **RuntimeError: ProcessGroupNCCL is ony supported with GPUs, no GPUs found! Warning: CUDA initialization Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 103: intergrity checks failed (function operator())** I verified the following options： ![image](https://github.com/vllm-project/vllm/assets/73686733/b6d0604a-c990-4bd6-a1b2-83ea2665692c) **My envs:** cuda 11.7 torch 2.0.1 python 3.8.16 vllm 0.2.1 How should this problem be solved? My api code: import argparse import asyncio import json import time from http import HTTPStatus from typing import AsyncGenerator, Dict, List, Optional, Tuple, Union import torch import re import fastapi import uvicorn from fastapi imp...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: is A800. When I do not set the tensor_parallel_size parameter, the vllm+qwen14b api can start normally and automatically use card 0. ![image](https://github.com/vllm-project/vllm/assets/73686733/a7c42c0c-67ba-487f-88e9-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: thon 3.8.16 vllm 0.2.1 How should this problem be solved? My api code: import argparse import asyncio import json import time from http import HTTPStatus from typing import AsyncGenerator, Dict, List, Optional, Tuple, U...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: When I set tensor_parallel_size=2, a time error occurred stale My device is A800. When I do not set the tensor_parallel_size parameter, the vllm+qwen14b api can start normally and automatically use card 0. ![image](http...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: or: ProcessGroupNCCL is ony supported with GPUs, no GPUs found! Warning: CUDA initialization Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have al...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: astchat_available = True except ImportError: _fastchat_available = False TIMEOUT_KEEP_ALIVE = 5 # seconds logger = init_logger(__name__) served_model = None app = fastapi.FastAPI() engine = None @app.get("/health") asyn...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
