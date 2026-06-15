# vllm-project/vllm#21604: [Feature]: Support multiple guided decoding settings

| 字段 | 值 |
| --- | --- |
| Issue | [#21604](https://github.com/vllm-project/vllm/issues/21604) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support multiple guided decoding settings

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently `GuidedDecodingParams` only supports one setting. If multiple settings are specified, for example `json` + `grammar`, it would raise: ``` ValueError: You can only use one kind of guided decoding but multiple are specified: ``` It would be super useful if `GuidedDecodingParams` could support multiple guided decoding settings. This way, you could for example use a json schema and at the same time force the grammar to follow a certain format. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support multiple guided decoding settings feature request;stale ### 🚀 The feature, motivation and pitch Currently `GuidedDecodingParams` only supports one setting. If multiple settings are specified, for exam...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: edDecodingParams` only supports one setting. If multiple settings are specified, for example `json` + `grammar`, it would raise: ``` ValueError: You can only use one kind of guided decoding but multiple are specified: `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: a json schema and at the same time force the grammar to follow a certain format. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
