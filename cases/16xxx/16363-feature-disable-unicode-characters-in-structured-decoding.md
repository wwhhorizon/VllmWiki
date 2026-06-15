# vllm-project/vllm#16363: [Feature]: Disable unicode characters in structured decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#16363](https://github.com/vllm-project/vllm/issues/16363) |
| 状态 | closed |
| 标签 | feature request;structured-output;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Disable unicode characters in structured decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, the xgrammar backend will often return lots of messy unicode characters that are hard to parse and deal with. It requires a lot of custom code to parse these out (with best efforts, as some are not even valid). ### Alternatives Opening this issue in the `xgrammar` repo, or create a custom unicode parser. ### Additional context From the [documentation](https://xgrammar.mlc.ai/docs/api/python/index.html#xgrammar.VocabType) it appears that this issue only arises for certain tokenizer types. It would be nice if it offered consistent behavior across models. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Disable unicode characters in structured decoding feature request;structured-output;stale ### 🚀 The feature, motivation and pitch Currently, the xgrammar backend will often return lots of messy unicode charac...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: t;stale ### 🚀 The feature, motivation and pitch Currently, the xgrammar backend will often return lots of messy unicode characters that are hard to parse and deal with. It requires a lot of custom code to parse these ou...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ls. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: kenizer types. It would be nice if it offered consistent behavior across models. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
