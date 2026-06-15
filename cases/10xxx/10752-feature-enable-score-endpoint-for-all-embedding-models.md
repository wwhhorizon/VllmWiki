# vllm-project/vllm#10752: [Feature]: Enable `/score` endpoint for all embedding models

| 字段 | 值 |
| --- | --- |
| Issue | [#10752](https://github.com/vllm-project/vllm/issues/10752) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enable `/score` endpoint for all embedding models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently only cross-encoder models support the `/score` endpoint. But it would make sense to enable it also for the embedding models using bi-encoding, i.e. calculating a cosine similarity score between the embedding vectors. cc: @DarkLight1337 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Enable `/score` endpoint for all embedding models feature request ### 🚀 The feature, motivation and pitch Currently only cross-encoder models support the `/score` endpoint. But it would make sense to enable i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Enable `/score` endpoint for all embedding models feature request ### 🚀 The feature, motivation and pitch Currently only cross-encoder models support the `/score` endpoint. But it would make sense to enable i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
