# vllm-project/vllm#22492: [Bug]: HF_HUB_OFFLINE Parameter does not take effect

| 字段 | 值 |
| --- | --- |
| Issue | [#22492](https://github.com/vllm-project/vllm/issues/22492) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: HF_HUB_OFFLINE Parameter does not take effect

### Issue 正文摘录

### Your current environment The current code directly accesses huggenface, ignoring the HF_HUB_OFFLINE configuration. ### 🐛 Describe the bug The current code directly accesses huggenface, ignoring the HF_HUB_OFFLINE configuration. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: HF_HUB_OFFLINE Parameter does not take effect bug ### Your current environment The current code directly accesses huggenface, ignoring the HF_HUB_OFFLINE configuration. ### 🐛 Describe the bug The current code dir...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
