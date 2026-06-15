# vllm-project/vllm#17783: [Bug]: Large Data Parallel Size Cause Loading Safetensors Extremely Slow

| 字段 | 值 |
| --- | --- |
| Issue | [#17783](https://github.com/vllm-project/vllm/issues/17783) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Large Data Parallel Size Cause Loading Safetensors Extremely Slow

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Node size =2, DP 16, TP1, Deepseek-V3 model. It took ~ 10 min to load all the safetensors, compared to ncalls tottime percall cumtime percall filename:lineno(function) 3 20.638 6.879 20.638 6.879 /usr/local/lib/python3.12/dist-packages/zmq/sugar/poll.py:80(poll) 21 6.544 0.312 6.544 0.312 {method 'poll' of 'select.poll' objects} 9 0.421 0.047 0.421 0.047 /usr/local/lib/python3.12/dist-packages/vllm/third_party/pynvml.py:2373(nvmlInitWithFlags) 1 0.208 0.208 0.208 0.208 {built-in method from_file} 9 0.071 0.008 0.071 0.008 /usr/local/lib/python3.12/dist-packages/vllm/third_party/pynvml.py:2603(nvmlDeviceGetHandleByIndex) 11 0.062 0.006 0.062 0.006 /usr/lib/python3.12/json/decoder.py:344(raw_decode) 1 0.042 0.042 0.042 0.042 {method 'get_vocab' of 'tokenizers.Tokenizer' objects} 9 0.032 0.004 0.032 0.004 /usr/local/lib/python3.12/dist-packages/vllm/third_party/pynvml.py:2428(nvmlShutdown) 17 0.029 0.002 0.040 0.002 {method 'read' of '_io.TextIOWrapper' objects} 38 0.011 0.000 0.011 0.000 {built-in method _codecs.utf_8_decode} 5704/64 0.010 0.000 0.013 0.000 {built-in method _abc._abc_subclasscheck} 4 0.010 0.002 0.010 0.002 {method...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: lt-in method __new__ of type object at 0xa20960} ``` To reproduce: ``` import argparse import functools import json import os import pathlib import random import time from typing import Dict, List, Tuple import multipro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ]: Large Data Parallel Size Cause Loading Safetensors Extremely Slow bug;stale ### Your current environment ### 🐛 Describe the bug Node size =2, DP 16, TP1, Deepseek-V3 model. It took ~ 10 min to load all the safetensor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: ict, List, Tuple import multiprocessing import click import generate_ob_tests import pandas as pd import yaml from loguru import logger from packaging import version from tabulate import tabulate import torch.profiler i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 0.005 0.000 0.018 0.001 /usr/lib/python3.12/inspect.py:1239(getblock) 1 0.004 0.004 0.217 0.217 /usr/local/lib/python3.12/dist-packages/transformers/tokenization_utils_fast.py:98(__init__) 28420/28237 0.004 0.000 0.006...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: onment ### 🐛 Describe the bug Node size =2, DP 16, TP1, Deepseek-V3 model. It took ~ 10 min to load all the safetensors, compared to ncalls tottime percall cumtime percall filename:lineno(function) 3 20.638 6.879 20.638...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
