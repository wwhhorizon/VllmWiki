# vllm-project/vllm#15035: [Feature]: Add support for reusable subschemas in tool requests (PydanticAI)

| 字段 | 值 |
| --- | --- |
| Issue | [#15035](https://github.com/vllm-project/vllm/issues/15035) |
| 状态 | closed |
| 标签 | feature request;stale;tool-calling |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Add support for reusable subschemas in tool requests (PydanticAI)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently PydanticAI clients leverage tools for structured response mapping. Consider the following ``tools`` definition in the request: ```json [ { "type": "function", "function": { "name": "final_result", "description": "The final response which ends this conversation", "parameters": { "$defs": { "Chapter": { "properties": { "chapter_name": { "description": "Name the chapter", "title": "Chapter Name", "type": "string" }, "content": { "description": "Content of the chapter", "title": "Content", "type": "string" } }, "required": [ "chapter_name", "content" ], "title": "Chapter", "type": "object" } }, "properties": { "title": { "description": "Title of the story", "title": "Title", "type": "string" }, "summary": { "description": "Short summary of the story", "title": "Summary", "type": "string" }, "chapters": { "description": "List of chapters", "items": { "$ref": "#/$defs/Chapter" }, "title": "Chapters", "type": "array" } }, "required": [ "title", "summary", "chapters" ], "title": "Story", "type": "object" } } } ] ``` Here, ``parameters`` contains the reusable subschema ``Chapter`` passed under ``"$defs"``. This is a valid JSON schema as ren...

## 现有链接修复摘要

#15627 Enable Outlines with JSON Sub-Schema References

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: o subschema passed. ## vLLM Startup Command Note that I am running the version of vLLM from [PR13483](https://github.com/vllm-project/vllm/pull/13483). Basically this PR adds support for ``tool_choice=required`` which i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ``"$defs"``. This is a valid JSON schema as rendered by a Pydantic ``BaseModel``, however results in a HTTP 400 error in vLLM. ### Alternatives For PydanticAI clients there are a few options available: * Don't use respo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Add support for reusable subschemas in tool requests (PydanticAI) feature request;stale;tool-calling ### 🚀 The feature, motivation and pitch Currently PydanticAI clients leverage tools for structured response...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: chunked-prefill=True \ --max-num-batched-tokens=4096 \ --dtype bfloat16 \ --kv-cache-dtype auto \ --gpu-memory-utilization 0.90 \ --enable-auto-tool-choice \ --tool-call-parser llama3_json \ --enable-prefix-caching \ --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -parser llama3_json \ --enable-prefix-caching \ --device=cuda \ --task=generate \ --scheduler-delay-factor=0.25 \ --uvicorn-log-level=debug \ --distributed-executor-backend=mp \ --max-logprobs=100 \ --enable-prompt-toke...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#15627](https://github.com/vllm-project/vllm/pull/15627) | closes_keyword | 0.95 | Enable Outlines with JSON Sub-Schema References | Fix #15035 # Bugfixes * Adding small bugfix that allows ``tool_choice=required`` to work with reasoning models. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
