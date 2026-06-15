# vllm-project/vllm#15275: [Bug]: int8 2:4 sparse time more than fp8

| 字段 | 值 |
| --- | --- |
| Issue | [#15275](https://github.com/vllm-project/vllm/issues/15275) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: int8 2:4 sparse time more than fp8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: int8 2:4 sparse time more than fp8 bug ### Your current environment ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot livi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
