# vllm-project/vllm#21037: [Bug]: TTFT of 1p1d using NIXLConnector is twice that of tp1

| 字段 | 值 |
| --- | --- |
| Issue | [#21037](https://github.com/vllm-project/vllm/issues/21037) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TTFT of 1p1d using NIXLConnector is twice that of tp1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am attempting to implement PD disaggregation for 1p1d using NIXLConnector, but I’ve observed that its TTFT is twice that of tp1 when concurrency is set to 1. After checking the metrics for the decode instance via `curl http://0.0.0.0:8200/metrics`, I noticed that the decode instance is reporting prefill latency, which matches the prefill latency seen on the prefill instance. It seems that the decode instance is redundantly executing the prefill computation, causing the 1p1d TTFT to exceed the expected duration. Here is the script I used to run PD disaggregation: ``` MODEL="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B" CONNECTOR="NixlConnector" trap 'kill $(jobs -pr)' SIGINT SIGTERM EXIT trap 'kill $(jobs -pr)' EXIT # Trap the SIGINT signal (triggered by Ctrl+C) trap 'cleanup' INT wait_for_server() { local port=$1 timeout 1200 bash -c " until curl -s localhost:${port}/v1/chat/completions > /dev/null; do sleep 1 done" && return 0 || return 1 } cleanup() { echo "Stopping everything…" trap - INT TERM # prevent re-entrancy kill -- -$$ # negative PID == “this whole process-group” wait # reap children so we don't leave zombies exit 0 } ru...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ected duration. Here is the script I used to run PD disaggregation: ``` MODEL="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B" CONNECTOR="NixlConnector" trap 'kill $(jobs -pr)' SIGINT SIGTERM EXIT trap 'kill $(jobs -pr)' EXIT...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: TTFT of 1p1d using NIXLConnector is twice that of tp1 bug;stale ### Your current environment ### 🐛 Describe the bug I am attempting to implement PD disaggregation for 1p1d using NIXLConnector, but I’ve observed t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: .0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project import argparse import os import time from contextlib import asynccontextmanager import httpx import numpy as np from fastapi import FastAPI, Reque...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: response.raise_for_status() async for chunk in response.aiter_bytes(): yield chunk @app.post("/v1/completions") async def handle_completions(request: Request): global counter, stats_calculator counter += 1 st = time.tim...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: prefilling instance, which is the KV producer PREFILL_PORT=8100 CUDA_VISIBLE_DEVICES=0 VLLM_NIXL_SIDE_CHANNEL_PORT=5559 vllm serve /home/hadoop-dpsr/dolphinfs_hdd_hadoop-dpsr/dongyanchu/data/huggingface.co/$model_name \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
