# vllm-project/vllm#29968: [Bug]: Ministral 3 - streaming tool call not working

| 字段 | 值 |
| --- | --- |
| Issue | [#29968](https://github.com/vllm-project/vllm/issues/29968) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Ministral 3 - streaming tool call not working

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running mistralai/Ministral-3-14B-Instruct-2512 as bellow. Tool calling works in non streaming mode, but not when streaming. ``` docker run \ --runtime nvidia \ --ipc=host \ -p "${MODEL_ID_PORT}:8000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ --env "CUDA_VISIBLE_DEVICES=0" \ vllm/vllm-openai:v0.12.0 \ --model mistralai/Ministral-3-14B-Instruct-2512 \ --gpu-memory-utilization 0.95 \ --max-model-len 128000 \ --tokenizer-mode mistral \ --config-format mistral \ --load-format mistral \ --enable-auto-tool-choice \ --tool-call-parser mistral \ --async-scheduling ``` Tool calling example: ``` curl -X POST \ http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "mistralai/Ministral-3-14B-Instruct-2512", "stream": false, "messages": [ {"role": "user", "content": "What'\''s the weather in New York?"}, { "role": "assistant", "tool_calls": [ { "id": "JlUnFJ7ea", "type": "function", "function": { "name": "get_weather", "arguments": "{\"location\": \"New York\"}" } } ] }, { "role": "tool", "tool_call_id": "JlUnFJ7ea", "content": "{\"temperature\": 22, \"description\": \"sunny\"...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: when streaming. ``` docker run \ --runtime nvidia \ --ipc=host \ -p "${MODEL_ID_PORT}:8000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ --env "CUDA_VISIBLE_DEVICES=0" \ vllm/vllm-openai:v0.12.0 \ --mode...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: . Tool calling works in non streaming mode, but not when streaming. ``` docker run \ --runtime nvidia \ --ipc=host \ -p "${MODEL_ID_PORT}:8000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ --env "CUDA_VI...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ --env "CUDA_VISIBLE_DEVICES=0" \ vllm/vllm-openai:v0.12.0 \ --model mistralai/Ministral-3-14B-Instruct-2512 \ --gpu-memory-utilization 0.95 \ --max-model...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: '{ "model": "mistralai/Ministral-3-14B-Instruct-2512", "stream": false, "messages": [ {"role": "user", "content": "What'\''s the weather in New York?"}, { "role": "assistant", "tool_calls": [ { "id": "JlUnFJ7ea", "type"...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
