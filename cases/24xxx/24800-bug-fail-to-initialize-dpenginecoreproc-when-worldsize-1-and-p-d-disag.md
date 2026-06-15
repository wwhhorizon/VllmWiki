# vllm-project/vllm#24800: [Bug]: Fail to initialize DPEngineCoreProc when worldsize = 1 and P/D disaggregate

| 字段 | 值 |
| --- | --- |
| Issue | [#24800](https://github.com/vllm-project/vllm/issues/24800) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Fail to initialize DPEngineCoreProc when worldsize = 1 and P/D disaggregate

### Issue 正文摘录

### Your current environment VLLM Version: 0.10.2rc2.dev171+g170129eb2.empty Wordsize = 1, TP=1, DP>=1, not related to specific environment ### 🐛 Describe the bug When TP=1, worldsize=1, and DP>=1, vllm v1 defaults to using UniProcExecutor for EngineCore initialization, which results in connector_worker and connector_scheduler being initialized within the same process, leading to errors. This issue can be avoided by forcibly setting --distributed-executor-backend mp . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ize = 1 and P/D disaggregate bug;stale ### Your current environment VLLM Version: 0.10.2rc2.dev171+g170129eb2.empty Wordsize = 1, TP=1, DP>=1, not related to specific environment ### 🐛 Describe the bug When TP=1, worlds...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: initialize DPEngineCoreProc when worldsize = 1 and P/D disaggregate bug;stale ### Your current environment VLLM Version: 0.10.2rc2.dev171+g170129eb2.empty Wordsize = 1, TP=1, DP>=1, not related to specific environment #...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: This issue can be avoided by forcibly setting --distributed-executor-backend mp . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: p . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
