# vllm-project/vllm#3264: Automatic Prefix Caching (#2792) might conflict with multi-LoRA (#1804)

| 字段 | 值 |
| --- | --- |
| Issue | [#3264](https://github.com/vllm-project/vllm/issues/3264) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Automatic Prefix Caching (#2792) might conflict with multi-LoRA (#1804)

### Issue 正文摘录

#2762 Provides a great way to improve efficiency when multiple requests share the same prefix through KV-cache reuse. Nevertheless, the user probably does not want to share KV-cache across two different LoRA adapters since the values would most likely be different. As the test cases in PR #3263 suggest, the code changes in #2762 might require a bit more work to distinguish between blocks from different LoRA adapters. Previously, #1804 avoided this conflict by including adapter_id in the tuple while generating hashes for prefixes. ([source](https://github.com/vllm-project/vllm/blob/9b945daaf1ce03b8b02d68b37c59baf28566b535/vllm/prefix.py#L84)). The fix proposed in #3263 drew inspiration from this approach.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nflict with multi-LoRA (#1804) #2762 Provides a great way to improve efficiency when multiple requests share the same prefix through KV-cache reuse. Nevertheless, the user probably does not want to share KV-cache across...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: improve efficiency when multiple requests share the same prefix through KV-cache reuse. Nevertheless, the user probably does not want to share KV-cache across two different LoRA adapters since the values would most like...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: de changes in #2762 might require a bit more work to distinguish between blocks from different LoRA adapters. Previously, #1804 avoided this conflict by including adapter_id in the tuple while generating hashes for pref...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: A (#1804) #2762 Provides a great way to improve efficiency when multiple requests share the same prefix through KV-cache reuse. Nevertheless, the user probably does not want to share KV-cache across two different LoRA a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: LoRA adapters since the values would most likely be different. As the test cases in PR #3263 suggest, the code changes in #2762 might require a bit more work to distinguish between blocks from different LoRA adapters. P...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
