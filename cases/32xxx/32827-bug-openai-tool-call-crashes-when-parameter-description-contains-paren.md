# vllm-project/vllm#32827: [Bug]: OpenAI tool call crashes when parameter description contains parentheses with examples (e.g. "(e.g. ls -la)")

| 字段 | 值 |
| --- | --- |
| Issue | [#32827](https://github.com/vllm-project/vllm/issues/32827) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OpenAI tool call crashes when parameter description contains parentheses with examples (e.g. "(e.g. ls -la)")

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### 🐞 Bug Report **Describe the bug** When using OpenAI-compatible function calling, if a parameter's `description` contains example commands like `(e.g. ls -la, ssh user@host, cat file.txt)`, vLLM server crashes with "Connection error" (server disconnects without response). This happens even with a single parameter. ✅ Works: "Command to run, e.g. ls -la" ❌ Crashes: "Command to run (e.g. ls -la)" **To Reproduce** Run the following minimal test script against a vLLM OpenAI server: ```python import litellm import asyncio async def test(): tools = [{ "type": "function", "function": { "name": "test", "parameters": { "type": "object", "properties": { "command": { "type": "string", "description": "The complete command to execute (e.g. ls -la, ssh user@host, cat file.txt)" } }, "required": ["command"] } } }] try: await litellm.acompletion( model="your-model", messages=[{"role": "user", "content": "hello"}], tools=tools, api_base="http://localhost:8000/v1" ) print("Success") except Exception as e: print(f"Crash: {e}") asyncio.run(test()) ``` ### Expected behavior Request should succeed (even if no tool is called). ### Actual behavior Ser...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: he following minimal test script against a vLLM OpenAI server: ```python import litellm import asyncio async def test(): tools = [{ "type": "function", "function": { "name": "test", "parameters": { "type": "object",
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: al behavior Server disconnects immediately with: ```bash litellm.InternalServerError: OpenAIException - Connection error ``` ### Environment vLLM version: 0.13.0 Model: MiniMax-M2.1 OS: Linux Python version: 3.12.12 How...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: escription contains parentheses with examples (e.g. "(e.g. ls -la)") bug;stale ### Your current environment ### 🐛 Describe the bug ### 🐞 Bug Report **Describe the bug** When using OpenAI-compatible function calling, if...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: and to run, e.g. ls -la" ❌ Crashes: "Command to run (e.g. ls -la)" **To Reproduce** Run the following minimal test script against a vLLM OpenAI server: ```python import litellm import asyncio async def test(): tools = [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
