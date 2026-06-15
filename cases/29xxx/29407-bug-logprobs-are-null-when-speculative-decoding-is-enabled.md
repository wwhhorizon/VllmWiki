# vllm-project/vllm#29407: [Bug]: Logprobs are null when speculative decoding is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#29407](https://github.com/vllm-project/vllm/issues/29407) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Logprobs are null when speculative decoding is enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In the current vLLM setup, when speculative decoding is active and a user requests logprobs, some tokens might show null values for top_logprobs. This occurs because vLLM only provides one set of logprobs per step, while multiple token IDs can be produced, leading to inconsistencies in the final output. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Logprobs are null when speculative decoding is enabled bug ### Your current environment ### 🐛 Describe the bug In the current vLLM setup, when speculative decoding is active and a user requests logprobs, some tok...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: er step, while multiple token IDs can be produced, leading to inconsistencies in the final output. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot liv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ut. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
