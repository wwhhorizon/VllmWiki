# vllm-project/vllm#14372: [Bug]: VLLM process dies when trying to profile with nsight systemss

| 字段 | 值 |
| --- | --- |
| Issue | [#14372](https://github.com/vllm-project/vllm/issues/14372) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM process dies when trying to profile with nsight systemss

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am attempting to profile a llama 70B model with tp=8 but it fails and hits the following error: ``` ERROR 03-06 08:47:40 multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 14538 died, exit code: -11 INFO 03-06 08:47:40 multiproc_worker_utils.py:123] Killing local vLLM worker processes ERROR 03-06 08:47:40 multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 14538 died, exit code: -11 ``` I am running with `nsys profile -s none -t nvtx,cuda --cudabacktrace=all --cuda-graph-trace=node --python-backtrace=cuda --wait all -o vllm-llama70b --force-overwrite true --capture-range=cudaProfilerApi --capture-range-end=stop python vllm_test_new.py --model "meta-llama/Llama-3.1-70B" --batch-size 4 --num-input-tokens 65536 --num-output-tokens 10 --tensor-parallel-size 8 --benchmark-profile` On the following simple script ```python import argparse import asyncio import random import tqdm import time from typing import List from vllm import LLM, SamplingParams from vllm.engine.async_llm_engine import AsyncLLMEngine, AsyncEngineArgs from vllm.inputs.data import TokensPrompt import torch def get_random_prompt_tokens(tokenizer, nu...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Bug]: VLLM process dies when trying to profile with nsight systemss bug ### Your current environment ### 🐛 Describe the bug I am attempting to profile a llama 70B model with tp=8 but it fails and hits the following err...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: el-size 8 --benchmark-profile` On the following simple script ```python import argparse import asyncio import random import tqdm import time from typing import List from vllm import LLM, SamplingParams from vllm.engine....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: model=model, tensor_parallel_size=tensor_parallel_size, dtype="bfloat16", max_num_batched_tokens=batch_size * (num_input_tokens + num_output_tokens), max_seq_len_to_capture=num_input_tokens + num_output_tokens ) # ray_w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: put_tokens ) # ray_workers_use_nsight=True, distributed_executor_backend="ray" sampling_params = SamplingParams( temperature=0.8, top_p=0.95, min_tokens=num_output_tokens, max_tokens=num_output_tokens ) tokenizer = llm....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed, exit code: -11 ``` I am running with `nsys profile -s none -t nvtx,cuda --cudabacktrace=all --cuda-graph-trace=node --python-backtrace=cuda --wait all -o vllm-llama70b --force-overwrite true --capture-range=cudaProf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
