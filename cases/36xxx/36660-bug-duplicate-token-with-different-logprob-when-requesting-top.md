# vllm-project/vllm#36660: [Bug]: Duplicate token with different logprob when requesting top

| 字段 | 值 |
| --- | --- |
| Issue | [#36660](https://github.com/vllm-project/vllm/issues/36660) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Duplicate token with different logprob when requesting top

### Issue 正文摘录

### Your current environment I am using vLLM 0.14 within the AWS LMI container: 763104351884.dkr.ecr.us-west-2.amazonaws.com/djl-inference:0.36.0-lmi19.0.0-cu128 ### 🐛 Describe the bug When requesting top_logprobs = 5 using the OpenAI chat completion schema (loprobs: True, max_tokens:1, max_completion_tokens:1), I get duplicate tokens with different probabilities. `Example: output["choices"][0]["logprobs"]["content"][0]["top_logprobs"] -> [{'token': 'none', 'logprob': -0.0012816318776458502, 'bytes': [110, 111, 110, 101]}, {'token': 'helper', 'logprob': -7.25128173828125, 'bytes': [104, 101, 108, 112, 101, 114]}, {'token': 'explanation', 'logprob': -7.75128173828125, 'bytes': [101, 120, 112, 108, 97, 110, 97, 116, 105, 111, 110]}, {'token': 'None', 'logprob': -9.87628173828125, 'bytes': [78, 111, 110, 101]}, {'token': 'none', 'logprob': -10.43878173828125, 'bytes': [110, 111, 110, 101]}]` Notice the first and last tokens in the serie are identical in name and sequence of bytes, but have different log probabilities. Why does this happen? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right co...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: en? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Duplicate token with different logprob when requesting top bug ### Your current environment I am using vLLM 0.14 within the AWS LMI container: 763104351884.dkr.ecr.us-west-2.amazonaws.com/djl-inference:0.36.0-lmi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
