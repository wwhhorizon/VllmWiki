# vllm-project/vllm#40248: [Bug]: High concurrency or enabling eagle3 and streaming + function call can trigger accuracy issues on kimi k2.5

| 字段 | 值 |
| --- | --- |
| Issue | [#40248](https://github.com/vllm-project/vllm/issues/40248) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: High concurrency or enabling eagle3 and streaming + function call can trigger accuracy issues on kimi k2.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In 0.18.0rc1, the function call feature was verified with eagle3. It was found that the content of the start or end identifier of the function call was not returned as the response. As a result, the JSON format was incorrect. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: concurrency or enabling eagle3 and streaming + function call can trigger accuracy issues on kimi k2.5 bug ### Your current environment ### 🐛 Describe the bug In 0.18.0rc1, the function call feature was verified with eag...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: concurrency or enabling eagle3 and streaming + function call can trigger accuracy issues on kimi k2.5 bug ### Your current environment ### 🐛 Describe the bug In 0.18.0rc1, the function call feature was verified with eag...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ct. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: he function call was not returned as the response. As a result, the JSON format was incorrect. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
