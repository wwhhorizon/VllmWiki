# vllm-project/vllm#16797: [Bug]: Qwen/Qwen2.5-VL-3B-Instruct doesnt identify tools

| 字段 | 值 |
| --- | --- |
| Issue | [#16797](https://github.com/vllm-project/vllm/issues/16797) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen/Qwen2.5-VL-3B-Instruct doesnt identify tools

### Issue 正文摘录

### Your current environment ok ### 🐛 Describe the bug I'm trying to use function calling with Qwen2.5-VL-3B-Instruct but it seems that the model doesnt have access to the tools. Im using: ``` #!/bin/bash source ../.env export MODEL_ID=Qwen/Qwen2.5-VL-3B-Instruct export MODEL_ID_PORT=8000 export MODEL_ID_GPU=0 docker run \ --ipc=host \ --runtime nvidia \ -e VLLM_USE_V1=1 \ -p "${MODEL_ID_PORT}:8000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ --env "CUDA_VISIBLE_DEVICES=${MODEL_ID_GPU}" \ --env "VLLM_ALLOW_RUNTIME_LORA_UPDATING=True" \ -v "VLLM_LOGGING_LEVEL=${VLLM_LOGGING_LEVEL}" \ -v "${HF_HOME}:/root/.cache/huggingface" \ vllm/vllm-openai:latest \ --model ${MODEL_ID} \ --max-model-len 10000 \ --enable_auto_tool_choice \ --tool_call_parser hermes \ --gpu-memory-utilization 0.35 \ --enforce-eager ``` A simple request example is: `curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "Qwen/Qwen2.5-VL-3B-Instruct", "temperature": 0.0001, "n": 1, "stream": false, "tools": [ { "type": "function", "function": { "name": "get_current_temperature", "description": "Get current temperature at a location.", "parameters": { "ty...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen/Qwen2.5-VL-3B-Instruct doesnt identify tools bug ### Your current environment ok ### 🐛 Describe the bug I'm trying to use function calling with Qwen2.5-VL-3B-Instruct but it seems that the model doesnt have...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: /Qwen2.5-VL-3B-Instruct export MODEL_ID_PORT=8000 export MODEL_ID_GPU=0 docker run \ --ipc=host \ --runtime nvidia \ -e VLLM_USE_V1=1 \ -p "${MODEL_ID_PORT}:8000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ --env "CUDA_VISIBLE_DEVICES=${MODEL_ID_GPU}" \ --env "VLLM_ALLOW_RUNTIME_LORA_UPDATING=True" \ -v "VLLM_LOGGING_LEVEL=${VLLM_LOGGING_LEVEL}" \ -v "${HF_H...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: -VL-3B-Instruct", "temperature": 0.0001, "n": 1, "stream": false, "tools": [ { "type": "function", "function": { "name": "get_current_temperature", "description": "Get current temperature at a location.", "parameters": {
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: r hermes \ --gpu-memory-utilization 0.35 \ --enforce-eager ``` A simple request example is: `curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "Qwen/Qwen2.5-VL-3B-Inst...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
