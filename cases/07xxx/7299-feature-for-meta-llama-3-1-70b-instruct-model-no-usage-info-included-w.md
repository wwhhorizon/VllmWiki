# vllm-project/vllm#7299: [Feature]: For Meta-Llama-3.1-70B-Instruct model, no usage info included while stream equal to True

| 字段 | 值 |
| --- | --- |
| Issue | [#7299](https://github.com/vllm-project/vllm/issues/7299) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: For Meta-Llama-3.1-70B-Instruct model, no usage info included while stream equal to True

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello, as with Meta-Llama-3-70B output response include usage information which contains prompt_token, total_tokens and completion_tokens in the last chunk. but after deployment with Meta-Llama-3.1-70B-Instruct using latest vllm image (`vllm/vllm-openai:v0.5.4`) I am not getting None usage: ChatCompletionChunk(id='chat-facd596ff0a44e4d2ca48006f11b', choices=[Choice(delta=ChoiceDelta(content='1', function_call=None, refusal=None, role=None, tool_calls=None), finish_reason='length', index=0, logprobs=None, stop_reason=None)], created=1723117897, model='Llama-3.1-70B-Instruct', object='chat.completion.chunk', service_tier=None, system_fingerprint=None, usage=None) please correct me if I am doing wrong anywhere or still usage not added there ? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: For Meta-Llama-3.1-70B-Instruct model, no usage info included while stream equal to True feature request ### 🚀 The feature, motivation and pitch Hello, as with Meta-Llama-3-70B output response include usage i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nstruct model, no usage info included while stream equal to True feature request ### 🚀 The feature, motivation and pitch Hello, as with Meta-Llama-3-70B output response include usage information which contains prompt_to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: st chunk. but after deployment with Meta-Llama-3.1-70B-Instruct using latest vllm image (`vllm/vllm-openai:v0.5.4`) I am not getting None usage: ChatCompletionChunk(id='chat-facd596ff0a44e4d2ca48006f11b', choices=[Choic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
