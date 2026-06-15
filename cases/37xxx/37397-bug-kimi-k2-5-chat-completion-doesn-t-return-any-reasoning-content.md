# vllm-project/vllm#37397: [Bug]: Kimi-K2.5 chat completion doesn't return any reasoning content

| 字段 | 值 |
| --- | --- |
| Issue | [#37397](https://github.com/vllm-project/vllm/issues/37397) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Kimi-K2.5 chat completion doesn't return any reasoning content

### Issue 正文摘录

### Your current environment `vllm-openai:v0.17.1` running with ``` non-default args: {'enable_auto_tool_choice': True, 'tool_call_parser': 'kimi_k2', 'host': '0.0.0.0', 'trust_remote_code': True, 'served_model_name': ['moonshotai/Kimi-K2.5'], 'load_format': 'runai_streamer', 'reasoning_parser': 'kimi_k2', 'tensor_parallel_size': 4, 'gpu_memory_utilization': 0.95, 'enable_prefix_caching': True, 'mm_encoder_tp_mode': 'data'} ``` ### 🐛 Describe the bug When using Kimi-K2.5 with vLLM's `kimi_k2` reasoning parser, streaming responses contain only `delta.content` and no `delta.reasoning`, even with `thinking=true`. ## Reproduction ```python URL = "http://localhost/v1/chat/completions" payload = { "model": "moonshotai/Kimi-K2.5", "messages": [{"role": "user", "content": "What is a mutex?"}], "stream": True, "extra_body": {"chat_template_kwargs": {"thinking": True}} } with requests.post(URL, json=payload, stream=True, headers=headers) as r: r.raise_for_status() for line in r.iter_lines(): if not line: continue print(line) ``` Output: ``` $ uv run stream.py b'data: {"id":"chatcmpl-ae276bc67b7c5185","created":1773821726,"model":"moonshotai/Kimi-K2.5","object":"chat.completion.chunk","choic...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: arser': 'kimi_k2', 'host': '0.0.0.0', 'trust_remote_code': True, 'served_model_name': ['moonshotai/Kimi-K2.5'], 'load_format': 'runai_streamer', 'reasoning_parser': 'kimi_k2', 'tensor_parallel_size': 4, 'gpu_memory_util...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ld. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: , "extra_body": {"chat_template_kwargs": {"thinking": True}} } with requests.post(URL, json=payload, stream=True, headers=headers) as r: r.raise_for_status() for line in r.iter_lines(): if not line: continue print(line)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
