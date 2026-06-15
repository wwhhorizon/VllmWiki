# vllm-project/vllm#25878: [CI]: Automatically cancel fastcheck when full CI have been triggered

| 字段 | 值 |
| --- | --- |
| Issue | [#25878](https://github.com/vllm-project/vllm/issues/25878) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Automatically cancel fastcheck when full CI have been triggered

### Issue 正文摘录

### 🚀 The feature, motivation and pitch - When a PR is marked ready to trigger full CI, given that fastcheck won't block merge, there is no need to run fastcheck CI with duplicated tests anymore. - Currently, we can only cancel fastcheck manually. It would be better to automatically cancel them when PR is ready. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Automatically cancel fastcheck when full CI have been triggered feature request;stale ### 🚀 The feature, motivation and pitch - When a PR is marked ready to trigger full CI, given that fastcheck won't block merge, there...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI]: Automatically cancel fastcheck when full CI have been triggered feature request;stale ### 🚀 The feature, motivation and pitch - When a PR is marked ready to trigger full CI, given that fastcheck won't block merge,
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: When a PR is marked ready to trigger full CI, given that fastcheck won't block merge, there is no need to run fastcheck CI with duplicated tests anymore. - Currently, we can only cancel fastcheck manually. It would be b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: won't block merge, there is no need to run fastcheck CI with duplicated tests anymore. - Currently, we can only cancel fastcheck manually. It would be better to automatically cancel them when PR is ready. ### Alternativ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
