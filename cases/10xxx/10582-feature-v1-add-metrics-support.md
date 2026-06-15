# vllm-project/vllm#10582: [Feature][v1]: Add metrics support 

| 字段 | 值 |
| --- | --- |
| Issue | [#10582](https://github.com/vllm-project/vllm/issues/10582) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][v1]: Add metrics support 

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We should also be feature parity on metrics with most of available stats if possible. On a high level: 1. [P0] Support system and requests stats logging 2. [P0] Support metric export to prometheus. 3. [P1] Support or deprecate all metrics from V0 4. [P1] Allow users to define their own prometheus client and other arbitrary loggers. 5. [P2] Make it work with tracing too (there's some request level stats that tracing needs, like queue time, ttft). These request level metric should be possible to be surfaced in v1 too. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature][v1]: Add metrics support feature request;stale ### 🚀 The feature, motivation and pitch We should also be feature parity on metrics with most of available stats if possible. On a high level: 1. [P0] Support sys...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: metheus client and other arbitrary loggers. 5. [P2] Make it work with tracing too (there's some request level stats that tracing needs, like queue time, ttft). These request level metric should be possible to be surface...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
