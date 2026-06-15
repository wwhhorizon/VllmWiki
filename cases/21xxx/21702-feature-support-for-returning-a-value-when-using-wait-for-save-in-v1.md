# vllm-project/vllm#21702: [Feature]: Support for returning a value when using wait_for_save in v1

| 字段 | 值 |
| --- | --- |
| Issue | [#21702](https://github.com/vllm-project/vllm/issues/21702) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for returning a value when using wait_for_save in v1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Motivation When attempting to use the v1 connector, communication issues between the scheduler and worker sides can be observed. Specifically, the scheduler-side connector struggles to detect which blocks the worker-side connector has successfully saved. We noticed that finished_sending defined in ModelRunnerOutput retrieve requests that have already sent the KV cache, but it is difficult to perceive whether there are blocks that can be successfully dumped. Currently, there is no common method to achieve this purpose. ### Proposed Change By adding new features in the Request and ModelRunnerOutput structures and returning the corresponding features through the wait_for_save function, we can achieve this purpose. ### Code https://github.com/flesher0813/vllm/commit/64a94cbdbc38df6f046379c59ac893545ddbd407 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e]: Support for returning a value when using wait_for_save in v1 feature request;stale ### 🚀 The feature, motivation and pitch ### Motivation When attempting to use the v1 connector, communication issues between the sch...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: cation issues between the scheduler and worker sides can be observed. Specifically, the scheduler-side connector struggles to detect which blocks the worker-side connector has successfully saved. We noticed that finishe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: efined in ModelRunnerOutput retrieve requests that have already sent the KV cache, but it is difficult to perceive whether there are blocks that can be successfully dumped. Currently, there is no common method to achiev...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ed. Specifically, the scheduler-side connector struggles to detect which blocks the worker-side connector has successfully saved. We noticed that finished_sending defined in ModelRunnerOutput retrieve requests that have...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
