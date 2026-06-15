# vllm-project/vllm#35574: [Bug]: Qwen3.5 Can not close thinking by "enable_thinking": false

| 字段 | 值 |
| --- | --- |
| Issue | [#35574](https://github.com/vllm-project/vllm/issues/35574) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 Can not close thinking by "enable_thinking": false

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Adding "chat_template_kwargs": {"enable_thinking": false} to the HTTP body does not disable the thinking process. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ss. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: Qwen3.5 Can not close thinking by "enable_thinking": false bug ### Your current environment ### 🐛 Describe the bug Adding "chat_template_kwargs": {"enable_thinking": false} to the HTTP body does not disable the t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Qwen3.5 Can not close thinking by "enable_thinking": false bug ### Your current environment ### 🐛 Describe the bug Adding "chat_template_kwargs": {"enable_thinking": false} to the HTTP body does not disable the t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
