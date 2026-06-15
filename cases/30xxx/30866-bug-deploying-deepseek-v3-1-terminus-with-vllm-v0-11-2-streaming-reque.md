# vllm-project/vllm#30866: [Bug]: Deploying DeepSeek-V3.1-Terminus with vLLM v0.11.2, streaming requests that include tool calls suffer from a missing first token issue.

| 字段 | 值 |
| --- | --- |
| Issue | [#30866](https://github.com/vllm-project/vllm/issues/30866) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deploying DeepSeek-V3.1-Terminus with vLLM v0.11.2, streaming requests that include tool calls suffer from a missing first token issue.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After deploying DeepSeek-V3.1-Terminus with vLLM v0.11.2, streaming requests that include tool calls suffer from a missing first token issue. Like this: data: {"id":"chatcmpl-ebce7364-aab6-9b58-bccd-68a1b1352c58","object":"chat.completion.chunk","created":1765969107,"model":"deepseek-v31-bak","choices":[{"index":0,"delta":{"role":"assistant","content":"","reasoning_content":null},"logprobs":null,"finish_reason":null}],"prompt_token_ids":null} data: {"id":"chatcmpl-ebce7364-aab6-9b58-bccd-68a1b1352c58","object":"chat.completion.chunk","created":1765969107,"model":"deepseek-v31-bak","choices":[{"index":0,"delta":{"content":null,"reasoning_content":null},"logprobs":null,"finish_reason":null,"token_ids":null}]} (the content and reasoning_content of this stream chunk is both null, which is unnormal) data: {"id":"chatcmpl-ebce7364-aab6-9b58-bccd-68a1b1352c58","object":"chat.completion.chunk","created":1765969107,"model":"deepseek-v31-bak","choices":[{"index":0,"delta":{"content":"UB","reasoning_content":null},"logprobs":null,"finish_reason":null,"token_ids":null}]} data: {"id":"chatcmpl-ebce7364-aab6-9b58-bccd-68a1b1352c58","object":"c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: }]} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Deploying DeepSeek-V3.1-Terminus with vLLM v0.11.2, streaming requests that include tool calls suffer from a missing first token issue. bug;stale ### Your current environment ### 🐛 Describe the bug After deployin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: el;frontend_api;gemm_linear;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ccd-68a1b1352c58","object":"chat.completion.chunk","created":1765969107,"model":"deepseek-v31-bak","choices":[{"index":0,"delta":{"role":"assistant","content":"","reasoning_content":null},"logprobs":null,"finish_reason"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
