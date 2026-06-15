# vllm-project/vllm#39948: [Bug]: Gemma4 Auto Tool Parsing via Responses API

| 字段 | 值 |
| --- | --- |
| Issue | [#39948](https://github.com/vllm-project/vllm/issues/39948) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma4 Auto Tool Parsing via Responses API

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Gemma4 tool calls emitted via the Responses API are left as plain `call:...{...}` text instead of being parsed into `function_call` output items, likely because `skip_special_tokens` is not disabled for `ResponsesRequest` in: https://github.com/vllm-project/vllm/blob/c77e596e2eb6627d9f126436733550f2e31f642d/vllm/tool_parsers/gemma4_tool_parser.py#L359-L370 The bug can be reproduced with the following Python script: ```python import json from openai import OpenAI client = OpenAI(base_url="http://127.0.0.1:11434/v1", api_key="EMPTY") def get_system_setpoints(): return {"InputAirFlow": 1.0, "InputWaterFlow": 1.0} tools = [ { "type": "function", "name": "get_system_setpoints", "description": "Return the current system setpoints.", "parameters": {"type": "object", "properties": {}, "additionalProperties": False}, "strict": True, } ] r = client.responses.create( model="google/gemma-4-E4B-it", input="Call get_system_setpoints now. Do not explain.", tools=tools, tool_choice="auto", reasoning={"effort": "high"}, max_output_tokens=256, ) print(r.model_dump_json(indent=2)) calls = [item for item in r.output if item.type == "function_call"]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: being parsed into `function_call` output items, likely because `skip_special_tokens` is not disabled for `ResponsesRequest` in: https://github.com/vllm-project/vllm/blob/c77e596e2eb6627d9f126436733550f2e31f642d/vllm/too...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma4 Auto Tool Parsing via Responses API bug ### Your current environment ### 🐛 Describe the bug Gemma4 tool calls emitted via the Responses API are left as plain `call:...{...}` text instead of being parsed in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tems, likely because `skip_special_tokens` is not disabled for `ResponsesRequest` in: https://github.com/vllm-project/vllm/blob/c77e596e2eb6627d9f126436733550f2e31f642d/vllm/tool_parsers/gemma4_tool_parser.py#L359-L370...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: }'` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
