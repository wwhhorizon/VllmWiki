# vllm-project/vllm#4698: [Performance]: benchmarking vllm copy kernel and pytorch index copy

| 字段 | 值 |
| --- | --- |
| Issue | [#4698](https://github.com/vllm-project/vllm/issues/4698) |
| 状态 | closed |
| 标签 | help wanted;performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: benchmarking vllm copy kernel and pytorch index copy

### Issue 正文摘录

### Proposal to improve performance I opened this issue to track a random idea: Currently we have a copy kernel: https://github.com/vllm-project/vllm/blob/e288df0632d5bdde76c20bed8310b46d35b8e5ac/csrc/cache_kernels.cu#L214-L220 Essentially this does the following vector copy: ```python key_cache_view = key_cache.reshape(-1, num_heads * head_size) value_cache_view = value_cache.reshape(-1, num_heads * head_size) key_view = key.reshape(-1, num_heads * head_size) value_view = value.reshape(-1, num_heads * head_size) key_cache_view[slot_mapping] = key_view value_cache_view[slot_mapping] = value_view ``` The caveat is, we have a special value in `slot_mapping`: `-1` means skip copying. If possible, we can reserve a slot in block manager for padded kv, then we can just use pytorch's index copying, without maintaining a separate copy kernel ourselves. Two TODOs: - [ ] What is the overhead of reserving a slot for padded kv in the block manager? - [ ] Does PyTorch copy kernel outperform the current hand-written one? cc @cadedaniel who knows a lot about block manager, and @WoosukKwon who knows a lot about cuda kernels. ### Report of performance regression _No response_ ### Misc discussion o...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: value_view = value.reshape(-1, num_heads * head_size) key_cache_view[slot_mapping] = key_view value_cache_view[slot_mapping] = value_view ``` The caveat is, we have a special value in `slot_mapping`: `-1` means skip cop...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e_cache_view[slot_mapping] = value_view ``` The caveat is, we have a special value in `slot_mapping`: `-1` means skip copying. If possible, we can reserve a slot in block manager for padded kv, then we can just use pyto...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: hmarking vllm copy kernel and pytorch index copy help wanted;performance;stale ### Proposal to improve performance I opened this issue to track a random idea: Currently we have a copy kernel: https://github.com/vllm-pro...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Performance]: benchmarking vllm copy kernel and pytorch index copy help wanted;performance;stale ### Proposal to improve performance I opened this issue to track a random idea: Currently we have a copy kernel: https://...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: o knows a lot about block manager, and @WoosukKwon who knows a lot about cuda kernels. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
