# vllm-project/vllm#20341: [Bug]: No output / Repeated outputs when using Gemma 3  on vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#20341](https://github.com/vllm-project/vllm/issues/20341) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: No output / Repeated outputs when using Gemma 3  on vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm running the google/gemma-3-27b-it model with vLLM using the OpenAI-compatible API server. ```bash CUDA_VISIBLE_DEVICES=0 VLLM_USE_V1=1 python /opt/VLLM/vllm/vllm/entrypoints/openai/api_server.py \ --model /opt/MODELS/gemma-3-27b-it/ \ --max-model-len 32000 \ --host 10.12.112.168 \ --port 9005 \ --tensor-parallel-size 1 \ --gpu_memory_utilization 0.9 ``` Then, I send a standard request to the /v1/chat/completions endpoint using Python: ```python import requests import json url = "http://10.12.112.168:9005/v1/chat/completions" data = { "model": "/opt/MODELS/gemma-3-27b-it/", "messages": [ {"role": "user", "content": "hello"} ], "temperature": 0.1, "max_tokens": 500, "enable_thinking": False } headers = { "Content-Type": "application/json" } response = requests.post(url, headers=headers, data=json.dumps(data)) result = response.json() print(result['choices'][0]['message']['content']) ``` The request is processed, but the model fails to produce meaningful responses. It either: outputs nothing, or keeps repeating certain tokens or parts of the input (e.g., repeating “selamlar brom”). This issue only happens with Gemma 3 IT models....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: No output / Repeated outputs when using Gemma 3 on vLLM bug ### Your current environment ### 🐛 Describe the bug I'm running the google/gemma-3-27b-it model with vLLM using the OpenAI-compatible API server. ```bas...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rd request to the /v1/chat/completions endpoint using Python: ```python import requests import json url = "http://10.12.112.168:9005/v1/chat/completions" data = { "model": "/opt/MODELS/gemma-3-27b-it/", "messages": [ {"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -27b-it model with vLLM using the OpenAI-compatible API server. ```bash CUDA_VISIBLE_DEVICES=0 VLLM_USE_V1=1 python /opt/VLLM/vllm/vllm/entrypoints/openai/api_server.py \ --model /opt/MODELS/gemma-3-27b-it/ \ --max-mode...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "temperature": 0.1, "max_tokens": 500, "enable_thinking": False } headers = { "Content-Type": "application/json" } response = requests.post(url, headers=headers, data=json.dumps(data)) result = response.json() print(res...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: No output / Repeated outputs when using Gemma 3 on vLLM bug ### Your current environment ### 🐛 Describe the bug I'm running the google/gemma-3-27b-it model with vLLM using the OpenAI-compatible API server. ```bas...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
