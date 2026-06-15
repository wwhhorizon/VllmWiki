# vllm-project/vllm#25539: [Bug]:When there is an enum type with Chinese values in the response_format schema, a decoding error occurs during output.

| 字段 | 值 |
| --- | --- |
| Issue | [#25539](https://github.com/vllm-project/vllm/issues/25539) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]:When there is an enum type with Chinese values in the response_format schema, a decoding error occurs during output.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When there is an enum type with Chinese values in the response_format schema, a decoding error occurs during output. I have tried various models such as qwen2.5-72b, qwen3-next, and llama_4_maverick. `curl --location --request POST 'http://xxx/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data-raw '{ "messages": [ { "content": "姓名：王五，偏好音乐：古典", "role": "user" } ], "model": "any model", "response_format": { "type": "json_schema", "json_schema": { "schema": { "$defs": { "MusicGenre": { "enum": [ "流行", "摇滚", "古典", "爵士", "嘻哈", "电子", "民谣", "乡村", "金属" ], "title": "MusicGenre", "type": "string" } }, "properties": { "name": { "description": "角色名称", "title": "Name", "type": "string" }, "music_genre": { "anyOf": [ { "$ref": "#/$defs/MusicGenre" }, { "type": "null" } ], "description": "角色音乐偏好" } }, "required": [ "name", "music_genre" ], "title": "CharacterCreateOutput", "type": "object", "additionalProperties": false }, "name": "CharacterCreateOutput", "strict": true } }, "stream": false }'` the result is： `{"content":"{\n \"name\": \"王五\",\n \"music_genre\": \"\\u00e7\\u0088\\u00b5\\u00e5\\u00a3\\u00ab\" \t \t\n}` ###...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]:When there is an enum type with Chinese values in the response_format schema, a decoding error occurs during output. bug;stale ### Your current environment ### 🐛 Describe the bug When there is an enum type with Ch...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: n the response_format schema, a decoding error occurs during output. bug;stale ### Your current environment ### 🐛 Describe the bug When there is an enum type with Chinese values in the response_format schema, a decoding...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n}` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
