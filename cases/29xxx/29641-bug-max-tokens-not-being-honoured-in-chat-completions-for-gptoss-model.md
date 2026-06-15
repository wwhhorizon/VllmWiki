# vllm-project/vllm#29641: [Bug]: Max Tokens not being honoured in Chat Completions for GPTOSS model

| 字段 | 值 |
| --- | --- |
| Issue | [#29641](https://github.com/vllm-project/vllm/issues/29641) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Max Tokens not being honoured in Chat Completions for GPTOSS model

### Issue 正文摘录

### Your current environment It seems that in the latest version of vllm 0.11+ Chat Completions has stopped honouring `max_tokens` with GPTOSS 120B model, the below request payload has stopped working with `max_tokens` earlier the same payload would provide an output to the limit of the `max_tokens` provided.. Interestingly if you look at the `usage` tokens, it's showing `completion_tokens` as 500 but the output is BLANK. ```json { "messages": [ { "role": "user", "content": "What is the role of AI in medicine?" } ], "model": "openai/gpt-oss-120b", "max_tokens": 500, "reasoning": {"effort": "low"}, "stream": false } ``` getting BLANK output, even though the `usage` is showing token counts created is matching max_tokens ```json { "id": "chatcmpl-c71e934ac0b74bd4b8f99fe9b5516ea3", "object": "chat.completion", "created": 1764300020, "model": "openai/gpt-oss-120b", "choices": [ { "index": 0, "message": { "role": "assistant", "content": null, "refusal": null, "annotations": null, "audio": null, "function_call": null, "tool_calls": [], "reasoning": "Need to answer.", "reasoning_content": "Need to answer." }, "logprobs": null, "finish_reason": "length", "stop_reason": null, "token_ids": n...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: TOSS model bug ### Your current environment It seems that in the latest version of vllm 0.11+ Chat Completions has stopped honouring `max_tokens` with GPTOSS 120B model, the below request payload has stopped working wit...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Max Tokens not being honoured in Chat Completions for GPTOSS model bug ### Your current environment It seems that in the latest version of vllm 0.11+ Chat Completions has stopped honouring `max_tokens` with GPTOS...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: adiology: Google DeepMind’s AI detects lung cancer on CT scans with >95% accuracy. • Dermatology: FDA‑cleared apps (e.g., SkinVision) classify skin lesions from photos. • Pathology: Paige.ai assists in detecting prostat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: • GE Healthcare’s AI‐driven inventory management. |\n\n---\n\n## 4. Research & Drug Development\n\n| Stage | AI Contribution | Notable Projects |\n|-------|----------------|------------------|\n| **Target Identification...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: or GPTOSS model bug ### Your current environment It seems that in the latest version of vllm 0.11+ Chat Completions has stopped honouring `max_tokens` with GPTOSS 120B model, the below request payload has stopped workin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
