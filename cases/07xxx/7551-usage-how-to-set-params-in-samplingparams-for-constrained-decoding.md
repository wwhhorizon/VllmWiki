# vllm-project/vllm#7551: [Usage]: how to set params in SamplingParams for constrained decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#7551](https://github.com/vllm-project/vllm/issues/7551) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to set params in SamplingParams for constrained decoding

### Issue 正文摘录

### Your current environment vllm 0.5.0 ### How would you like to use vllm I want to apply constrained decoding for offline inference. I found related doc like:https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#extra-parameters. It seems constrained decoding only can be apply by OpenAI, because i did not find the param "allowed_token_ids" provied in SamplingParams. I don't know how to apply constrained decoding for offline inference.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: or offline inference. I found related doc like:https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#extra-parameters. It seems constrained decoding only can be apply by OpenAI, because i did not find the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
