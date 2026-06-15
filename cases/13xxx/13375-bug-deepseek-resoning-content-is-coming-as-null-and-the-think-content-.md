# vllm-project/vllm#13375: [Bug]: Deepseek resoning content is coming as null and the think content is going inside content when using vllm-openai v0.7.2 docker containers

| 字段 | 值 |
| --- | --- |
| Issue | [#13375](https://github.com/vllm-project/vllm/issues/13375) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Deepseek resoning content is coming as null and the think content is going inside content when using vllm-openai v0.7.2 docker containers

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running "deepseek-ai/DeepSeek-R1-Distill-Llama-8B" model using docker with parameters: --enable-reasoning --reasoning-parser deepseek_r1 --max-model-len 16800 As per the documentation, all the content should go under the key reasoning_content. When I am testing the deployment using /chat/completions api , the reasoning content is coming as null and the actual reasoning content is going inside the content key. Request: { "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B", "messages": [ {"role": "user", "content": "9.11 and 9.8, which is greater?"} ] } Response: { "id": "chatcmpl-f55ac124e83d4df297cbdd133b28cc5f", "object": "chat.completion", "created": 1739728395, "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B", "choices": [ { "index": 0, "message": { "role": "assistant", "reasoning_content": null, "content": "First, I need to compare the two numerical values, 9.11 and 9.8.\n\nTo make the comparison easier, I'll align both numbers by their decimal places. I can rewrite 9.8 as 9.80.\n\nNow, I'll compare the numbers digit by digit. Both have the same whole number part, 9.\n\nNext, I'll look at the tenths place: 1 in 9.11 a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: the think content is going inside content when using vllm-openai v0.7.2 docker containers bug;stale ### Your current environment ### 🐛 Describe the bug I am running "deepseek-ai/DeepSeek-R1-Distill-Llama-8B" model using...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: going inside content when using vllm-openai v0.7.2 docker containers bug;stale ### Your current environment ### 🐛 Describe the bug I am running "deepseek-ai/DeepSeek-R1-Distill-Llama-8B" model using docker with paramete...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ent": null, "content": "First, I need to compare the two numerical values, 9.11 and 9.8.\n\nTo make the comparison easier, I'll align both numbers by their decimal places. I can rewrite 9.8 as 9.80.\n\nNow, I'll compare...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l } ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🐛 Describe the bug I am running "deepseek-ai/DeepSeek-R1-Distill-Llama-8B" model using docker with parameters: --enable-reasoning --reasoning-parser deepseek_r1 --max-model-len 16800 As per the documentation, all th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
