# vllm-project/vllm#11786: [Bug]: Multiple tool calls for llama3.2-11b-vision-instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#11786](https://github.com/vllm-project/vllm/issues/11786) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | install |
| Operator 关键词 | gemm |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multiple tool calls for llama3.2-11b-vision-instruct

### Issue 正文摘录

### Your current environment I used one H100, and the params I used to serve llama3.2-11b-vision-instruct: `. - --max-model-len=32768 - --tensor-parallel-size=1 - --gpu_memory_utilization=0.99 - --max_num_seqs=16 - --limit-mm-per-prompt=image=2 - --enforce-eager - --enable-auto-tool-choice - --tool-call-parser=llama3_json - --chat-template=tool_chat_template_llama3.2_json.jinja (by vLLM) ` ### Model Input Dumps _No response_ ### 🐛 Describe the bug `client` is an OpenAI client, and I tested it with the following codes: ``` tools = [ { "type": "function", "function": { "name": "get_current_weather", "description": "Get the current weather conditions for a specific location", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "The city and state, e.g., San Francisco, CA", }, "unit": { "type": "string", "enum": ["Celsius", "Fahrenheit"], "description": "The temperature unit to use. Infer this from the user's location.", }, }, "required": ["location", "unit"], }, }, }, { "type": "function", "function": { "name": "get_current_traffic", "description": "Get the current traffic conditions for a specific location", "parameters": { "type": "objec...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: instruct bug;stale;tool-calling ### Your current environment I used one H100, and the params I used to serve llama3.2-11b-vision-instruct: `. - --max-model-len=32768 - --tensor-parallel-size=1 - --gpu_memory_utilization...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Multiple tool calls for llama3.2-11b-vision-instruct bug;stale;tool-calling ### Your current environment I used one H100, and the params I used to serve llama3.2-11b-vision-instruct: `. - --max-model-len=32768 -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Multiple tool calls for llama3.2-11b-vision-instruct bug;stale;tool-calling ### Your current environment I used one H100, and the params I used to serve llama3.2-11b-vision-instruct: `. - --max-model-len=32768 -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: "description": "Get the current weather conditions for a specific location", "parameters": { "type": "object", "properties": { "location": { "type": "string",
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: elopment distributed_parallel;frontend_api;model_support;sampling_logits gemm Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
