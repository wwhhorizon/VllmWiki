# vllm-project/vllm#31342: [Bug]: vllm profiler cannot working

| 字段 | 值 |
| --- | --- |
| Issue | [#31342](https://github.com/vllm-project/vllm/issues/31342) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm profiler cannot working

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug https://docs.vllm.ai/en/latest/contributing/profiling/#profile-with-pytorch-profiler ref this doc to use, it can not working. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: vllm profiler cannot working bug ### Your current environment ### 🐛 Describe the bug https://docs.vllm.ai/en/latest/contributing/profiling/#profile-with-pytorch-profiler ref this doc to use, it can not working. #...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
