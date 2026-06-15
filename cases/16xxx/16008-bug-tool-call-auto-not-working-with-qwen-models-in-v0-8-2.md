# vllm-project/vllm#16008: [Bug]: Tool call auto not working with Qwen models in v0.8.2

| 字段 | 值 |
| --- | --- |
| Issue | [#16008](https://github.com/vllm-project/vllm/issues/16008) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tool call auto not working with Qwen models in v0.8.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Getting hallucination response on Qwen tools call and no tool_calls output at all. It works fine in v0.8.1 sample output: ``` {"id":"chatcmpl-cd27f78c6e22498fa95736e040210fd9","object":"chat.completion","created":1743588875,"model":"Qwen/Qwen2.5-7B-Instruct-AWQ","choices":[{"index":0,"message":{"role":"assistant","reasoning_content":null,"content":" כאיל אפשרותObs.ShouldBe /v1/chat/completions" \ -H "Content-Type: application/json" \ --data \ "{ \"model\": \"Qwen/Qwen2.5-7B-Instruct-AWQ\", \"max_tokens\": 1024, \"messages\": $(echo ${MESSAGES} |jq '[.[]|tojson|fromjson]'), \"tools\": $(echo ${TOOLS} |jq '[.[]|tojson|fromjson]') }" ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: le ### Your current environment ### 🐛 Describe the bug Getting hallucination response on Qwen tools call and no tool_calls output at all. It works fine in v0.8.1 sample output: ``` {"id":"chatcmpl-cd27f78c6e22498fa95736...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Tool call auto not working with Qwen models in v0.8.2 bug;stale ### Your current environment ### 🐛 Describe the bug Getting hallucination response on Qwen tools call and no tool_calls output at all. It works fine...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Tool call auto not working with Qwen models in v0.8.2 bug;stale ### Your current environment ### 🐛 Describe the bug Getting hallucination response on Qwen tools call and no tool_calls output at all. It works fine...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
