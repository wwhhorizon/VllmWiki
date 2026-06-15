# vllm-project/vllm#42729: [RFC]: Derender Endpoints to Provide Detokenization for Disaggregated Serving

| 字段 | 值 |
| --- | --- |
| Issue | [#42729](https://github.com/vllm-project/vllm/issues/42729) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Derender Endpoints to Provide Detokenization for Disaggregated Serving

### Issue 正文摘录

### Motivation. The `/render` endpoints (`POST /v1/chat/completions/render` and `POST /v1/completions/render`) landed in PR #36166 as the preprocessing leg of disaggregated serving. They accept a standard OpenAI request and return a`GenerateRequest` that the GPU inference tier can consume directly without a tokenizer. After generation, the inference server (`/inference/v1/generate`) returns a `GenerateResponse` containing raw output token IDs, along with logprob entries encoded as `"token_id:N"` placeholder strings because the generate server has no tokenizer. To turn that into a client-facing OpenAI response, we need to: 1. Detokenize the output token IDs back into text 2. Resolve `"token_id:N"` logprob placeholders into real token strings 3. Populate the `bytes` field in logprob entries (required by the OpenAI spec, cannot be filled by the tokenizer-free generate server) 4. Format the result as a `ChatCompletionResponse` or `CompletionResponse` Currently this postprocessing is coupled to `OpenAIServingChat` /`OpenAIServingCompletion` inside the GPU server. Operators running llm-d, Dynamo, or any other disaggregated setup are forced to either run the full vLLM stack on the CPU ti...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: OpenAI spec, cannot be filled by the tokenizer-free generate server) 4. Format the result as a `ChatCompletionResponse` or `CompletionResponse` Currently this postprocessing is coupled to `OpenAIServingChat` /`OpenAISer...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: cause the generate server has no tokenizer. To turn that into a client-facing OpenAI response, we need to: 1. Detokenize the output token IDs back into text 2. Resolve `"token_id:N"` logprob placeholders into real token...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tokens` is provided its length must equal `len(generate_responses)`. A mismatch will return `400 Bad Request`. ##### Example Requests ```bash curl -X POST http://localhost:8000/v1/chat/completions/derender \ -H "Content...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: reprocessing leg of disaggregated serving. They accept a standard OpenAI request and return a`GenerateRequest` that the GPU inference tier can consume directly without a tokenizer. After generation, the inference server...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t_tokens` is provided its length must equal `len(generate_responses)`. A mismatch will return `400 Bad Request`. ##### Example Requests ```bash curl -X POST http://localhost:8000/v1/chat/completions/derender \ -H "Conte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
