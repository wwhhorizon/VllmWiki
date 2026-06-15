# vllm-project/vllm#10607: [Feature]: When apply prompt_logprobs for OpenAI server, the prompt_logprobs field in respnose does not show which token is chosen

| 字段 | 值 |
| --- | --- |
| Issue | [#10607](https://github.com/vllm-project/vllm/issues/10607) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: When apply prompt_logprobs for OpenAI server, the prompt_logprobs field in respnose does not show which token is chosen

### Issue 正文摘录

### Your current environment vLLM Version: 0.6.3.post2.dev256+g4be3a451 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Reproduce code: ```bash curl -X POST "http://39.105.21.95:12481/v1/chat/completions" \ -H "Content-Type: application/json" \ -d '{ "model": "meta-llama/Meta-Llama-3-8B-Instruct", "messages": [ { "role": "user", "content": "just reply [🍓]" }, { "role": "assistant", "content": "[🍓" } ], "logprobs":true, "prompt_logprobs":2, "max_tokens":1 }' ``` The prompt_logprobs field in respnose like this: ```js {'4345': {'logprob': -30.0319766998291, 'rank': 35807, 'decoded_token': 'just'}, '40': {'logprob': -0.31130534410476685, 'rank': 1, 'decoded_token': 'I'}, '3923': {'logprob': -1.3839313983917236, 'rank': 2, 'decoded_token': 'What'}}, {'10052': {'logprob': -11.685066223144531, 'rank': 299, 'decoded_token': ' reply'}, '264': {'logprob': -0.7353454828262329, 'rank': 1, 'decoded_token': ' a'}, '369': {'logprob': -2.165513515472412, 'rank': 2, 'decoded_token': ' for'}} ``` It's a list of dicts, the dicts' key is token ID and don't contain which token is chosen. Although, first key (token ID) in the prompt_logprobs dict would be the chosen token, but in the json sp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: token is chosen feature request;stale ### Your current environment vLLM Version: 0.6.3.post2.dev256+g4be3a451 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Reproduce code: ```bash curl -X POST "http://39.10...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: t_logprobs field in respnose does not show which token is chosen feature request;stale ### Your current environment vLLM Version: 0.6.3.post2.dev256+g4be3a451 ### Model Input Dumps _No response_ ### 🐛 Describe the bug R...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: r current environment vLLM Version: 0.6.3.post2.dev256+g4be3a451 ### Model Input Dumps _No response_ ### 🐛 Describe the bug Reproduce code: ```bash curl -X POST "http://39.105.21.95:12481/v1/chat/completions" \ -H "Cont...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
