# vllm-project/vllm#43244: [Bug]: `previous_response_id` drops function_call/function_call_output from stored context in Responses API

| 字段 | 值 |
| --- | --- |
| Issue | [#43244](https://github.com/vllm-project/vllm/issues/43244) |
| 状态 | open |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `previous_response_id` drops function_call/function_call_output from stored context in Responses API

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using `previous_response_id` to chain multi-turn conversations that include tool calls, the server-side stored context only carries forward text messages — `function_call` and `function_call_output` messages from earlier turns are dropped. The model in follow-up turns has no memory of what tools were called or what data they returned. **Server start command:** ```bash docker run -d \ --name vllm-gemma4 \ --gpus all \ --ipc=host \ -p 8000:8000 \ -e VLLM_ENABLE_RESPONSES_API_STORE=1 \ vllm/vllm-openai:v0.21.0 \ --model google/gemma-4-26B-A4B-it \ --tensor-parallel-size 4 \ --max-model-len 32768 \ --gpu-memory-utilization 0.9 \ --max-num-seqs 4 \ --max-num-batched-tokens 14336 \ --tool-call-parser functiongemma \ --enable-auto-tool-choice \ --reasoning-parser gemma4 ``` **Reproduction script:** ```python import requests, json BASE = "http://localhost:8000/v1" MODEL = "google/gemma-4-26B-A4B-it" tools = [ { "type": "function", "name": "get_weather", "description": "Get current weather for a city", "parameters": { "type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"], }, } ] # Turn 1: model calls a to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e called or what data they returned. **Server start command:** ```bash docker run -d \ --name vllm-gemma4 \ --gpus all \ --ipc=host \ -p 8000:8000 \ -e VLLM_ENABLE_RESPONSES_API_STORE=1 \ vllm/vllm-openai:v0.21.0 \ --mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: and `function_call_output` messages from earlier turns are dropped. The model in follow-up turns has no memory of what tools were called or what data they returned. **Server start command:** ```bash docker run -d \ --na...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : model response = I do not have access to real-time weather data or a search engine... Turn 3: I did not find any temperature or weather conditions because I do not have access to real-time information... FAIL: Model d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: gemm_linear;hardware_porting;model_support;sampling_logits cuda;operator;triton build_error env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ext3 or "foggy" in text3: print("PASS: Model recalls tool results") else: print("FAIL: Model does not recall tool results from prior turns") ``` **Observed output:** ``` Turn 1: tool call get_weather({"city": "San Franc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
