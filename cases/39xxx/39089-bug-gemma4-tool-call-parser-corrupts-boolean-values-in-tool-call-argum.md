# vllm-project/vllm#39089: [Bug]: gemma4 tool-call-parser corrupts boolean values in tool call arguments during streaming mode

| 字段 | 值 |
| --- | --- |
| Issue | [#39089](https://github.com/vllm-project/vllm/issues/39089) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gemma4 tool-call-parser corrupts boolean values in tool call arguments during streaming mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The gemma4 tool-call-parser produces corrupted JSON in tool call arguments. Boolean values like true are mangled into `trutrue`, making the arguments unparseable. This occurs in both streaming and non-streaming responses, confirming the corruption originates in the parser itself, not in SSE delta computation. Environment • Docker image: vllm/vllm-openai:gemma4 • Model: google/gemma-4-31B-it • Launch command: ``` vllm serve google/gemma-4-31B-it \ --async-scheduling \ --enable-auto-tool-choice \ --tool-call-parser=gemma4 \ --reasoning-parser=gemma4 ``` How to Reproduce Send a chat completion request with tools that have complex JSON Schema parameters (using $defs / $ref): ``` curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "google/gemma-4-31B-it", "messages": [ {"role": "user", "content": "show me last 2 workflow results"} ], "tools": [ { "type": "function", "function": { "name": "search_reservations", "description": "Search list of reservations.", "parameters": { "type": "object", "$defs": { "SearchField": { "type": "object", "required": ["field"], "properties": { "field": {"t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: es in the parser itself, not in SSE delta computation. Environment • Docker image: vllm/vllm-openai:gemma4 • Model: google/gemma-4-31B-it • Launch command: ``` vllm serve google/gemma-4-31B-it \ --async-scheduling \ --e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: gemma4 tool-call-parser corrupts boolean values in tool call arguments during streaming mode bug ### Your current environment ### 🐛 Describe the bug The gemma4 tool-call-parser produces corrupted JSON in tool cal...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: --reasoning-parser=gemma4 ``` How to Reproduce Send a chat completion request with tools that have complex JSON Schema parameters (using $defs / $ref): ``` curl http://localhost:8000/v1/chat/completions \ -H "Content-Ty...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: { "type": "function", "function": { "name": "search_reservations", "description": "Search list of reservations.", "parameters": { "type": "object", "$defs": { "SearchField": { "type": "object",
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: "type": "boolean", "default": false } } } }, "required": ["input_model"], "properties": { "input_model": {"$ref": "#/$defs/SearchInput"}, "p

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
