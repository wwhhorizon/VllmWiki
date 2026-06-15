# vllm-project/vllm#16029: [Feature]: Adding tool_choice: required for lm-format-enforcer

| 字段 | 值 |
| --- | --- |
| Issue | [#16029](https://github.com/vllm-project/vllm/issues/16029) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Adding tool_choice: required for lm-format-enforcer

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Continuetion of #13002 I understand outlines is by default used; but complicated and advanced applications usually go with the lm-format-enforcer. It's not only better, but also supports much more than outlines in terms of schemas. Unfortunately I cannot be using pydantic with LLM cause there is no fix here and I get: `tool_choice` must either be a named tool, "auto", or "none"` I would appreciate a fix or a workaround that make it work with lm-format-enforcer. Also I don't know why but lm-format-enforcer seems to be a better option for guided decoding. ### Alternatives None ### Additional context [Pydantic Side of Issue ](https://github.com/pydantic/pydantic-ai/issues/224) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Adding tool_choice: required for lm-format-enforcer feature request;stale ### 🚀 The feature, motivation and pitch Continuetion of #13002 I understand outlines is by default used; but complicated and advanced...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ol_choice` must either be a named tool, "auto", or "none"` I would appreciate a fix or a workaround that make it work with lm-format-enforcer. Also I don't know why but lm-format-enforcer seems to be a better option for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 24) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Adding tool_choice: required for lm-format-enforcer feature request;stale ### 🚀 The feature, motivation and pitch Continuetion of #13002 I understand outlines is by default used; but complicated and advanced...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
