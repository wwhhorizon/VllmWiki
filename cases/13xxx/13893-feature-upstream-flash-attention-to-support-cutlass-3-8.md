# vllm-project/vllm#13893: [Feature]: Upstream flash attention to support cutlass 3.8

| 字段 | 值 |
| --- | --- |
| Issue | [#13893](https://github.com/vllm-project/vllm/issues/13893) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Upstream flash attention to support cutlass 3.8

### Issue 正文摘录

### 🚀 The feature, motivation and pitch flash attention was changed in the last weeks to support blackwell and new versions of cuda ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tion and pitch flash attention was changed in the last weeks to support blackwell and new versions of cuda ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] M...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Upstream flash attention to support cutlass 3.8 feature request;stale ### 🚀 The feature, motivation and pitch flash attention was changed in the last weeks to support blackwell and new versions of cuda ### Al...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Upstream flash attention to support cutlass 3.8 feature request;stale ### 🚀 The feature, motivation and pitch flash attention was changed in the last weeks to support blackwell and new versions of cuda ### Al...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ash attention was changed in the last weeks to support blackwell and new versions of cuda ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you alre...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
