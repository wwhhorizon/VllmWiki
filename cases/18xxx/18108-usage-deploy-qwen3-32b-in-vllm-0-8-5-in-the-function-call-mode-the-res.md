# vllm-project/vllm#18108: [Usage]: Deploy Qwen3-32B in vLLM 0.8.5. In the function_call mode, the results of streaming calls and non-streaming calls are inconsistent.

| 字段 | 值 |
| --- | --- |
| Issue | [#18108](https://github.com/vllm-project/vllm/issues/18108) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Deploy Qwen3-32B in vLLM 0.8.5. In the function_call mode, the results of streaming calls and non-streaming calls are inconsistent.

### Issue 正文摘录

### Your current environment 1、deploy Qwen3-32B python -m vllm.entrypoints.openai.api_server \ --model /data/ai-center/model_dir/Qwen3-32B \ --served_model_name=qwen3 \ --dtype=half --trust_remote_code --gpu_memory_utilization=0.8 \ --tensor-parallel-size 2 \ --max_model_len=12288 --disable_log_requests \ --tool-call-parser hermes --enable-auto-tool-choice \ --host 0.0.0.0 --port 4203 2、 Invoke function_call { "messages": [ { "role": "user", "content": "比较1.2和1.5的大小" } ], "temperature": 0.8, "max_tokens": 128, "stream": false, "model": "qwen3", "presence_penalty":1.5, "chat_template_kwargs": {"enable_thinking": false}, "tools" : [ { "type": "function", "function": { "name": "than_size", "description": "比较两个数的大小\\n\\n Args:\\n a: 数字\\n b: 数字\\n ", "parameters": { "properties": { "a": { "title": "A", "type": "number" }, "b": { "title": "B", "type": "number" } }, "required": [ "a", "b" ] } } } ] } 3、 Non-streaming response is correct "tool_calls": [ { "id": "chatcmpl-tool-8926bd6287b945e5bad62a6883df07b7", "type": "function", "function": { "name": "than_size", "arguments": "{\"a\": 1.2, \"b\": 1.5}" } } ] 4、 streaming response is bad data: {"id":"chatcmpl-96d222cc74c64e46a0807f0e95ea...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Deploy Qwen3-32B in vLLM 0.8.5. In the function_call mode, the results of streaming calls and non-streaming calls are inconsistent. usage;stale ### Your current environment 1、deploy Qwen3-32B python -m vllm.ent...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: sults of streaming calls and non-streaming calls are inconsistent. usage;stale ### Your current environment 1、deploy Qwen3-32B python -m vllm.entrypoints.openai.api_server \ --model /data/ai-center/model_dir/Qwen3-32B \...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ta/ai-center/model_dir/Qwen3-32B \ --served_model_name=qwen3 \ --dtype=half --trust_remote_code --gpu_memory_utilization=0.8 \ --tensor-parallel-size 2 \ --max_model_len=12288 --disable_log_requests \ --tool-call-parser...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ], "temperature": 0.8, "max_tokens": 128, "stream": false, "model": "qwen3", "presence_penalty":1.5, "chat_template_kwargs": {"enable_thinking": false}, "tools" : [ { "type": "function", "function": { "name": "

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
