# vllm-project/vllm#23787: [Bug]: Performance Analysis: Significant Latency on First Inference due to Engine Warm-up (torch.compile & Graph Capture)

| 字段 | 值 |
| --- | --- |
| Issue | [#23787](https://github.com/vllm-project/vllm/issues/23787) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale;startup-ux |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Performance Analysis: Significant Latency on First Inference due to Engine Warm-up (torch.compile & Graph Capture)

### Issue 正文摘录

Your current environment ### 🐛 Describe the bug I'm currently performing a detailed performance analysis of the difference in inference time between the first inference after model loading and subsequent inferences. My findings confirm the existence of a significant warmup overhead, and I'd like to share my analysis. To Reproduce: The tests were run using an automated script that loads two models in sleep mode and alternates prompts. The core logic is in the script below: ``` import subprocess import os import time import requests import signal import sys import atexit from openai import OpenAI from typing import Optional, Dict # Global list to track all child processes child_processes = [] # Global timing dictionary timing_data = {} def terminate_process(process): """Safely terminate a process and remove it from tracking""" try: if process.poll() is None: process.terminate() process.wait(timeout=5) except subprocess.TimeoutExpired: process.kill() except Exception as e: print(f"Error terminating process: {e}") finally: if process in child_processes: child_processes.remove(process) def cleanup_processes(): """Kill all child processes""" for process in child_processes: terminate_pro...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: sis: Significant Latency on First Inference due to Engine Warm-up (torch.compile & Graph Capture) bug;torch.compile;stale;startup-ux Your current environment ### 🐛 Describe the bug I'm currently performing a detailed pe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: is of the difference in inference time between the first inference after model loading and subsequent inferences. My findings confirm the existence of a significant warmup overhead, and I'd like to share my analysis. To...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: due to Engine Warm-up (torch.compile & Graph Capture) bug;torch.compile;stale;startup-ux Your current environment ### 🐛 Describe the bug I'm currently performing a detailed performance analysis of the difference in infe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Performance Analysis: Significant Latency on First Inference due to Engine Warm-up (torch.compile & Graph Capture) bug;torch.compile;stale;startup-ux Your current environment ### 🐛 Describe the bug I'm currently...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: nforce-eager' # '--compilation-config', '{"use_inductor": true, "backend": "inductor", "cudagraph_mode": "NONE", "cudagraph_num_of_warmups": 0}', '--compilation-config', '{"full_cuda_graph": true}' ] if enable_sleep_mod...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23789: Should have ROCm label: NO (0 matches) #23787: Should have ROCm label: NO (0 matches) #23786: Should have ROCm label: NO (0 matches) #23784: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
