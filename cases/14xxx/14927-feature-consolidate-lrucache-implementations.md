# vllm-project/vllm#14927: [Feature]: Consolidate `LRUCache` implementations

| 字段 | 值 |
| --- | --- |
| Issue | [#14927](https://github.com/vllm-project/vllm/issues/14927) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Consolidate `LRUCache` implementations

### Issue 正文摘录

### 🚀 The feature, motivation and pitch #14805 introduced `cachetools.LRUCache` to support different size for each item and prepare for a thread-safe implementation. On the other hand, the code under `vllm/adapter_commons` uses the existing `vllm.utils.LRUCache`. To clean up the code, we should consolidate these implementations inside `vllm.utils.LRUCache`. This cache should support the following features: - Pinning specific items in the cache (the existing `vllm.utils.LRUCache`) - Custom function to compute the size for each item (`cachetools.LRUCache`) - Custom callback functions when an item is removed (`vllm.adapter_commons.AdapterLRUCache`) - The cache should remain compatible with `collections.abc.MutableMapping` interface so it can be passed to `cachetools.cached` to make it thread-safe. ### Alternatives Keep the two implementations separate. However, this may cause confusion since the two classes share the same name. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: UCache`. This cache should support the following features: - Pinning specific items in the cache (the existing `vllm.utils.LRUCache`) - Custom function to compute the size for each item (`cachetools.LRUCache`) - Custom...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ache`) - The cache should remain compatible with `collections.abc.MutableMapping` interface so it can be passed to `cachetools.cached` to make it thread-safe. ### Alternatives Keep the two implementations separate. Howe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: eature]: Consolidate `LRUCache` implementations good first issue;feature request ### 🚀 The feature, motivation and pitch #14805 introduced `cachetools.LRUCache` to support different size for each item and prepare for a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
