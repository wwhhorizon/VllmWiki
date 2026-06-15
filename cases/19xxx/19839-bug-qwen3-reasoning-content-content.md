# vllm-project/vllm#19839: [Bug]: qwen3不思考模型，【内容放到reasoning_content，正常应该在content】

| 字段 | 值 |
| --- | --- |
| Issue | [#19839](https://github.com/vllm-project/vllm/issues/19839) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen3不思考模型，【内容放到reasoning_content，正常应该在content】

### Issue 正文摘录

### Your current environment 1 ### 🐛 Describe the bug 使用deepseek思考范式启动的qwen3。 使用参数覆盖功能设置，不让qwen3思考： { "chat_template_kwargs": {"enable_thinking": false} } 返回的结果如下：【内容放到reasoning_content，正常应该在content】 { "id": "chatcmpl-8fd7068f0e534d7e9bd7e0dab6686399", "object": "chat.completion", "created": 1750236511, "model": "matrix-local-llm-reason", "choices": [ { "index": 0, "message": { "role": "assistant", "reasoning_content": "我是Qwen3，阿里巴巴最新推出的通义千问大语言模型。我基于更全面的知识语料，拥有更丰富的语言理解和表达能力。相比之前的版本，我在多个方面都有显著提升：\n\n1. 更强更全的基座模型：基于更全面的知识语料，我拥有更丰富的语言理解和表达能力，包含多个dense和MoE版本，以满足不同场景的需求。\n\n2. 丰富的推理模式选择：我支持多种推理模式的切换，包括适合日常交流的chat模式和专注推理的reasoning模式，满足用户更复杂、更精确的交互需求。\n\n3. 卓越的推理能力：我的逻辑推理、数学计算以及代码生成能力得到全面强化和优化，能够更高效、更准确地处理具有挑战性的推理任务。\n\n4. 全方位通用对话能力：经过更深入的优化与迭代，我现在能够流畅地进行内容创作、多轮对话、角色扮演，甚至支持智能Agent交互体验，营造更自然、更沉浸的对话环境。\n\n5. 更广泛的多语言支持：我的语言能力覆盖全球超过100种主流语言，满足全球化、多样化的语言交流需求，更好地服务国际用户。\n\n如果你有任何问题或需要帮助，欢迎随时告诉我！", "content": null, "tool_calls": [] }, "logprobs": null, "finish_reason": "stop", "stop_reason": null } 【内容放到reasoning_content，正常应该在content】 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [doc...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen3不思考模型，【内容放到reasoning_content，正常应该在content】 bug;stale ### Your current environment 1 ### 🐛 Describe the bug 使用deepseek思考范式启动的qwen3。 使用参数覆盖功能设置，不让qwen3思考： { "chat_template_kwargs": {"enable_thinking": false} }...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nt】 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 3。 使用参数覆盖功能设置，不让qwen3思考： { "chat_template_kwargs": {"enable_thinking": false} } 返回的结果如下：【内容放到reasoning_content，正常应该在content】 { "id": "chatcmpl-8fd7068f0e534d7e9bd7e0dab6686399", "object": "chat.completion", "created": 1...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: 前的版本，我在多个方面都有显著提升：\n\n1. 更强更全的基座模型：基于更全面的知识语料，我拥有更丰富的语言理解和表达能力，包含多个dense和MoE版本，以满足不同场景的需求。\n\n2. 丰富的推理模式选择：我支持多种推理模式的切换，包括适合日常交流的chat模式和专注推理的reasoning模式，满足用户更复杂、更精确的交互需求。\n\n3. 卓越的推理能力：我的逻辑推理、数学计算以及代码生成能力得到全面强化和优化，能够更高效...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: qwen3不思考模型，【内容放到reasoning_content，正常应该在content】 bug;stale ### Your current environment 1 ### 🐛 Describe the bug 使用deepseek思考范式启动的qwen3。 使用参数覆盖功能设置，不让qwen3思考： { "chat_template_kwargs": {"enable_thinking": false} }...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
