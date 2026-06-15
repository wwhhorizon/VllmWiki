# vllm-project/vllm#21156: [Bug]: When making a streaming request, the 9-digit integer in the function call result will be truncated to 6 digits

| 字段 | 值 |
| --- | --- |
| Issue | [#21156](https://github.com/vllm-project/vllm/issues/21156) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: When making a streaming request, the 9-digit integer in the function call result will be truncated to 6 digits

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use vllm by vllm/vllm-openai:v0.9.1 docker image, docker run arguments: --model Qwen/Qwen3-8B --enable-auto-tool-choice --tool-call-parser hermes --chat-template /root/vllm/qwen3_nonthinking.jinja --max-model-len=32768 use /v1/chat/completions api: ```json { "messages": [ { "role": "system", "content": "\n\n# 知识库\n\n当前时间：2025-07-18 09:05:54\n\n\n\n\n# 指令\n\n你是一个人类助手，可以利用工具帮助人类做许多事情。\n\n请注意：\n1. 你可以调用工具来绘制图表，不需要展示图表，也不要展示图片url，你只用说你已绘制图表即可。\n2. 如果用户闲聊，请你建议用户提供资源名称以帮助用户检索资源并进行后续的分析等操作。\n3. 如果用户提问模糊，请你基于上述工具推测用户的意图并继续询问用户。\n4. 如果用户提到或使用某些资源、某些数据或某些数据集但是没有提供它们的id，请你先使用资源搜索工具依次查询每一份资源。\n5. 当用户没有指定工具的某些参数值时，你需要按照下面两种情况进行处理：（1）该参数为必须参数时，禁止使用你自己的理解生成参数值，必须与用户进行对话获取参数值；（2）该参数为非必须参数且标注有默认值时，直接使用默认值进行工具调用，不需要再与用户进行对话获取。\n" }, { "role": "user", "content": "使用“北京住宅小区分布”数据，根据“单价”字段，制作一幅热力图" }, { "content": null, "role": "assistant", "function_call": null, "tool_calls": [ { "id": "chatcmpl-tool-88673f15f2274a19aff8466ba78b601a", "function": { "arguments": "{\"text\": \"北京住宅小区分布\", \"resource_type\": \"DATA\"}", "name": "resource_search" }, "type": "function" } ], "reasoning_content": null }, { "role": "tool", "content": "{\"resource_list\": [...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: onment ### 🐛 Describe the bug I use vllm by vllm/vllm-openai:v0.9.1 docker image, docker run arguments: --model Qwen/Qwen3-8B --enable-auto-tool-choice --tool-call-parser hermes --chat-template /root/vllm/qwen3_nonthink...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: When making a streaming request, the 9-digit integer in the function call result will be truncated to 6 digits bug;stale ### Your current environment ### 🐛 Describe the bug I use vllm by vllm/vllm-openai:v0.9.1 d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: resource_type\": \"DATA\"}", "name": "resource_search" }, "type": "function" } ], "reasoning_content": null }, { "role": "tool", "content": "{\"resou
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: se vllm by vllm/vllm-openai:v0.9.1 docker image, docker run arguments: --model Qwen/Qwen3-8B --enable-auto-tool-choice --tool-call-parser hermes --chat-template /root/vllm/qwen3_nonthinking.jinja --max-model-len=32768 u...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
