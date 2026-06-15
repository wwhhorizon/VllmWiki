# vllm-project/vllm#22762: [Bug]: Internal Server Error 'Encoding' object has no attribute 'items' When Using Mistral Tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#22762](https://github.com/vllm-project/vllm/issues/22762) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Internal Server Error 'Encoding' object has no attribute 'items' When Using Mistral Tokenizer

### Issue 正文摘录

### Your current environment This can be reproduced with the vllm/vllm-openai:v0.10.0 image using the below docker compose (This was run on an L40s GPU (g6e.xlarge instance in AWS): ``` services: vllm: container_name: vllm restart: unless-stopped networks: - 'vllm' image: vllm/vllm-openai:v0.10.0 deploy: resources: reservations: devices: - driver: nvidia count: 1 capabilities: [gpu] ports: - 8000:8000 command: - "--model" - "mistralai/Mistral-Nemo-Instruct-2407" - "--max-model-len" - "30000" - "--tokenizer-mode" - "mistral" environment: HF_TOKEN: networks: vllm: ``` ### 🐛 Describe the bug When sending multiple concurrent requests to a vLLM instance running a Mistral model such as mistralai/Mistral-Nemo-Instruct-2407 and specifying the mistral tokenizer, vLLM is returning a 500 Internal Server Error with the message "'Encoding' object has no attribute 'items'". This error does not appear when running vLLM v0.9.1, but does occur when running v0.10.0. The error also only occurs when "--tokenizer mistral" is passed, omitting this input prevents the error from occurring. Example script to reproduce error: ``` import json import os import time import threading import urllib.error import...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: an be reproduced with the vllm/vllm-openai:v0.10.0 image using the below docker compose (This was run on an L40s GPU (g6e.xlarge instance in AWS): ``` services: vllm: container_name: vllm restart: unless-stopped network...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: s: vllm: ``` ### 🐛 Describe the bug When sending multiple concurrent requests to a vLLM instance running a Mistral model such as mistralai/Mistral-Nemo-Instruct-2407 and specifying the mistral tokenizer, vLLM is returni...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: og) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: capabilities: [gpu] ports: - 8000:8000 command: - "--model" - "mistralai/Mistral-Nemo-Instruct-2407" - "--max-model-len" - "30000" - "--tokenizer-mode" - "mistral" environment: HF_TOKEN: networks: vllm: ``` ### 🐛 Descri...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
