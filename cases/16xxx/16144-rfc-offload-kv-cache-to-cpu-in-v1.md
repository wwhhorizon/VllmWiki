# vllm-project/vllm#16144: [RFC]: Offload KV cache to CPU in V1

| 字段 | 值 |
| --- | --- |
| Issue | [#16144](https://github.com/vllm-project/vllm/issues/16144) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache |
| 症状 | slowdown |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Offload KV cache to CPU in V1

### Issue 正文摘录

### Motivation. Offloading device KV cache to the CPU can be worthwhile if the transfer overhead outweighs the re-computation, saving precious GPU cycles. This is especially useful in cases such as long, multi-turn conversations. Additionally, hardware improvements such as Nvidia [C2C](https://www.nvidia.com/en-us/data-center/nvlink-c2c/) greatly accelerate CPU-GPU communication, making offloading even more compelling. ### Proposed Change. ## Design The design space for KV cache offloading is broad. As an initial goal, we propose focusing primarily on offloading to the CPU. While we aim to keep the interface and implementation extensible—enabling future support for offloading to other mediums such as disk or remote storage—these are out of scope for this RFC. A key design consideration is determining when to swap KV cache blocks out to the CPU and when to swap them back into the device. For swap-out, the earliest opportunity is immediately after a KV cache block is generated, while the latest is just before it is evicted from the device. For swap-in, the earliest timing can be guided by a prefetching policy, while the latest is just before the next forward() call. In this RFC, we...

## 现有链接修复摘要

#13377 [V1][Core] Support offloading KV cache to CPU.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [RFC]: Offload KV cache to CPU in V1 RFC ### Motivation. Offloading device KV cache to the CPU can be worthwhile if the transfer overhead outweighs the re-computation, saving precious GPU cycles. This is especially usef...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: is RFC. A key design consideration is determining when to swap KV cache blocks out to the CPU and when to swap them back into the device. For swap-out, the earliest opportunity is immediately after a KV cache block is g...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ortunity is immediately after a KV cache block is generated, while the latest is just before it is evicted from the device. For swap-in, the earliest timing can be guided by a prefetching policy, while the latest is jus...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: thwhile if the transfer overhead outweighs the re-computation, saving precious GPU cycles. This is especially useful in cases such as long, multi-turn conversations. Additionally, hardware improvements such as Nvidia [C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: is swap plan becomes part of the scheduler output and is executed by the model runner prior to the model forward. ## Interface The KV cache manager will continue to manage all the metadata with roughly the same API with...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#13377](https://github.com/vllm-project/vllm/pull/13377) | mentioned | 0.45 | [V1][Core] Support offloading KV cache to CPU. | on-mo ### any other things. an initial prototype is implemented in #13377 ### before submitting a new issue... - [x] make sure you already searched for relevant issues, and asked… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
