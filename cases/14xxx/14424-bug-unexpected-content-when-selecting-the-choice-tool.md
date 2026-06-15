# vllm-project/vllm#14424: [Bug]: Unexpected content when selecting the choice tool

| 字段 | 值 |
| --- | --- |
| Issue | [#14424](https://github.com/vllm-project/vllm/issues/14424) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unexpected content when selecting the choice tool

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Description When I used version v0.7.3, I made the following request that the model must give the tool I chose to call, but when I did, the message returned with the tool parameters was not the normal content. I checked the Openapi documentation and this does not seem to be a normal response. # Request: ```json { "messages": [{ "content": "What requirements should be observed when applying for setting up foreign-related meteorological observation stations?", "role": "user" }], "model": "qwen2.5-7b", "max_completion_tokens": 8192, "n": 1, "stream": false, "temperature": 0.0, "tool_choice": { "type": "function", "function": { "name": "duckduckgo-search" } }, "tools": [{ "type": "function", "function": { "name": "duckduckgo-search", "description": "Use duckduckgo to search", "parameters": { "type": "object", "required": ["question"], "properties": { "question": { "type": "string", "description": "Use duckduckgo to search" } } } } }], "top_p": 1.0 } ``` # Response: ```json { "id": "chatcmpl-74c026d03f3448259fc071fe6db1b862", "object": "chat.completion", "created": 1741339638, "model": "qwen2.5-7b", "choices": [ { "index": 1, "messa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rrent environment ### 🐛 Describe the bug # Description When I used version v0.7.3, I made the following request that the model must give the tool I chose to call, but when I did, the message returned with the tool param...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Unexpected content when selecting the choice tool bug;stale ### Your current environment ### 🐛 Describe the bug # Description When I used version v0.7.3, I made the following request that the model must give the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: hoice": { "type": "function", "function": { "name": "duckduckgo-search" } }, "tools": [{ "type": "function", "function": { "name": "duckduckgo-search", "description": "Use duckduckgo to search", "parameters": { "type":...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ption When I used version v0.7.3, I made the following request that the model must give the tool I chose to call, but when I did, the message returned with the tool parameters was not the normal content. I checked the O...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
