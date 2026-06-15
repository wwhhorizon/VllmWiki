# vllm-project/vllm#14088: [Feature][Frontend]: Deprecate `--enable-reasoning`

| 字段 | 值 |
| --- | --- |
| Issue | [#14088](https://github.com/vllm-project/vllm/issues/14088) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Frontend]: Deprecate `--enable-reasoning`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch > If `--reasoning-parser` is required when `--enable-reasoning` is set, why don't we just remove `--enable-reasoning`? We can assume the user wants to enable reasoning content by their specification of `--reasoning-parser` from https://github.com/vllm-project/vllm/pull/12955#discussion_r1976088726 We could deprecate it. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: g`? We can assume the user wants to enable reasoning content by their specification of `--reasoning-parser` from https://github.com/vllm-project/vllm/pull/12955#discussion_r1976088726 We could deprecate it. ### Alternat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature][Frontend]: Deprecate `--enable-reasoning` feature request ### 🚀 The feature, motivation and pitch > If `--reasoning-parser` is required when `--enable-reasoning` is set, why don't we just remove `--enable-reas...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
