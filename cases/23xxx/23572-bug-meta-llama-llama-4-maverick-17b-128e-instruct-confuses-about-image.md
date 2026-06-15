# vllm-project/vllm#23572: [Bug]: meta-llama/Llama-4-Maverick-17B-128E-Instruct confuses about image inputs when tool choice is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#23572](https://github.com/vllm-project/vllm/issues/23572) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: meta-llama/Llama-4-Maverick-17B-128E-Instruct confuses about image inputs when tool choice is enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Starting the server via: ``` vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct -tp 8 --download-dir /app/data/models --enable-auto-tool-choice --tool-call-parser llama4_pythonic --chat-template /vllm-workspace/examples/tool_chat_template_llama4_pythonic.jinja ``` The image input works fine without any tools specified: ``` from openai import OpenAI client = OpenAI( base_url=base_url, api_key="apikey" ) messages = [ { "role": "user", "content": [ { "type": "text", "text": "what is the sum of the numbers in the image?" }, { "type": "image_url", "image_url": { "url": "https://www.diariodesantotirso.pt/wp-content/uploads/2024/10/Totoloto-1.jpg" } } ] } ] stream = client.chat.completions.create( model=model, messages=messages, temperature=temperature, stream=True) ``` And the it tells the sum of the numbers. However when some tools are specified it leads to issue on output (regardless of the tool definitions): ``` stream = client.chat.completions.create( model=model, messages=messages, temperature=temperature, stream=true, tool_choice='auto', tools = [ { "type": "function", "function": { "name": "get-location", "description": "G...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: meta-llama/Llama-4-Maverick-17B-128E-Instruct confuses about image inputs when tool choice is enabled bug;stale ### Your current environment ### 🐛 Describe the bug Starting the server via: ``` vllm serve meta-lla...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ama4_pythonic.jinja ``` The image input works fine without any tools specified: ``` from openai import OpenAI client = OpenAI( base_url=base_url, api_key="apikey" ) messages = [ { "role": "user", "content": [ { "ty
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: (?) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ting;model_support;multimodal_vlm;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "required": [], "additionalProperties": False } }} ]) ``` Outputs: ``` I don't have access to image processing information. However, I can tell you that the numbers in the image are 1, 10, 11, 16, 35, and 4. The sum of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
