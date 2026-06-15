# vllm-project/vllm#9048: [Bug]: IndexError when sending a streaming request with tool use

| 字段 | 值 |
| --- | --- |
| Issue | [#9048](https://github.com/vllm-project/vllm/issues/9048) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: IndexError when sending a streaming request with tool use

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I run the server with Mistral with auto-tool support ``` vllm serve mistralai/Mistral-7B-Instruct-v0.3 --enable-auto-tool-choice --tool-call-parser mistral --chat-template tool_chat_template_mistral.jinja ``` and send the following streaming request to `/v1/chat/completions` ``` { "model": "mistralai/Mistral-7B-Instruct-v0.3", "tool_choice": {"type": "function", "function": {"name": "get_current_weather"}}, "stream": true, "messages": [ { "role": "user", "content": "What is the weather like in California?" } ], "tools": [ { "type": "function", "function": { "name": "get_current_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": { "description": "The city, e.g. San Francisco, CA", "type": "string" }, "unit": { "enum": ["celsius", "fahrenheit"], "type": "string" } }, "required": ["location"] } } } ] } ``` the response stream does not contain the `data: [DONE]` message and the logs show an Exception being raised: ``` INFO 10-03 17:08:20 logger.py:36] Received request chat-0f80f7a4a8054f9582b94130483e7cd4: promp...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ['location']}, regex=None, choice=None, grammar=None, json_object=None, backend=None, whitespace_pattern=None), prompt_token_ids: [1, 6, 1501, 7567, 1891, 2032, 1113, 3396, 1316, 1113, 3396, 2032, 10598, 1629, 2032, 111...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: , temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: using a Mistral model... INFO 10-03 17:08:24 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: "location": { "description": "The city, e.g. San Francisco, CA", "type": "string" }, "unit": { "enum": ["celsius", "fahrenheit"], "t
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. Compiling FSM index for all state transitions: 100%|███████████████████████████████████████████| 5...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
