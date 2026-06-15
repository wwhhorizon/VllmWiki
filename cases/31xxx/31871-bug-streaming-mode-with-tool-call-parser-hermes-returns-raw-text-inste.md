# vllm-project/vllm#31871: [Bug]: Streaming mode with --tool-call-parser hermes returns raw text instead of parsed tool_calls

| 字段 | 值 |
| --- | --- |
| Issue | [#31871](https://github.com/vllm-project/vllm/issues/31871) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Streaming mode with --tool-call-parser hermes returns raw text instead of parsed tool_calls

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using vLLM with `--tool-call-parser hermes`, tool calls are correctly parsed in non-streaming mode but fail to be parsed in streaming mode. Instead of returning structured `tool_calls`, the streaming response returns raw text content with ` ` XML tags. ## vLLM launch command ```bash vllm serve Qwen/Qwen3-VL-8B-Instruct-FP8 \ --host 0.0.0.0 \ --port 30000 \ --enable-auto-tool-choice \ --tool-call-parser hermes ``` ## Minimal reproduction ```python import requests import json BASE_URL = "http://localhost:30000/v1" tools = [ { "type": "function", "function": { "name": "get_weather", "description": "Get weather for a city", "parameters": { "type": "object", "properties": { "city": {"type": "string", "description": "City name"} }, "required": ["city"], }, }, } ] messages = [{"role": "user", "content": "What's the weather in Beijing?"}] # Test 1: Non-streaming (works correctly) print("=== Non-streaming test ===") response = requests.post( f"{BASE_URL}/chat/completions", json={ "model": "Qwen/Qwen3-VL-8B-Instruct-FP8", "messages": messages, "tools": tools, "tool_choice": "auto", "stream": False, }, ) result = response.json() print(...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: \ --tool-call-parser hermes ``` ## Minimal reproduction ```python import requests import json BASE_URL = "http://localhost:30000/v1" tools = [ { "type": "function", "function": { "name": "get_weather", "description": "G...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: s. ## vLLM launch command ```bash vllm serve Qwen/Qwen3-VL-8B-Instruct-FP8 \ --host 0.0.0.0 \ --port 30000 \ --enable-auto-tool-choice \ --tool-call-parser hermes ``` ## Minimal reproduction ```python import requests im...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: --tool-call-parser hermes ``` ## Minimal reproduction ```python import requests import json BASE_URL = "http://localhost:30000/v1" tools = [ { "type": "function", "function": { "name": "get_weather", "description": "Get...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t content with ` ` XML tags. ## vLLM launch command ```bash vllm serve Qwen/Qwen3-VL-8B-Instruct-FP8 \ --host 0.0.0.0 \ --port 30000 \ --enable-auto-tool-choice \ --tool-call-parser hermes ``` ## Minimal reproduction ``...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
