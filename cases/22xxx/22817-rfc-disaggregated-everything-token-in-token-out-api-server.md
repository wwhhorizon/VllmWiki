# vllm-project/vllm#22817: [RFC]: Disaggregated Everything - Token In <> Token Out API Server

| 字段 | 值 |
| --- | --- |
| Issue | [#22817](https://github.com/vllm-project/vllm/issues/22817) |
| 状态 | open |
| 标签 | RFC;keep-open;rl |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Disaggregated Everything - Token In <> Token Out API Server

### Issue 正文摘录

### Motivation. We have seen asks from multiple groups to offer a token-in / token-out API for vLLM, including: - disaggregated tokenization/MM input processing use cases (e.g. llm-d, Dynamo, etc) - custom frontends around vLLM (for users doing custom tool calling, MM input processing) - RL use cases ### Proposed Change. #### Existing MM Refactor Effort There is an existing effort in vLLM to refactor MM input processing (#22880 by @WoosukKwon and @ywang96) to convert the `Processor` class to a `Renderer` class which : - Has much less layers of abstraction - Does not necessarily need to use the HF Processor class (allow custom implementation for model providers) - Sits outside the AsyncLLM (at the API server level) Goal is to introduce a new class called a “Renderer”, which: - Converts OpenAI Spec → Tokens, MM Features, etc - Sits “Outside” the AsyncLLM (so moved to the API Server level) - AsyncLLM becomes tokens in >> tokens out #### Enabling Token-In | Token-Out API Server As the AsyncLLM interface becomes token-in/tokens-out, we can wrap this in an API. Create a clear class, document, make it an external API - Note: `GenerateRequest` roughly maps to `EngineCoreRequest` - Note: `...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s much less layers of abstraction - Does not necessarily need to use the HF Processor class (allow custom implementation for model providers) - Sits outside the AsyncLLM (at the API server level) Goal is to introduce a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ## Disaggregated Tokenization With a tokens-in / tokens-out API, we can build a disaggregated tokenization architecture for large scale serving ```bash # microservice for renderer vllm renderer $MODEL /v1/chat/completio...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ut API, we can build a disaggregated tokenization architecture for large scale serving ```bash # microservice for renderer vllm renderer $MODEL /v1/chat/completions/render input: ChatCompletionRequest output: GenerateRe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: a tokens-in / tokens-out API, we can build a disaggregated tokenization architecture for large scale serving ```bash # microservice for renderer vllm renderer $MODEL /v1/chat/completions/render input: ChatCompletionRequ...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Create a clear class, document, make it an external API - Note: `GenerateRequest` roughly maps to `EngineCoreRequest` - Note: `GenerateResponse` roughly maps to `EngineCoreOutput` - `/generate` that maps to the new `Asy...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
