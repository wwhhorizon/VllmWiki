# vllm-project/vllm#9453: [Bug]: Logprob values are affected by sampling parameters and are incompatible with OpenAI API

| 字段 | 值 |
| --- | --- |
| Issue | [#9453](https://github.com/vllm-project/vllm/issues/9453) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Logprob values are affected by sampling parameters and are incompatible with OpenAI API

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The logprob in vLLM is not the raw probability of the standard LLM loss but is influenced by the sampling parameters. On the other hand, OpenAI returns the raw probability, meaning that no matter how the sampling parameters are set, the logprob of the next token under the same context remains unchanged in OpenAI. I would like vLLM's logprob to be consistent with OpenAI's behavior because logprob should reflect the ideal probability of a token being sampled, independent of the sampling parameters. Additionally, when setting `top_p: 0.0001`, only the first token in `top_logprobs` is correct, while the subsequent tokens are fixed high-frequency tokens (such as `"`, `!`) instead of the current highest-probability tokens. The bug can be reproduced as follows: ```bash curl -X POST "http://39.105.21.95:12481/v1/chat/completions" \ -H "Content-Type: application/json" \ -d '{ "model": "meta-llama/Meta-Llama-3-8B-Instruct", "top_p": 0.0001, "stream": false, "max_tokens":5, "logprobs": true, "top_logprobs": 3, "messages": [ { "role": "user", "content": "just generate a random two-digit integer , no other...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ompatible with OpenAI API bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The logprob in vLLM is not the raw probability of the standard LLM loss but is influenced by th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: affected by sampling parameters and are incompatible with OpenAI API bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The logprob in vLLM is not the raw probability of th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
