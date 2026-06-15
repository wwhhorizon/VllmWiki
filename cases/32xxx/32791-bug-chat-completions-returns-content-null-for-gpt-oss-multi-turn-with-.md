# vllm-project/vllm#32791: [Bug]: chat.completions returns content: null for GPT-OSS multi-turn with json_object

| 字段 | 值 |
| --- | --- |
| Issue | [#32791](https://github.com/vllm-project/vllm/issues/32791) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 29; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: chat.completions returns content: null for GPT-OSS multi-turn with json_object

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Summary** When using GPT-OSS (openai/gpt-oss-120b) with vLLM Chat Completions, combining: - multi-turn conversation and - response_format: { "type": "json_object" } results in message.content == null, invalid JSON, or whitespace/repetition loops — even for trivial prompts. The same prompt works in: - single-turn Chat Completions, - multi-turn Chat Completions without JSON mode, - and via /v1/completions (raw generation). This strongly suggests a bug in vLLM’s Chat Completions adapter / Harmony parsing layer, not in the model or decoding itself. **Reproduction** (TL,DR: skip to case 3 below) All cases use the same instruction: “Respond with JSON only in the form {"response":"bye"}.” Only turn structure / grammar differs. **CASE 0 — Single turn, no JSON mode (baseline, works)** ```bash curl -s http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -H "Authorization: Bearer dummy" \ -d '{ "model": "openai/gpt-oss-120b", "messages": [ { "role": "user", "content": "Respond with JSON only in the form {\"response\":\"bye\"}." } ], "max_tokens": 128, "temperature": 0 }' ``` Expected: {"response":"bye"} in cho...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: red fields and additionalProperties: false - Switching structured output backend (xgrammar vs outlines) - Enabling and disabling grammar fallback - Enabling and disabling whitespace allowance - Disabling prefix caching...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ses Chat Completions packaging and shows the raw Harmony output, with special tokens preserved. ```bash curl -s http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -H "Authorization: Bearer dumm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: chat.completions returns content: null for GPT-OSS multi-turn with json_object bug ### Your current environment ### 🐛 Describe the bug **Summary** When using GPT-OSS (openai/gpt-oss-120b) with vLLM Chat Completio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ns. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: prompt_token_ids": null, "kv_transfer_params": null } ``` This occurs deterministically. **CASE 4 — OPTIONAL: Same as Case 3 via /v1/completions (works, raw tokens shown)** This bypasses Chat Completions packaging and s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
