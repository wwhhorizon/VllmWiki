# vllm-project/vllm#21570: [Bug]: [P/D] in nixl_connector, the P node implements a request timeout but the D node cannot detect.

| 字段 | 值 |
| --- | --- |
| Issue | [#21570](https://github.com/vllm-project/vllm/issues/21570) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [P/D] in nixl_connector, the P node implements a request timeout but the D node cannot detect.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When there are numerous requests, the D node accumulates them. The P node releases the kv blocks due to the timeout mechanism, and the D node retrieves the already released kv blocks, leading to abnormal precision. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ulates them. The P node releases the kv blocks due to the timeout mechanism, and the D node retrieves the already released kv blocks, leading to abnormal precision. ### Before submitting a new issue... - [x] Make sure y...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: [P/D] in nixl_connector, the P node implements a request timeout but the D node cannot detect. bug;stale ### Your current environment ### 🐛 Describe the bug When there are numerous requests, the D node accumulate...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: the D node retrieves the already released kv blocks, leading to abnormal precision. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bott...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: D node retrieves the already released kv blocks, leading to abnormal precision. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom r...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: merous requests, the D node accumulates them. The P node releases the kv blocks due to the timeout mechanism, and the D node retrieves the already released kv blocks, leading to abnormal precision. ### Before submitting...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
