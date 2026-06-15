# vllm-project/vllm#16546: [Feature]: Return logprobs tensor

| 字段 | 值 |
| --- | --- |
| Issue | [#16546](https://github.com/vllm-project/vllm/issues/16546) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Return logprobs tensor

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Is it possible to get the full prompt_logprobs/logprobs tensor output? Right now I can do this by specifying prompt_logprobs/logprobs=vocab_size, but this returns the top-k sorted list and I have to iterate through it to format it back into the tensor which is extremely slow in python. I need this for calculating eval loss ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Return logprobs tensor feature request;stale ### 🚀 The feature, motivation and pitch Is it possible to get the full prompt_logprobs/logprobs tensor output? Right now I can do this by specifying prompt_logprob...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: he tensor which is extremely slow in python. I need this for calculating eval loss ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already sea...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ll prompt_logprobs/logprobs tensor output? Right now I can do this by specifying prompt_logprobs/logprobs=vocab_size, but this returns the top-k sorted list and I have to iterate through it to format it back into the te...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t this returns the top-k sorted list and I have to iterate through it to format it back into the tensor which is extremely slow in python. I need this for calculating eval loss ### Alternatives _No response_ ### Additio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
