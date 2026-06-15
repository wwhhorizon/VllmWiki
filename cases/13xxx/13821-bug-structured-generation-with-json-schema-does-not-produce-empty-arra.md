# vllm-project/vllm#13821: [Bug]: Structured generation with JSON schema does not produce empty array

| 字段 | 值 |
| --- | --- |
| Issue | [#13821](https://github.com/vllm-project/vllm/issues/13821) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Structured generation with JSON schema does not produce empty array

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using structured generation with JSON schema for array output, the output does not produce an empty list. Instead it either produces an invalid JSON or a JSON with non-zero number of elements in the array. Here is how this can be reproduced. First, set up the Docker compose file named `vllm.compose.yaml` to spin up the vLLM OpenAI-compatible server ``` services: vllm-server: image: vllm/vllm-openai:latest ports: - 8000:8000 environment: HUGGING_FACE_HUB_TOKEN: ${HF_TOKEN} DO_NOT_TRACK: 1 command: --model google/gemma-2-9b-it --quantization fp8 --enable-prefix-caching deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: [gpu] volumes: - $HF_HOME:/root/.cache/huggingface:rw ``` Then run the following: ```bash export HF_TOKEN= docker compose -f vllm.compose.yaml up ``` Once the server starts up, make the following request: ```bash curl --location 'localhost:8000/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data '{ "model": "google/gemma-2-9b-it", "messages": [ { "role": "user", "content": "Give me a json with key '\''matches'\'' and value an empty list." } ], "temperature":...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: orts: - 8000:8000 environment: HUGGING_FACE_HUB_TOKEN: ${HF_TOKEN} DO_NOT_TRACK: 1 command: --model google/gemma-2-9b-it --quantization fp8 --enable-prefix-caching deploy: resources: reservations: devices: - driver: nvi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nts in the array. Here is how this can be reproduced. First, set up the Docker compose file named `vllm.compose.yaml` to spin up the vLLM OpenAI-compatible server ``` services: vllm-server: image: vllm/vllm-openai:lates...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: TOKEN} DO_NOT_TRACK: 1 command: --model google/gemma-2-9b-it --quantization fp8 --enable-prefix-caching deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: [gpu] volumes: -
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Structured generation with JSON schema does not produce empty array bug;stale ### Your current environment ### 🐛 Describe the bug When using structured generation with JSON schema for array output, the output does not p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: array with non-zero number of elements. We can set the guided decoding backend as `outlines` instead using the following request: ```bash curl --location 'localhost:8000/v1/chat/completions' \ --header 'Content-Type: ap...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
