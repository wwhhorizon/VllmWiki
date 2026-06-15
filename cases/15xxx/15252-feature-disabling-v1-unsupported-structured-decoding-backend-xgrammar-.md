# vllm-project/vllm#15252: [Feature]: Disabling V1: unsupported structured decoding backend - xgrammar:disable-any-whitespace

| 字段 | 值 |
| --- | --- |
| Issue | [#15252](https://github.com/vllm-project/vllm/issues/15252) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Disabling V1: unsupported structured decoding backend - xgrammar:disable-any-whitespace

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The current v1 engine only supports the `xgrammar` backend, but not configurations like `disable-any-whitespace`. The `_validate_structure_output` function raises an error in such cases on this [line](https://github.com/vllm-project/vllm/blob/d8e82bc06d96e9f8f1235926ba9674a14b2bfe31/vllm/v1/engine/processor.py#L130). Happy to open a small PR if it's as simple as accepting `xgrammar` backends with such configs. I haven't done a deep dive to determine if it's something more complex than that. ### Alternatives Creating/using a custom fork. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 926ba9674a14b2bfe31/vllm/v1/engine/processor.py#L130). Happy to open a small PR if it's as simple as accepting `xgrammar` backends with such configs. I haven't done a deep dive to determine if it's something more comple...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Disabling V1: unsupported structured decoding backend - xgrammar:disable-any-whitespace feature request ### 🚀 The feature, motivation and pitch The current v1 engine only supports the `xgrammar` backend, but...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tch The current v1 engine only supports the `xgrammar` backend, but not configurations like `disable-any-whitespace`. The `_validate_structure_output` function raises an error in such cases on this [line](https://github...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ed structured decoding backend - xgrammar:disable-any-whitespace feature request ### 🚀 The feature, motivation and pitch The current v1 engine only supports the `xgrammar` backend, but not configurations like `disable-a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
