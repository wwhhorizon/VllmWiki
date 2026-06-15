# vllm-project/vllm#10630: [Bug]: GPU memory leak when using bad_words feature

| 字段 | 值 |
| --- | --- |
| Issue | [#10630](https://github.com/vllm-project/vllm/issues/10630) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GPU memory leak when using bad_words feature

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I attempt to use the newly added bad_words blocking feature, I encounter a GPU memory leak problem. Specifically, the memory consumption keeps increasing on GPU:0 while that of the others remains stable until an Out of Memory (OOM) error occurs. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: GPU memory leak when using bad_words feature bug;stale ### Your current environment ### 🐛 Describe the bug When I attempt to use the newly added bad_words blocking feature, I encounter a GPU memory leak problem....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ed bad_words blocking feature, I encounter a GPU memory leak problem. Specifically, the memory consumption keeps increasing on GPU:0 while that of the others remains stable until an Out of Memory (OOM) error occurs. ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ### 🐛 Describe the bug When I attempt to use the newly added bad_words blocking feature, I encounter a GPU memory leak problem. Specifically, the memory consumption keeps increasing on GPU:0 while that of the others rem...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: GPU memory leak when using bad_words feature bug;stale ### Your current environment ### 🐛 Describe the bug When I attempt to use the newly added bad_words blocking feature, I encounter a GPU memory leak problem....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
