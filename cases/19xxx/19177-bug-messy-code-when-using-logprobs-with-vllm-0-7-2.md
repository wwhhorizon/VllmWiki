# vllm-project/vllm#19177: [Bug]: messy code when using logprobs with vllm>0.7.2

| 字段 | 值 |
| --- | --- |
| Issue | [#19177](https://github.com/vllm-project/vllm/issues/19177) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: messy code when using logprobs with vllm>0.7.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Runing code like that gives me such output: ``` import requests import json api_key = "xxxx" base_url = "your base_url" headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"} input_params = { "messages": [ { "role": "user", "content": "今天天气不错" } ], "temperature": 0.1, "model": "/root/autodl-tmp/outputs/Qwen3-8B-0604/merged/", "logprobs": True, "top_logprobs": 5, "stream": False, "extra_body": { "chat_template_kwargs": { "enable_thinking": False } } } response = requests.post(f"{base_url}/chat/completions", json=input_params, headers=headers) print(response.json()['choices'][0]['logprobs']['content'][0]) ``` {'token': 'æĺ¯', 'logprob': -0.1649082601070404, 'bytes': [195, 166, 196, 186, 194, 175], 'top_logprobs': [{'token': 'æĺ¯', 'logprob': -0.1649082601070404, 'bytes': [195, 166, 196, 186, 194, 175]}, {'token': 'è°¢è°¢', 'logprob': -3.0399081707000732, 'bytes': [195, 168, 194, 176, 194, 162, 195, 168, 194, 176, 194, 162]}, {'token': 'åķĬ', 'logprob': -4.164908409118652, 'bytes': [195, 165, 196, 183, 196, 172]}, {'token': 'åĹ¯', 'logprob': -4.289908409118652, 'bytes': [195, 165, 196, 185, 194, 175]},...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: "content": "今天天气不错" } ], "temperature": 0.1, "model": "/root/autodl-tmp/outputs/Qwen3-8B-0604/merged/", "logprobs": True, "top_logprobs": 5, "stream": False, "extra_body": { "chat_template_kwargs": { "enable_thinking":...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: en is messy. It is supposed to output Chinese character. It can only be reproduced with vllm>0.7.2 for both qwen3 series and qwen 2.5 series while sglang working just fine. ### Before submitting a new issue... - [x] Mak...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### 🐛 Describe the bug Runing code like that gives me such output: ``` import requests import json api_key = "xxxx" base_url = "your base_url" headers = {"Content-Type": "application/json", "Authorization": f"Bearer {ap...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ne. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 4/merged/", "logprobs": True, "top_logprobs": 5, "stream": False, "extra_body": { "chat_template_kwargs": { "enable_thinking": False } } } response = requests.post(f"{base_url}/chat/completions", json=input_params, head...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
