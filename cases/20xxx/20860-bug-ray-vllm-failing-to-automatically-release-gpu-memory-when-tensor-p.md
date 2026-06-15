# vllm-project/vllm#20860: [Bug]: Ray + vLLM failing to automatically release GPU memory when tensor parallelism size (tp_size) > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#20860](https://github.com/vllm-project/vllm/issues/20860) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;sampling |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ray + vLLM failing to automatically release GPU memory when tensor parallelism size (tp_size) > 1

### Issue 正文摘录

### Your current environment My program runs correctly under the following environment: vllm=0.7.0 torch=2.5.1 CUDA 12.4 (Cu124) flashattention=2.7.0.post2 To support Qwen3, I upgraded to: vllm=0.8.5 torch=2.6.0 flashattention=2.7.2.post1 The program executes without errors, ​​but it fails to automatically release GPU memory after completion​​. I conducted the experiments on 8×NVIDIA A100 GPUs. ### 🐛 Describe the bug My program runs correctly under the following environment: vllm=0.7.0 torch=2.5.1 CUDA 12.4 (Cu124) flashattention=2.7.0.post2 To support Qwen3, I upgraded to: vllm=0.8.5 torch=2.6.0 flashattention=2.7.2.post1 The program executes without errors, ​​but it fails to automatically release GPU memory after completion​​. I conducted the experiments on 8×NVIDIA A100 GPUs. Here is my code: ```python import json from vllm import LLM, SamplingParams from typing import Any, Dict, List import ray import numpy as np from packaging.version import Version import argparse import sys import os import atexit sys.path.append('..') from prompts.convert import MyDataset from transformers import AutoTokenizer, AutoConfig from vllm.distributed.parallel_state import destroy_model_parallel a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 7.0 torch=2.5.1 CUDA 12.4 (Cu124) flashattention=2.7.0.post2 To support Qwen3, I upgraded to: vllm=0.8.5 torch=2.6.0 flashattention=2.7.2.post1 The program executes without errors, ​​but it fails to automatically releas...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ucted the experiments on 8×NVIDIA A100 GPUs. Here is my code: ```python import json from vllm import LLM, SamplingParams from typing import Any, Dict, List import ray import numpy as np from packaging.version import Ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: + vLLM failing to automatically release GPU memory when tensor parallelism size (tp_size) > 1 bug;ray;stale ### Your current environment My program runs correctly under the following environment: vllm=0.7.0 torch=2.5.1...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: Ray + vLLM failing to automatically release GPU memory when tensor parallelism size (tp_size) > 1 bug;ray;stale ### Your current environment My program runs correctly under the following environment: vllm=0.7.0 t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ly release GPU memory when tensor parallelism size (tp_size) > 1 bug;ray;stale ### Your current environment My program runs correctly under the following environment: vllm=0.7.0 torch=2.5.1 CUDA 12.4 (Cu124) flashattent...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
