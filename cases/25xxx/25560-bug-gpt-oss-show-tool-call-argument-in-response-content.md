# vllm-project/vllm#25560: [Bug]: GPT oss show tool call argument in response content

| 字段 | 值 |
| --- | --- |
| Issue | [#25560](https://github.com/vllm-project/vllm/issues/25560) |
| 状态 | closed |
| 标签 | bug;tool-calling |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GPT oss show tool call argument in response content

### Issue 正文摘录

### Your current environment I am running vllm with docker: docker run --runtime nvidia --gpus '"device=1"' --name vllm_openai_gpt_oss_20b -e TRANSFORMERS_OFFLINE=1 -v ~/models/openai-gpt-oss-20b:/openai-gpt-oss-20b -v ~/models/openai-gpt-oss-20b/vocab:/etc/encodings:ro -e TIKTOKEN_ENCODINGS_BASE=/etc/encodings -p 8080:8080 --ipc=host vllm/vllm-openai:v0.10.2 --model /openai-gpt-oss-20b --served-model-name openai/gpt-oss-20b --port=8080 --host=0.0.0.0 --gpu-memory-utilization 0.5 --max-model-len 8192 --kv-cache-dtype auto --max-num-batched-tokens 2048 --enable-auto-tool-choice --tool-call-parser openai --async-scheduling ### 🐛 Describe the bug Minimal code: ```python from openai import OpenAI # Create a client client = OpenAI( base_url="vllm_server_url", api_key="" ) # Define the tool tools = [ { "type": "function", "function": { "name": "get_weather", "description": "Get the current weather for a given city, using the tool given", "parameters": { "type": "object", "properties": { "city": {"type": "string", "description": "City name"} }, "required": ["city"] } } } ] # Send the request response = client.chat.completions.create( model="", messages=[ {"role": "user", "content": "What...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nt bug;tool-calling ### Your current environment I am running vllm with docker: docker run --runtime nvidia --gpus '"device=1"' --name vllm_openai_gpt_oss_20b -e TRANSFORMERS_OFFLINE=1 -v ~/models/openai-gpt-oss-20b:/op...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: device=1"' --name vllm_openai_gpt_oss_20b -e TRANSFORMERS_OFFLINE=1 -v ~/models/openai-gpt-oss-20b:/openai-gpt-oss-20b -v ~/models/openai-gpt-oss-20b/vocab:/etc/encodings:ro -e TIKTOKEN_ENCODINGS_BASE=/etc/encodings -p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ost=0.0.0.0 --gpu-memory-utilization 0.5 --max-model-len 8192 --kv-cache-dtype auto --max-num-batched-tokens 2048 --enable-auto-tool-choice --tool-call-parser openai --async-scheduling ### 🐛 Describe the bug Minimal cod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: oss ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: =8080 --host=0.0.0.0 --gpu-memory-utilization 0.5 --max-model-len 8192 --kv-cache-dtype auto --max-num-batched-tokens 2048 --enable-auto-tool-choice --tool-call-parser openai --async-scheduling ### 🐛 Describe the bug Mi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
