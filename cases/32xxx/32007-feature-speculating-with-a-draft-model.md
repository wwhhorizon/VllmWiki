# vllm-project/vllm#32007: [Feature]: Speculating with a draft model

| 字段 | 值 |
| --- | --- |
| Issue | [#32007](https://github.com/vllm-project/vllm/issues/32007) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Speculating with a draft model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In docs, I found this [Speculating with a draft model](https://docs.vllm.ai/en/latest/features/spec_decode/#speculating-with-a-draft-model) While in codes, I also found this https://github.com/vllm-project/vllm/blob/e2d49ec2a4818186b8bafda43f97c298ff91a35e/vllm/config/speculative.py#L379-L384 I'm really confused about whether vLLM supports speculation with a draft model or not. Thanks for your clarification. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Feature]: Speculating with a draft model feature request;stale ### 🚀 The feature, motivation and pitch In docs, I found this [Speculating with a draft model](https://docs.vllm.ai/en/latest/features/spec_decode/#specula...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Speculating with a draft model feature request;stale ### 🚀 The feature, motivation and pitch In docs, I found this [Speculating with a draft model](https://docs.vllm.ai/en/latest/features/spec_decode/#specula...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: I found this [Speculating with a draft model](https://docs.vllm.ai/en/latest/features/spec_decode/#speculating-with-a-draft-model) While in codes, I also found this https://github.com/vllm-project/vllm/blob/e2d49ec2a481...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
