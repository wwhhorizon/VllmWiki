# vllm-project/vllm#33877: [Bug]: GLM47 Tool Call Bug

| 字段 | 值 |
| --- | --- |
| Issue | [#33877](https://github.com/vllm-project/vllm/issues/33877) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM47 Tool Call Bug

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Env**：vllm 0.14.0 GLM4.7 FP8， openai api **AgentCli**：opencode gemini cli **Problem**： The following is the agent's response; this type of question occurs very frequently. ``` 让我先查看当前的配置获取逻辑。好的，我来分析如何修改 inferserver 的调用地址和模型名称，使其优先使用环境变量设置的值。 TodoWrite todos [{"id": "1", "content": "分析当前配置获取逻辑", "status": "in_progress"}, {"id": "2", "content": "设计环境变量优先级方案", "status": "pending"}, {"id": "3", "content": "提供 API_BASE_URL 修改方案", "status": "pending"}, {"id": "4", "content": "提供模型名称修改方案", "status": "pending"}, {"id": "5", "content": "生成配置修改指南文档", "status": "pending"}] ``` and flowing is another problem，maybe they are the same problem **request body**： ``` { "model": "GLM-4.7-FP8", "messages": [ { "role": "user", "content": "请查询今天的日期" } ], "tools": [ { "type": "function", "function": { "name": "get_current_date", "description": "获取今天的日期", "parameters": {} } } ], "tool_choice": "auto", "stream": false } ``` **response**： ``` { "id": "chatcmpl-b326ed8fd9cbe29822161f4672241723", "created": 1770122001, "model": "GLM-4.7-FP8", "object": "chat.completion", "choices": [ { "finish_reason": "stop", "index": 0, "message": { "content": "用户正在询问今天...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: "role": "assistant" }, "provider_specific_fields": { "stop_reason": 151338 } } ], "usage": { "completion_tokens": 38, "prompt_tokens": 136, "total_tokens": 174 } } ``` ### Before subm
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: rent environment ### 🐛 Describe the bug **Env**：vllm 0.14.0 GLM4.7 FP8， openai api **AgentCli**：opencode gemini cli **Problem**： The following is the agent's response; this type of question occurs very frequently. ``` 让...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: } } ], "tool_choice": "auto", "stream": false } ``` **response**： ``` { "id": "chatcmpl-b326ed8fd9cbe29822161f4672241723", "created": 1770122001, "model": "GLM-4.7-FP8", "object": "chat.completion", "choices": [ { "finis
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: er problem，maybe they are the same problem **request body**： ``` { "model": "GLM-4.7-FP8", "messages": [ { "role": "user", "content": "请查询今天的日期" } ], "tools": [ { "type": "function", "function": {

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
