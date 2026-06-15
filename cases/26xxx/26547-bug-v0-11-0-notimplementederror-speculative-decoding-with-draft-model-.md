# vllm-project/vllm#26547: [Bug]: v0.11.0 NotImplementedError: Speculative decoding with draft model is not supported yet.

| 字段 | 值 |
| --- | --- |
| Issue | [#26547](https://github.com/vllm-project/vllm/issues/26547) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v0.11.0 NotImplementedError: Speculative decoding with draft model is not supported yet.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using the speculative decoding feature in v0.11.0, but I'm getting the following error: ```bash NotImplementedError: Speculative decoding with draft model is not supported yet. Please consider using other speculative decoding methods such as ngram, medusa, eagle, or deepseek_mtp. ``` According to the documentation, v0.10.0 doesn't support the draft model, but there's no mention of support in v0.11.0 either. However, v0.11.0 doesn't support the draft model either. When will speculative decoding support the draft model? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: v0.11.0 NotImplementedError: Speculative decoding with draft model is not supported yet. bug ### Your current environment ### 🐛 Describe the bug I'm using the speculative decoding feature in v0.11.0, but I'm gett...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: el? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: v0.11.0 NotImplementedError: Speculative decoding with draft model is not supported yet. bug ### Your current environment ### 🐛 Describe the bug I'm using the speculative decoding feature in v0.11.0, but I'm gett...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
