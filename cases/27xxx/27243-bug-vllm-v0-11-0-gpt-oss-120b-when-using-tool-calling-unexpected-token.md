# vllm-project/vllm#27243: [Bug]: [vLLM v0.11.0 + GPT-OSS-120B]: when using tool calling, Unexpected token 200012 while expecting start token 200006 error occurred with a probability of approximately 10–20%.

| 字段 | 值 |
| --- | --- |
| Issue | [#27243](https://github.com/vllm-project/vllm/issues/27243) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: [vLLM v0.11.0 + GPT-OSS-120B]: when using tool calling, Unexpected token 200012 while expecting start token 200006 error occurred with a probability of approximately 10–20%.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running a simple tool calling example using gpt-oss-120b in vLLM v0.11.0, the following error occurs with a probability of approximately 10–20%. ```text Unexpected token 200012 while expecting start token 200006 ``` The tool calling example code is as follows. ```python from openai import OpenAI import json client = OpenAI(base_url="http://YOUR_ENDPOINT_URL/v1", api_key="dummy") def add_num(int_a: int, int_b: int): return f"{int_a} + {int_b} = {int_a+int_b}" tools = [{ "type": "function", "function": { "name": "calculator", "description": "add two numbers.", "parameters": { "type": "object", "properties": { "int_a": {"type": "int", "description": "number 1"}, "int_b": {"type": "int", "description": "number 2"} }, "required": ["int_a", "int_b"] } } }] from tqdm import tqdm # print(response) for i in tqdm(range(1000)): response = client.chat.completions.create( model=client.models.list().data[0].id, messages=[ {"role": "developer", "content": "You are a personal math agent. Please select a tool among tools provided."}, {"role": "user", "content": "add 3 to 5"} ], tools=tools, tool_choice="auto", # reasoning_effort="high", temp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ``` The tool calling example code is as follows. ```python from openai import OpenAI import json client = OpenAI(base_url="http://YOUR_ENDPOINT_URL/v1", api_key="dummy") def add_num(int_a: int, int_b: int): return f"{in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: [vLLM v0.11.0 + GPT-OSS-120B]: when using tool calling, Unexpected token 200012 while expecting start token 200006 error occurred with a probability of approximately 10–20%. bug ### Your current environment ### 🐛...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: max_tokens=16384, stream=True ) is_tool_response = False content = "" reasoning_content = "" tool_name = "" for chunk in response: if hasattr(chunk.choices[0].delta, "tool_calls") and chunk.choices[0].delta.tool_calls i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
