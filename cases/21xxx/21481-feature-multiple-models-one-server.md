# vllm-project/vllm#21481: [Feature]: Multiple models one server

| 字段 | 值 |
| --- | --- |
| Issue | [#21481](https://github.com/vllm-project/vllm/issues/21481) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Multiple models one server

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hey Im working on a project and I want to do my on infra inference for small models, I just want one inference server running multiple models to do this though I had to setup my own model management and unloading loading models when appropriate into memory. It would be cool if VLLM had this I would be happy myself to make a PR, if you guys are ok with this. ### Alternatives _No response_ ### Additional context Im on azure container apps where multiple gpu nodes are not supported as far as I know ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Hey Im working on a project and I want to do my on infra inference for small models, I just want one inference server running multiple models to do this though I had to setup my own model management and unloading loadin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Multiple models one server feature request;stale ### 🚀 The feature, motivation and pitch Hey Im working on a project and I want to do my on infra inference for small models, I just want one inference server r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Multiple models one server feature request;stale ### 🚀 The feature, motivation and pitch Hey Im working on a project and I want to do my on infra inference for small models, I just want one inference server r...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
