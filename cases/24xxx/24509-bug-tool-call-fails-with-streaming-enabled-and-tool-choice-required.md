# vllm-project/vllm#24509: [Bug]: Tool call fails with streaming enabled and tool_choice "required"

| 字段 | 值 |
| --- | --- |
| Issue | [#24509](https://github.com/vllm-project/vllm/issues/24509) |
| 状态 | closed |
| 标签 | bug;tool-calling |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tool call fails with streaming enabled and tool_choice "required"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Bug found by @ndebeiss in https://github.com/vllm-project/vllm/pull/19425#issuecomment-3245918269 ## Issue origin `previous_texts[i]` is updated twice and the `delta_text` ends up added twice to the `previous_texts[i]` `previous_texts[i]` updated if `request.tool_choice == "required":` https://github.com/vllm-project/vllm/blob/1da94e673c257373280026f75ceb4effac80e892/vllm/entrypoints/openai/serving_chat.py#L765 `delta_text` added to `previous_texts[i]` https://github.com/vllm-project/vllm/blob/1da94e673c257373280026f75ceb4effac80e892/vllm/entrypoints/openai/serving_chat.py#L876 ## Reproducer The bug is triggered when - model is started with `--enable-auto-tool-choice` - and request has `"stream":true` and `"tool_choice":"required"` ```bash vllm serve meta-llama/Llama-3.1-8B-Instruct --enable-log-requests --enable-auto-tool-choice --tool-call-parser llama3_json ``` ```bash curl -i -X POST \ -H "Content-Type:application/json" \ -d \ '{ "messages":[ { "content":"Combien font 9-5 ?", "role":"user" }], "stream":true, "tools":[ { "type":"function", "function":{ "name":"substractor", "description":"Soustrait 2 valeurs num..riques", "par...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ERROR 09-09 13:18:55 [serving_chat.py:1051] File "/home/avigny/.pyenv/versions/3.12.11/lib/python3.12/json/__init__.py", line 346, in loads (APIServer pid=24867) ERROR 09-09 13:18:55 [serving_chat.py:1051] return _defau...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: added twice to the `previous_texts[i]` `previous_texts[i]` updated if `request.tool_choice == "required":` https://github.com/vllm-project/vllm/blob/1da94e673c257373280026f75ceb4effac80e892/vllm/entrypoints/openai/servi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s/openai/serving_chat.py#L876 ## Reproducer The bug is triggered when - model is started with `--enable-auto-tool-choice` - and request has `"stream":true` and `"tool_choice":"required"` ```bash vllm serve meta-llama/Ll...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
