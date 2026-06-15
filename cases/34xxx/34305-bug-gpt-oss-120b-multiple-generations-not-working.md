# vllm-project/vllm#34305: [Bug]: gpt-oss-120b Multiple generations not working

| 字段 | 值 |
| --- | --- |
| Issue | [#34305](https://github.com/vllm-project/vllm/issues/34305) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: gpt-oss-120b Multiple generations not working

### Issue 正文摘录

### 🐛 Describe the bug I'm trying to generate multiple assistant completions with tool calls for the same user message and system prompt. I tried setting `n` = 2 and 3, but I only see completion. The model I'm interested in is `gpt-oss-120b`. The model is deployed in NVIDIA Dynamo with vLLM backend and the exact runtime image is https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/vllm-runtime?version=0.7.0. ``` curl -X POST http://localhost:${SVC_PORT}/v1/chat/completions \ -H "Content-Type: application/json" \ -d "{ \"model\": \"${MODEL_NAME}\", \"messages\": [ {\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}, {\"role\": \"user\", \"content\": \"What is opposite of big?\"} ], \"max_tokens\": 200, \"temperature\": 0.7, \"stream\": false, \"n\": 3 }" {"id":"chatcmpl-f217e1ce-ab3a-41a6-94d7-e5c9546ae8f2","choices":[{"index":0,"message":{"content":"The opposite of **big** is **small** (or synonyms like “tiny,” “little,” etc.). to be).","role":"assistant","reasoning_content":"The user asks: \"What is opposite of big?\" Simple answer: \"small\". Could also mention \"tiny\". Provide answer."},"finish_reason":"stop"}],"created":1770783121,"model":"g...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: gpt-oss-120b Multiple generations not working bug ### 🐛 Describe the bug I'm trying to generate multiple assistant completions with tool calls for the same user message and system prompt. I tried setting `n` = 2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: "choices":[{"index":0,"message":{"content":"The opposite of **big** is **small** (or synonyms like “tiny,” “little,” etc.). to be).","role":"assistant","reasoning_content":"The user asks: \"What is opposite of big?\" Si...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: in is `gpt-oss-120b`. The model is deployed in NVIDIA Dynamo with vLLM backend and the exact runtime image is https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/vllm-runtime?version=0.7.0. ``` curl -X...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: talog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/vllm-runtime?version=0.7.0. ``` curl -X POST http://localhost:${SVC_PORT}/v1/chat/completions \ -H "Content-Type: application/json" \ -d "{ \"model\": \"${MODE...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ], \"max_tokens\": 200, \"temperature\": 0.7, \"stream\": false, \"n\": 3 }" {"id":"chatcmpl-f217e1ce-ab3a-41a6-94d7-e5c9546ae8f2","choices":[{"index":0,"message":{"content":"The opposite of **big** is **small** (or syn...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
