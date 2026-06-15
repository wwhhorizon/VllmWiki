# vllm-project/vllm#19056: [Bug]: Hermes tool parser stream output error in Qwen3 case

| 字段 | 值 |
| --- | --- |
| Issue | [#19056](https://github.com/vllm-project/vllm/issues/19056) |
| 状态 | closed |
| 标签 | bug;tool-calling |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Hermes tool parser stream output error in Qwen3 case

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The extract_tool_calls_streaming component of the Hermes tool parser improperly handled a specific token during the parsing of streaming tool function outputs when the Qwen3 generates a specific token. case: Qwen3 tokenizer vocab has a token `"}`, id 9207 if Qwen3 models output this token, hermes extract_tool_calls_streaming method will truncate this token to `"` in which case `}` will be discarded, further led to broken tool call's json schema output ### LLM Qwen3 series **Client code** ```python import openai api_key = "" api_base = "" client = openai.OpenAI( api_key=api_key, base_url=api_base, ) tools = [ { "type": "function", "function": { "name": "summary", "description": "总结工具，用于在资料准备完成后生成回答，并展示给用户。", "parameters": { "type": "object", "properties": { "query": { "description": "用户的问题", "type": "string" }, "title": { "description": "回答的标题，与用户问题密切相关，不超过15个字。", "type": "string" }, "style": { "description": "回答风格。可能的回答风格包含: 自媒体文章，短视频脚本，媒体稿件，论文，研究报告等", "enum": [ "自媒体文章", "短视频脚本", "媒体稿件", "论文", "研究报告" ], "type": "string" }, "outline": { "description": "回答的大纲", "type": "array", "items": { "h2": { "type": "string", "description": "大...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ls_streaming component of the Hermes tool parser improperly handled a specific token during the parsing of streaming tool function outputs when the Qwen3 generates a specific token. case: Qwen3 tokenizer vocab has a tok...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: } }, "search_result_index_list": { "type": "array", "items": { "type": "string" } }, "li
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Hermes tool parser stream output error in Qwen3 case bug;tool-calling ### Your current environment ### 🐛 Describe the bug The extract_tool_calls_streaming component of the Hermes tool parser improperly handled a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: sage.content) print(response.choices[0].message.tool_calls) else: full_response = "" tool_calls_list = [] for chunk in response: if chunk.choices[0].delta: if chunk.choices[0].delta.content: full_response += c
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance frontend_api;hardware_porting;model_support cuda crash;slowdown env_depen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
