# vllm-project/vllm#25001: [Bug]: GPT-OSS Tool Answer Role Object not working

| 字段 | 值 |
| --- | --- |
| Issue | [#25001](https://github.com/vllm-project/vllm/issues/25001) |
| 状态 | closed |
| 标签 | bug;tool-calling |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GPT-OSS Tool Answer Role Object not working

### Issue 正文摘录

### Your current environment ```sh docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \ -p 8000:8000 \ --ipc=host \ **vllm/vllm-openai:v0.10.2** \ --model openai/gpt-oss-20b --tool-call-parser openai \ --enable-auto-tool-choice ``` ### 🐛 Describe the bug while this body works: ```json { "model": "openai/gpt-oss-20b", "messages": [ { "role": "user", "content": [ { "text": "what is the weather in Paris", "type": "text" } ] }, { "role": "assistant", "tool_calls": [ { "function": { "arguments": "{\"city\": \"Paris\"}", "name": "get_weather" }, "id": "chatcmpl-tool-aaae1ecc31344b9d94f69f52a0a4c52e", "type": "function" } ] }, { "role": "tool", "tool_call_id": "chatcmpl-tool-aaae1ecc31344b9d94f69f52a0a4c52e", "content": **"18 degrees"** } ], "tools": [ { "type": "function", "function": { "name": "get_weather", "description": "get weather using city.", "parameters": { "type": "object", "required": [] } } } ], "tool_choice": "auto" } ``` The next one does not; ```json { "model": "openai/gpt-oss-20b", "messages": [ { "role": "user", "content": [ { "text": "what is the weather in Paris", "type": "text" } ] }, {...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: GPT-OSS Tool Answer Role Object not working bug;tool-calling ### Your current environment ```sh docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e Object not working bug;tool-calling ### Your current environment ```sh docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \ -p 8000:800...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ray ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: https://errors.pydantic.dev/2.11/v/model_type None", "type": "BadRequestError", "param": null, "code": 400 } } ``` according to openai doc and the example in /docs of vllm swagger: [chat-create-messages-tool-message-con...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
