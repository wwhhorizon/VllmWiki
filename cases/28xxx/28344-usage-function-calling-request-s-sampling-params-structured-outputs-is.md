# vllm-project/vllm#28344: [Usage]: Function calling Request's sampling_params.structured_outputs is None?

| 字段 | 值 |
| --- | --- |
| Issue | [#28344](https://github.com/vllm-project/vllm/issues/28344) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Function calling Request's sampling_params.structured_outputs is None?

### Issue 正文摘录

Hi, I used openai server API to build a LLM backend when I tried to deploy a MCP server. I discovered that the prompt of vllm engine combined system prompt, tool lists and user prompt. but i saw sampling_params.structured_outputs is None. Although the result seemed correct， I think it's important to use structured output when generating function calling.But why not use structured output when generate JSON? Please explain，thanks a lot. Below start a vllm backend. ``` python -m vllm.entrypoints.openai.api_server \ --model /workspace/models/qwen-2.5B/models--Qwen--Qwen2.5-1.5B-Instruct/snapshots/989aa7980e4cf806f80c7fef2b1adb7bc71aa306/ \ --served-model-name "qwen-2.5b" \ --port 8000 \ --trust-remote-code \ --enable-auto-tool-choice \ --tool-call-parser hermes ``` Below is input of vllm engine. ``` (APIServer pid=703600) > /workspace/vllm/vllm/entrypoints/openai/serving_chat.py(326)create_chat_completion() (APIServer pid=703600) -> generator = self.engine_client.generate( (APIServer pid=703600) [' system\nYou are Qwen, created by Alibaba Cloud. You are a helpful assistant.\n\n# Tools\n\nYou may call one or more functions to assist with the user query.\n\nYou are provided with functio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: params.structured_outputs is None? usage Hi, I used openai server API to build a LLM backend when I tried to deploy a MCP server. I discovered that the prompt of vllm engine combined system prompt, tool lists and user p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t a vllm backend. ``` python -m vllm.entrypoints.openai.api_server \ --model /workspace/models/qwen-2.5B/models--Qwen--Qwen2.5-1.5B-Instruct/snapshots/989aa7980e4cf806f80c7fef2b1adb7bc71aa306/ \ --served-model-name "qwe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Function calling Request's sampling_params.structured_outputs is None? usage Hi, I used openai server API to build a LLM backend when I tried to deploy a MCP server. I discovered that the prompt of vllm engine...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: finish_reason=stop, stop_reason=None)], finished=True, metrics=RequestStateStats(num_generation_tokens=43, arrival_time=1762590097.5898013, queued_ts=2224082.281896018, scheduled_ts=2224082.282071909, first_token_ts=222...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tured_outputs is None? usage Hi, I used openai server API to build a LLM backend when I tried to deploy a MCP server. I discovered that the prompt of vllm engine combined system prompt, tool lists and user prompt. but i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
