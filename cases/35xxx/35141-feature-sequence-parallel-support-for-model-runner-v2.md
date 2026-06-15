# vllm-project/vllm#35141: [Feature]: Sequence Parallel Support for Model Runner V2

| 字段 | 值 |
| --- | --- |
| Issue | [#35141](https://github.com/vllm-project/vllm/issues/35141) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Sequence Parallel Support for Model Runner V2

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Sequence Parallel Support for Model Runner V2 Tasks: - [ ] Basic feature https://github.com/vllm-project/vllm/pull/35206 - [ ] PP supprot - [ ] Full cuda graph support ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ps://github.com/vllm-project/vllm/pull/35206 - [ ] PP supprot - [ ] Full cuda graph support ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you al...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Sequence Parallel Support for Model Runner V2 feature request ### 🚀 The feature, motivation and pitch Sequence Parallel Support for Model Runner V2 Tasks: - [ ] Basic feature https://github.com/vllm-project/v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Sequence Parallel Support for Model Runner V2 feature request ### 🚀 The feature, motivation and pitch Sequence Parallel Support for Model Runner V2 Tasks: - [ ] Basic feature https://github.com/vllm-project/v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
