# vllm-project/vllm#16880: [Bug]: [v0.8.4][Critical] Tools calling broken: xgrammar rejects minItems in JSON Schema, blocking agent functionality

| 字段 | 值 |
| --- | --- |
| Issue | [#16880](https://github.com/vllm-project/vllm/issues/16880) |
| 状态 | closed |
| 标签 | bug;structured-output;tool-calling |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [v0.8.4][Critical] Tools calling broken: xgrammar rejects minItems in JSON Schema, blocking agent functionality

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the OpenAI‐compatible tool‐calling interface with `--guided-decoding-backend xgrammar` and `tool_choice="required"`, the client auto‑injects a JSON Schema for the array of tool calls that contains `"minItems": 1`. vLLM’s xgrammar backend currently [rejects any schema with minItems](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/guided_decoding/utils.py#L6), resulting in: ```javascript openai.BadRequestError: Error code: 400 - { 'message': 'The provided JSON schema contains features not supported by xgrammar.', … } ``` As a result, tool-calling with agents is completely disabled in this configuration. If I switch to `tool_choice="auto"`, the error disappears but the model never emits any tool_calls (so `response.choices[0].message.tool_calls` is empty and I get an IndexError). ## To reproduce ```python import os, json from openai import OpenAI from dotenv import load_dotenv load_dotenv() client = OpenAI( base_url=os.getenv("VLLM_ENDPOINT"), # e.g. http://localhost:8000 api_key="****", # redacted ) def get_weather(location: str, unit: str): return f"Getting the weather for {location} in {unit}…" tools...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ol_calls` is empty and I get an IndexError). ## To reproduce ```python import os, json from openai import OpenAI from dotenv import load_dotenv load_dotenv() client = OpenAI( base_url=os.getenv("VLLM_ENDPOINT"), # e.g....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ing the OpenAI‐compatible tool‐calling interface with `--guided-decoding-backend xgrammar` and `tool_choice="required"`, the client auto‑injects a JSON Schema for the array of tool calls that contains `"minItems": 1`. v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: M! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: chema with minItems](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/guided_decoding/utils.py#L6), resulting in: ```javascript openai.BadRequestError: Error code: 400 - { 'message': 'The provided JSON...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: choices[0].message.tool_calls` is empty and I get an IndexError). ## To reproduce ```python import os, json from openai import OpenAI from dotenv import load_dotenv load_dotenv() client = OpenAI( base_url=os.getenv("VLL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
