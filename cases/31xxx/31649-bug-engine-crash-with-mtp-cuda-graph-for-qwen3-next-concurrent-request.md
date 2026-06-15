# vllm-project/vllm#31649: [Bug]: Engine crash with MTP + CUDA-Graph for Qwen3-Next (concurrent requests = 3)

| 字段 | 值 |
| --- | --- |
| Issue | [#31649](https://github.com/vllm-project/vllm/issues/31649) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine crash with MTP + CUDA-Graph for Qwen3-Next (concurrent requests = 3)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug #### Description When deploying the Qwen3-Next model using vLLM with **both MTP (num_speculative_tokens=3) and CUDA-Graph enabled**, the engine crashes when there are exactly **3 concurrent decode requests**. The crash triggers the following error: `ValueError: Counters can only be incremented by non-negative amounts.` #### Steps to Reproduce I have attached my server script and client script below: server script: ```shell #!/bin/bash PORT=8235 TP=4 MODEL_DIR=Qwen/Qwen3-Next-80B-A3B-Instruct echo "MODEL_DIR: $MODEL_DIR" env_vars=( # "CUDA_LAUNCH_BLOCKING=0" ) for var in "${env_vars[@]}"; do var_name="${var%%=*}" var_value="${var#*=}" echo -e "\t$var_name=$var_value" done CMD=( env ) for var in "${env_vars[@]}"; do CMD+=( "$var" ) done CMD+=( $MODEL_DIR --port "$PORT" --gpu-memory-utilization 0.9 -tp $TP # --enforce-eager --no-enable-prefix-caching --enable-chunked-prefill --max-num-batched-tokens 8192 --distributed-executor-backend mp --block-size 64 --max-num-seqs 256 # --compilation-config "{\"cudagraph_capture_sizes\": [1,2,3,4]}" --speculative-config "{\"method\": \"qwen3_next_mtp\", \"num_speculative_tokens\": 3}" ) echo -e...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Engine crash with MTP + CUDA-Graph for Qwen3-Next (concurrent requests = 3) bug;stale ### Your current environment ### 🐛 Describe the bug #### Description When deploying the Qwen3-Next model using vLLM with **bot...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: CMD[@]}" ``` client scripts: ```python #!/usr/bin/env python from enum import Enum, auto from typing import List import requests import multiprocessing as mp import sys class TestType(Enum): Dummy = auto() Real = auto()...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: A3B-Instruct echo "MODEL_DIR: $MODEL_DIR" env_vars=( # "CUDA_LAUNCH_BLOCKING=0" ) for var in "${env_vars[@]}"; do var_name="${var%%=*}" var_value="${var#*=}" echo -e "\t$var_name=$var_value" done CMD=( env ) for var in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Engine crash with MTP + CUDA-Graph for Qwen3-Next (concurrent requests = 3) bug;stale ### Your current environment ### 🐛 Describe the bug #### Description When deploying the Qwen3-Next model using vLLM with **bot...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Engine crash with MTP + CUDA-Graph for Qwen3-Next (concurrent requests = 3) bug;stale ### Your current environment ### 🐛 Describe the bug #### Description When deploying the Qwen3-Next model using vLLM with **bot...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
