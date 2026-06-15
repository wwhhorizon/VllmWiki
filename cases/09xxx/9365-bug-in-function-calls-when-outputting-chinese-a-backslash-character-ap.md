# vllm-project/vllm#9365: [Bug]: In function calls, when outputting Chinese, a backslash character "\" appears before Chinese characters.

| 字段 | 值 |
| --- | --- |
| Issue | [#9365](https://github.com/vllm-project/vllm/issues/9365) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: In function calls, when outputting Chinese, a backslash character "\" appears before Chinese characters.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug start vllm ~~~ vllm serve meta-llama/Llama-3.1-70B-Instruct --dtype bfloat16 --enable-auto-tool-choice --tool-call-parser llama3_json ~~~ send message ~~~ { "model": "meta-llama/Llama-3.1-70B-Instruct", "messages": [ { "role": "user", "content": "查询scene_code为“YQ0204”，scene_name为“文明养宠”的sop" } ], "tools": [ { "type": "function", "function": { "name": "query_sop_by_scene", "description": "Retrieve the Standard Operating Procedure (SOP) based on a specific scenario code. Use this when you need SOP details for a given scene.", "parameters": { "type": "object", "properties": { "scene_code": { "type": "string", "description": "The encoded representation of the scenario for which the SOP is being queried." }, "scene_name": { "type": "string", "description": "scene name" } }, "required": [ "scene_code", "scene_name" ], "additionalProperties": false } } } ], "stream": false, "logprobs": true } ~~~ problem in logprob, no backslash character "\\" appears before Chinese characters. but in output there is a backslash character "\\" appears before Chinese characters. ![image](https://github.com/user-attachme...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ription": "Retrieve the Standard Operating Procedure (SOP) based on a specific scenario code. Use this when you need SOP details for a given scene.", "parameters": { "type": "object", "properties": { "scene_code":
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e the bug start vllm ~~~ vllm serve meta-llama/Llama-3.1-70B-Instruct --dtype bfloat16 --enable-auto-tool-choice --tool-call-parser llama3_json ~~~ send message ~~~ { "model": "meta-llama/Llama-3.1-70B-Instruct", "messa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 27) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: efore Chinese characters. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug start vllm ~~~ vllm serve meta-llama/Llama-3.1-70B-Instruct --dtype bfloat16 --enable-auto-tool...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: hinese, a backslash character "\" appears before Chinese characters. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug start vllm ~~~ vllm serve meta-llama/Llama-3.1-70B-I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
