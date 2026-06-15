# vllm-project/vllm#13622: [Bug]: Mistral streaming tool parser fails to parse integer tool argument

| 字段 | 值 |
| --- | --- |
| Issue | [#13622](https://github.com/vllm-project/vllm/issues/13622) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral streaming tool parser fails to parse integer tool argument

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Mistral tool parser fails to parse a tool call when streaming if arguments are of type integer. Vllm server started with : ```bash vllm serve mistralai/Mistral-7B-Instruct-v0.3 --tool-call-parser mistral --enable-auto-tool-choice --chat-template /home/avigny/vllm/examples/tool_chat_template_mistral.jinja --max-model-len 1024 --tokenizer-mode mistral --load-format mistral --config-format mistral ``` and client code to reproduce the bug : ```python from openai import OpenAI client = OpenAI( api_key="NOT_NEEDED", base_url="http://localhost:8000/v1", ) tools = [ { 'type': 'function', 'function': { 'name': 'add', 'description': 'Adds a and b.', 'parameters': { 'type': 'object', 'properties': { 'a': {'type': 'integer', 'description': 'One number'}, 'b': {'type': 'integer', 'description': 'One number'} }, "required": ["a", "b"] }, } } ] # Completion API stream = True completion = client.chat.completions.create( model=client.models.list().data[0].id, messages=[{"role": "user", "content": "What is 3 + 4?"}], stream=stream, tools=tools, tool_choice="auto", temperature=0 ) if stream: name = '' arguments = '' for c in completion: try: functi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: stral ``` and client code to reproduce the bug : ```python from openai import OpenAI client = OpenAI( api_key="NOT_NEEDED", base_url="http://localhost:8000/v1", ) tools = [ { 'type': 'function', 'function': { 'name': 'a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: mplate /home/avigny/vllm/examples/tool_chat_template_mistral.jinja --max-model-len 1024 --tokenizer-mode mistral --load-format mistral --config-format mistral ``` and client code to reproduce the bug : ```python from op...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --- ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : Mistral streaming tool parser fails to parse integer tool argument bug;stale ### Your current environment ### 🐛 Describe the bug Mistral tool parser fails to parse a tool call when streaming if arguments are of type i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
