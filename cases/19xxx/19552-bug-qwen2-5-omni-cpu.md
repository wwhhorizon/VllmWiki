# vllm-project/vllm#19552: [Bug]: 使用qwen2.5-omni对音频识别，cpu会被打满。

| 字段 | 值 |
| --- | --- |
| Issue | [#19552](https://github.com/vllm-project/vllm/issues/19552) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 使用qwen2.5-omni对音频识别，cpu会被打满。

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 调用推理服务，发现cpu利用率达到99%。会支持将audio的处理放在gpu里吗？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 里吗？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: 使用qwen2.5-omni对音频识别，cpu会被打满。 bug;stale ### Your current environment ### 🐛 Describe the bug 调用推理服务，发现cpu利用率达到99%。会支持将audio的处理放在gpu里吗？ ### Before submitting a new issue... - [x] Make sure you already searched for r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: 使用qwen2.5-omni对音频识别，cpu会被打满。 bug;stale ### Your current environment ### 🐛 Describe the bug 调用推理服务，发现cpu利用率达到99%。会支持将audio的处理放在gpu里吗？ ### Before submitting a new issue... - [x] Make sure you already searched for r...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
