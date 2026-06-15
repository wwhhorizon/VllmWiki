# vllm-project/vllm#11603: [Bug]: AsyncEngine Backend loop is stopped

| 字段 | 值 |
| --- | --- |
| Issue | [#11603](https://github.com/vllm-project/vllm/issues/11603) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AsyncEngine Backend loop is stopped

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug - I use the djl serving + vllm to inference ``` docker images: 727897471807.dkr.ecr.cn-north-1.amazonaws.com.cn/djl-inference:0.31.0-lmi13.0.0-cu124 ``` - I need a stream output, so I use the AsyncEngine in model.py ``` import torch import logging import math import os import transformers import torch from djl_python import Input, Output from transformers import pipeline, AutoModel, AutoTokenizer, AutoModelForCausalLM from vllm import LLM, SamplingParams from vllm.engine.arg_utils import AsyncEngineArgs from vllm.engine.async_llm_engine import AsyncLLMEngine import asyncio import uuid from threading import Thread from queue import Queue, Empty engine = None tokenizer = None def init_llm(properties): print('============================🚀load tokenizer🚀====================') tokenizer = AutoTokenizer.from_pretrained(properties['model_id'], trust_remote_code=True) print('============================🚀load model🚀====================') engine_args = AsyncEngineArgs( model = properties['model_id'], max_model_len = int(properties["max_model_len"]), tensor_parallel_size=int(properties["tensor_parallel_de...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### 🐛 Describe the bug - I use the djl serving + vllm to inference ``` docker images: 727897471807.dkr.ecr.cn-north-1.amazonaws.com.cn/djl-inference:0.31.0-lmi13.0.0-cu124 ``` - I need a stream output, so I use the Asyn...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: AsyncEngine Backend loop is stopped bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug - I use the djl serving + vllm to inference ``` docker images: 727897471807.dk...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: AsyncEngine Backend loop is stopped bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug - I use the djl serving + vllm to inference ``` docker images: 727897471807.dk...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r** ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: cess W-1058-model-stdout: INFO 12-29 14:32:59 metrics.py:467] Avg prompt throughput: 0.5 tokens/s, Avg generation throughput: 0.2 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
