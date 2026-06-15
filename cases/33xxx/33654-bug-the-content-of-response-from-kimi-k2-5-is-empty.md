# vllm-project/vllm#33654: [Bug]: The content of response from Kimi-K2.5 is empty.

| 字段 | 值 |
| --- | --- |
| Issue | [#33654](https://github.com/vllm-project/vllm/issues/33654) |
| 状态 | open |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The content of response from Kimi-K2.5 is empty.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I`m running Kimi-K2.5 with vllm-0.15.0, and I find that when the "max_tokens" in a request is less than 330, the content of response is empty, it`s so strange. This is my command to start the engine: ''' vllm serve moonshotai/Kimi-K2.5 \ -tp 8 \ --mm-encoder-tp-mode data \ --trust-remote-code \ --tool-call-parser kimi_k2 \ --reasoning-parser kimi_k2 \ --max-parallel-loading-workers 8 \ --disable-log-requests ''' And this is my test request: ''' curl localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "messages": [ { "role": "system", "content": "You are Kimi, an AI assistant created by Moonshot AI." }, { "role": "user", "content": "which one is bigger, 9.11 or 9.9? think carefully." } ], "temperature": 0.7, "max_tokens": 329 }' ''' while the response is here: ''' {"id":"chatcmpl-93a3c11a1f87fb5c","object":"chat.completion","created":1770098358,"model":"moonshotai/Kimi-K2.5","choices":[{"index":0,"message":{"role":"assistant",**"content":null**,"refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning":" The user is asking which number is bigger: 9.11 or 9.9. This i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: trick\" question that plays on how people sometimes mistakenly compare decimal numbers as if they were whole numbers or version numbers.\n\nLet me think about this carefully:\n\n1. If we treat these as decimal numbers:\...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ''' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: g Kimi-K2.5 with vllm-0.15.0, and I find that when the "max_tokens" in a request is less than 330, the content of response is empty, it`s so strange. This is my command to start the engine: ''' vllm serve moonshotai/Kim...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf env_dependency;memory_layout Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ;gemm;operator;sampling;triton build_error;nan_inf env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
