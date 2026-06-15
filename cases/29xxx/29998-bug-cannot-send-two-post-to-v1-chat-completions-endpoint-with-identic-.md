# vllm-project/vllm#29998: [Bug]: cannot send two POST to /v1/chat/completions endpoint with identic tool function name with model GPT-OSS-120B

| 字段 | 值 |
| --- | --- |
| Issue | [#29998](https://github.com/vllm-project/vllm/issues/29998) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: cannot send two POST to /v1/chat/completions endpoint with identic tool function name with model GPT-OSS-120B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This bash script cannot be executed a second time, unless the name of the function is changed to a value which was not yet sent. Without tool definition, the POST can be sent as often as you like. ```bash #!/bin/bash curl -X POST http://localhost:8000/v1/chat/completions \ -H "Authorization: Bearer ${VLLM_API_KEY}" \ -H "Content-Type: application/json" \ -d '{ "model": "openai/gpt-oss-120b", "stream": false, "messages": [ { "role": "system", "content": "Be a helpful assistant." }, { "role": "user", "content": "Hi" }, { "role": "assistant", "content": "How can I help you?" }, { "role": "user", "content": "Do you like Monty Python?" } ], "tools": [ { "type": "function", "function": { "name": "CHANGE-NAME-BEFORE-SENDING", "description": "Use this tool if you need to extract information from a website.", "parameters": { "type": "object", "properties": { "url": { "type": "string", "description": "The URL to search or extract information from." } }, "required": ["url"] } } } ] }' ``` The script doesn't finish waiting for a response and `nvidia-smi` shows the cards consuming max power. The vllm logs show that there are tokens generated,...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ST to /v1/chat/completions endpoint with identic tool function name with model GPT-OSS-120B bug ### Your current environment ### 🐛 Describe the bug This bash script cannot be executed a second time, unless the name of t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: call it with python SDK, it is working fine, e.g. ```python from openai import OpenAI from dotenv import load_dotenv import os load_dotenv() client = OpenAI( api_key=os.getenv("API_KEY"), base_url="http://localhost:8000...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: "type": "string", "description": "The URL to search or extract information from." } }, "required": ["url"] } } } ] }' ``` The script doesn't finish waiting for a response and `nvidia-smi` shows the
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: se ) print(response.choices[0].message) ``` In fact this can also be reproduced using n8n, AI Agent nodes which are based on the typescipt langgraph implementation: https://github.com/n8n-io/n8n/blob/master/packages/%40...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tion/json" \ -d '{ "model": "openai/gpt-oss-120b", "stream": false, "messages": [ { "role": "system", "content": "Be a helpful assistant." }, { "role": "user", "content": "Hi" }, { "role": "assistant",

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
