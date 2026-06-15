# vllm-project/vllm#23196: [Bug]: unable to use GPTOss built-in browser tool

| 字段 | 值 |
| --- | --- |
| Issue | [#23196](https://github.com/vllm-project/vllm/issues/23196) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: unable to use GPTOss built-in browser tool

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After installing gpt-oss package and passing `EXA_API_KEY`, the server shows ` Browser tool initialized` and could response to normal request without tool ```python import openai client = openai.Client( api_key="empty", base_url=base_url ) response = client.responses.create( model="gpt-oss-120b", input="Who is the president of South Korea as of now?", reasoning={'effort':'high'} ) ## pass assert response is not None assert response.status == "completed" response = client.responses.create( model="gpt-oss-120b", input="Who is the president of South Korea as of now?", tools=[{ "type": "web_search_preview" }], reasoning={'effort':'high'} ) ### wrong ``` however, if adding `tools=[{ "type": "web_search_preview" }],`, the server will down, and here is the traceback: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: bug;stale ### Your current environment ### 🐛 Describe the bug After installing gpt-oss package and passing `EXA_API_KEY`, the server shows ` Browser tool initialized` and could response to normal request without tool ``...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: unable to use GPTOss built-in browser tool bug;stale ### Your current environment ### 🐛 Describe the bug After installing gpt-oss package and passing `EXA_API_KEY`, the server shows ` Browser tool initialized` an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: resident of South Korea as of now?", tools=[{ "type": "web_search_preview" }], reasoning={'effort':'high'} ) ### wrong ``` however, if adding `tools=[{ "type": "web_search_preview" }],`, the server will down, and here i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ## Your current environment ### 🐛 Describe the bug After installing gpt-oss package and passing `EXA_API_KEY`, the server shows ` Browser tool initialized` and could response to normal request without tool ```python imp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: model_support;scheduler_memory;speculative_decoding cuda;kernel;operator;triton build_error;crash env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
