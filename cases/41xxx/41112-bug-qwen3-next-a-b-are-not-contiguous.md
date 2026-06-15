# vllm-project/vllm#41112: [Bug]: Qwen3_next a/b are not contiguous

| 字段 | 值 |
| --- | --- |
| Issue | [#41112](https://github.com/vllm-project/vllm/issues/41112) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3_next a/b are not contiguous

### Issue 正文摘录

### Your current environment - ### 🐛 Describe the bug after "fix_query_key_value_ordering", **a** and **b** are not contiguous, which later causes the assertion to fail ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ail ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: Qwen3_next a/b are not contiguous bug ### Your current environment - ### 🐛 Describe the bug after "fix_query_key_value_ordering", **a** and **b** are not contiguous, which later causes the assertion to fail ### B...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Qwen3_next a/b are not contiguous bug ### Your current environment - ### 🐛 Describe the bug after "fix_query_key_value_ordering", **a** and **b** are not contiguous, which later causes the assertion to fail ### Be
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
