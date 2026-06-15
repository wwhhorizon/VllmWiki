# vllm-project/vllm#14532: [Feature]: [V1] Validate / Fix Load Formats on V1

| 字段 | 值 |
| --- | --- |
| Issue | [#14532](https://github.com/vllm-project/vllm/issues/14532) |
| 状态 | closed |
| 标签 | good first issue;feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: [V1] Validate / Fix Load Formats on V1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We are not sure if `--load-format sharded_state` of `--load-format tensorizer` work with V1 This issue asks to look into it and fix any issues that occur, including for TP>1 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eature]: [V1] Validate / Fix Load Formats on V1 good first issue;feature request;stale ### 🚀 The feature, motivation and pitch We are not sure if `--load-format sharded_state` of `--load-format tensorizer` work with V1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: [V1] Validate / Fix Load Formats on V1 good first issue;feature request;stale ### 🚀 The feature, motivation and pitch We are not sure if `--load-format sharded_state` of `--load-format tensorizer` work with V...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
