# vllm-project/vllm#17655: [Bug]: Qwen3 streaming output failed to return function call results when using "qwen3" reasoning parser.

| 字段 | 值 |
| --- | --- |
| Issue | [#17655](https://github.com/vllm-project/vllm/issues/17655) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3 streaming output failed to return function call results when using "qwen3" reasoning parser.

### Issue 正文摘录

### Your current environment ```Bash vllm serve ... --enable-auto-tool-choice --tool-call-parser hermes --enable-reasoning --reasoning-parser qwen3" ``` ### 🐛 Describe the bug The Qwen3 model supports switching between "think" and non-"think" modes. Therefore, if the output is in non-"think" mode and is streamed, the `is_reasoning_end` function in `Qwen3ReasoningParser` may return incorrect results, causing the function call parser to not be executed, and no function call result will be output. Here is an example: Function call will failed if we set stream=True and added "disable thinking" argument in request: ```Python from openai import OpenAI openai_api_base = "API_ENDPOINT" openai_api_key = "API_KEY" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base + "/v1", ) class bcolors: HEADER = '\033[95m' OKBLUE = '\033[94m' OKCYAN = '\033[96m' OKGREEN = '\033[92m' WARNING = '\033[93m' FAIL = '\033[91m' ENDC = '\033[0m' BOLD = '\033[1m' UNDERLINE = '\033[4m' tools = [ { "type": "function", "function": { "name": "get_current_temperature", "description": "Get current temperature at a location.", "parameters": { "type": "object", "properties": { "location": { "type": "string...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3 streaming output failed to return function call results when using "qwen3" reasoning parser. bug ### Your current environment ```Bash vllm serve ... --enable-auto-tool-choice --tool-call-parser hermes --ena...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: and added "disable thinking" argument in request: ```Python from openai import OpenAI openai_api_base = "API_ENDPOINT" openai_api_key = "API_KEY" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base + "/v1"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ream=True, extra_body={"chat_template_kwargs": {"enable_thinking": False}}, ) chunks = [] for chunk in tool_calls_stream: chunks.append(chunk) if hasattr(chunk.choices[0].delta, "reasoning_content"): reasoning_content =...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ll failed if we set stream=True and added "disable thinking" argument in request: ```Python from openai import OpenAI openai_api_base = "API_ENDPOINT" openai_api_key = "API_KEY" client = OpenAI( api_key=openai_api_key,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
