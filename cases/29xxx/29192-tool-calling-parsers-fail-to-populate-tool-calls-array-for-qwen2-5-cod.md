# vllm-project/vllm#29192: Tool Calling Parsers Fail to Populate tool_calls Array for Qwen2.5-Coder Models

| 字段 | 值 |
| --- | --- |
| Issue | [#29192](https://github.com/vllm-project/vllm/issues/29192) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | wrong_output |
| Operator 关键词 | quantization |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Tool Calling Parsers Fail to Populate tool_calls Array for Qwen2.5-Coder Models

### Issue 正文摘录

# Tool Calling Parsers Fail to Populate `tool_calls` Array for Qwen2.5-Coder Models ## Environment - **vLLM Version**: v0.11.2.dev115+g56669c1f2 (Blackwell build) - **Model**: Qwen/Qwen2.5-Coder-14B-Instruct-AWQ - **Quantization**: AWQ - **Python Version**: 3.x (Docker container) - **GPU**: NVIDIA GeForce RTX 5080 (16GB, Blackwell/sm_120) - **Platform**: WSL2, Linux 6.6.87.2-microsoft-standard-WSL2 ## Description When using tool calling with Qwen2.5-Coder models, the model correctly generates tool calls in ` ` XML format, but both `qwen3_xml` and `qwen3_coder` parsers fail to extract these tool calls into the `tool_calls` array in the API response. The tool call information remains in the `content` field but the `tool_calls` array stays empty. ## Steps to Reproduce 1. Start vLLM with Qwen2.5-Coder and tool calling parser: ```bash python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen2.5-Coder-14B-Instruct-AWQ \ --quantization awq \ --enable-auto-tool-choice \ --tool-call-parser qwen3_xml # or qwen3_coder ``` 2. Send a tool calling request: ```bash curl -s http://localhost:8002/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "qwen2.5-coder-14b-a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ate `tool_calls` Array for Qwen2.5-Coder Models ## Environment - **vLLM Version**: v0.11.2.dev115+g56669c1f2 (Blackwell build) - **Model**: Qwen/Qwen2.5-Coder-14B-Instruct-AWQ - **Quantization**: AWQ - **Python Version*...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: er Models ## Environment - **vLLM Version**: v0.11.2.dev115+g56669c1f2 (Blackwell build) - **Model**: Qwen/Qwen2.5-Coder-14B-Instruct-AWQ - **Quantization**: AWQ - **Python Version**: 3.x (Docker container) - **GPU**: N...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Tool Calling Parsers Fail to Populate tool_calls Array for Qwen2.5-Coder Models # Tool Calling Parsers Fail to Populate `tool_calls` Array for Qwen2.5-Coder Models ## Environment - **vLLM Version**: v0.11.2.dev115+g5666...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: the `content` field but the `tool_calls` array stays empty. ## Steps to Reproduce 1. Start vLLM with Qwen2.5-Coder and tool calling parser: ```bash python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen2.5-Cod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: available at: - File: `qwen_tool_calling_client.py` - Includes automatic fallback to manual parsing when vLLM parser fails - Tested successfully with Qwen2.5-Coder-14B-Instruct-AWQ Would appreciate guidance on: 1. Wheth...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
