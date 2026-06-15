# vllm-project/vllm#21711: [Bug]: Qwen3 tool call

| 字段 | 值 |
| --- | --- |
| Issue | [#21711](https://github.com/vllm-project/vllm/issues/21711) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3 tool call

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When Qwen3 performs `tool call`, `json.loads` throws an error because the output is ' \n{"name": "get_current_weather", "arguments": {"city": "Dallas", "state": "TX", "unit": "fahrenheit"}}\n '. Is there an automated way to parse this? ```python #!/usr/bin/env python3 # -*- coding: utf-8 -*- # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project # ruff: noqa import json import random import string from vllm import LLM from vllm.sampling_params import SamplingParams model_name = "/home/ubuntu/Large-Model/Qwen/Qwen3-4B" # or switch to "mistralai/Mistral-Nemo-Instruct-2407" # or "mistralai/Mistral-Large-Instruct-2407" # or any other mistral model with function calling ability sampling_params = SamplingParams(max_tokens=8192, temperature=0.0) llm = LLM( model=model_name, gpu_memory_utilization=0.8 ) def generate_random_id(length=9): characters = string.ascii_letters + string.digits random_id = "".join(random.choice(characters) for _ in range(length)) return random_id # simulate an API that can be called def get_current_weather(city: str, state: str, unit: "str"): return ( f"The weat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: because the output is ' \n{"name": "get_current_weather", "arguments": {"city": "Dallas", "state": "TX", "unit": "fahrenheit"}}\n '. Is there an automated way to parse this? ```python #!/usr/bin/env python3 # -*- coding...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3 tool call bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug When Qwen3 performs `tool call`, `json.loads` throws an error because the output is ' \n{"name": "get_current_weather", "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: renheit?", } ] chat_template_kwargs = { "enable_thinking": False } outputs = llm.chat(messages, sampling_params=sampling_params, tools=tools, chat_template_kwargs=chat_template_kwargs) output = outputs[0].outputs[0].tex...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Qwen3 tool call bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug When Qwen3 performs `tool call`, `json.loads` throws an error because the output is ' \n{"name": "get_current_weather", "...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
