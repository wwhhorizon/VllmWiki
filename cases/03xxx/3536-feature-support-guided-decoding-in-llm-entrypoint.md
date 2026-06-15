# vllm-project/vllm#3536: [Feature]: Support Guided Decoding in `LLM` entrypoint

| 字段 | 值 |
| --- | --- |
| Issue | [#3536](https://github.com/vllm-project/vllm/issues/3536) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Guided Decoding in `LLM` entrypoint

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently we support guided decoding of (JSON, Regex, Choice, Grammar, and arbitrary JSON) in OpenAI inference server. It would be great that we expose the same functionality in the offline interface as well. https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#extra-parameters Concretely this would mean adding the support here as a new parameter to generate call. Using methods introduced in #2819. Do make sure to add test and examples. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support Guided Decoding in `LLM` entrypoint feature request ### 🚀 The feature, motivation and pitch Currently we support guided decoding of (JSON, Regex, Choice, Grammar, and arbitrary JSON) in OpenAI inferen...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ctionality in the offline interface as well. https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#extra-parameters Concretely this would mean adding the support here as a new parameter to generate call....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
