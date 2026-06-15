# vllm-project/vllm#30262: [Bug]: The find_matches function took 15 seconds to process 175 images in a single request.

| 字段 | 值 |
| --- | --- |
| Issue | [#30262](https://github.com/vllm-project/vllm/issues/30262) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The find_matches function took 15 seconds to process 175 images in a single request.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The internal loop of find_matches has exceeded 20,000 iterations. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: find_matches function took 15 seconds to process 175 images in a single request. bug;stale ### Your current environment ### 🐛 Describe the bug The internal loop of find_matches has exceeded 20,000 iterations. ### Before...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ns. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
