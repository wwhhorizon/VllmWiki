# vllm-project/vllm#30939: [Bug]: The same input produces outputs of different lengths in the same batch.

| 字段 | 值 |
| --- | --- |
| Issue | [#30939](https://github.com/vllm-project/vllm/issues/30939) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The same input produces outputs of different lengths in the same batch.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the qwen3-32b model on release version 0.11.2, I noticed that even with the same prompt, when sending a batch of requests with a batch size of 8 to the server, the output lengths vary significantly, despite setting temperature=0 and seed=1234. longcase.ndjson: https://gist.github.com/sorenwu/23eafd14e82b6d86c08f33056f08d56d ``` import copy import json import sys import time import unicodedata from functools import partial from typing import List, Tuple from concurrent.futures import ThreadPoolExecutor, as_completed from multiprocessing import Value,Process,Manager,Lock import numpy as np # import matplotlib.pyplot as plt import random from openai import OpenAI from transformers import AutoTokenizer random.seed(1) CONFIG = { "model": "your_model_name", "shuffle_dataset": False, "port": 8021, "total_requests": 10, "ip":"0.0.0.0", "concurrency_levels": [8], "output_token_limit": 32678, "ignore_eos": False, "request_start_delay": 0, } manager = Manager() METRICS = manager.dict() GLOBAL_LOCK = Lock() class EnhancedSyncBenchmark: # def __init__(self): # self.req_list = self.load_dataset('') def generate_prompt(self, token_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### 🐛 Describe the bug When running the qwen3-32b model on release version 0.11.2, I noticed that even with the same prompt, when sending a batch of requests with a batch size of 8 to the server, the output lengths vary...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ## Your current environment ### 🐛 Describe the bug When running the qwen3-32b model on release version 0.11.2, I noticed that even with the same prompt, when sending a batch of requests with a batch size of 8 to the ser...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: nager() METRICS = manager.dict() GLOBAL_LOCK = Lock() class EnhancedSyncBenchmark: # def __init__(self): # self.req_list = self.load_dataset('') def generate_prompt(self, token_count): return "NVIDIA is a great company...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: .11.2, I noticed that even with the same prompt, when sending a batch of requests with a batch size of 8 to the server, the output lengths vary significantly, despite setting temperature=0 and seed=1234. longcase.ndjson...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
