# vllm-project/vllm#7697: [RFC]: Enable Memory Tiering for vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#7697](https://github.com/vllm-project/vllm/issues/7697) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cache;kernel |
| 症状 | slowdown |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Enable Memory Tiering for vLLM

### Issue 正文摘录

### Motivation. Nowadays, many new applications including multi-turn conversations, multi-modality and multi-agent, require a significant amount of KV cache. Such applications generally have a shared prompt for multiple requests, and recomputing them each time can take significant time for prefilling. Suppose the length of shared prompt is $n$, the complexity of recomputation is $O(n^2)$. On the other hand, if the shared prompt is saved on the slower but larger-capacity storage hierarchy (such as DRAM or even Disk), the time to load the prompt KV cache and compute the next token is $O(n)$ (assuming a full hit). So at some point, evicting and reloading the KV cache from storage hierarchy becomes beneficial than recomputing the whole prompt again. Such observation is also found in papers [1], [2] However, the current vLLM rarely uses the secondary storage tier (DRAM). It only swaps out the running sequences when they fail to allocate blocks for the newly generated token which rarely happens for different workloads (what I have tested included sharedGPT, UltraChat, LooGle, Toolbench). When vLLM allocates blocks for prefill sequences, it discards the content of the GPU blocks in the e...

## 现有链接修复摘要

#7910 [Core] Enable Memory Tiering for vLLM | #8694 [Core] Enable Memory Tiering for vLLM | #9682 [Core] Support offloading KV cache to CPU | #10874 [Core] Support offloading KV cache to CPU

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [RFC]: Enable Memory Tiering for vLLM RFC;stale ### Motivation. Nowadays, many new applications including multi-turn conversations, multi-modality and multi-agent, require a significant amount of KV cache. Such applicat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: enerated token which rarely happens for different workloads (what I have tested included sharedGPT, UltraChat, LooGle, Toolbench). When vLLM allocates blocks for prefill sequences, it discards the content of the GPU blo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: the shared prompt is saved on the slower but larger-capacity storage hierarchy (such as DRAM or even Disk), the time to load the prompt KV cache and compute the next token is $O(n)$ (assuming a full hit). So at some poi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: sations, multi-modality and multi-agent, require a significant amount of KV cache. Such applications generally have a shared prompt for multiple requests, and recomputing them each time can take significant time for pre...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: RAM). It only swaps out the running sequences when they fail to allocate blocks for the newly generated token which rarely happens for different workloads (what I have tested included sharedGPT, UltraChat, LooGle, Toolb...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7910](https://github.com/vllm-project/vllm/pull/7910) | mentioned | 0.6 | [Core] Enable Memory Tiering for vLLM | [Core] Enable Memory Tiering for vLLM This is the follow-up PR or #7697 Goal: Enable memory tiering for vLLM where the blocks evicted from HBM will be swapped to DRAM, and further |
| [#8694](https://github.com/vllm-project/vllm/pull/8694) | mentioned | 0.6 | [Core] Enable Memory Tiering for vLLM | [Core] Enable Memory Tiering for vLLM This is the following PR of #7697. This PR introduces 3 major functionalities: 1. Context Caching with TTL support is also a huge drive for me |
| [#9682](https://github.com/vllm-project/vllm/pull/9682) | mentioned | 0.6 | [Core] Support offloading KV cache to CPU | cache to CPU ## A minmal implementation for CPU KV cache offloading (#7697) ## Benchmarking results: A long document QA workload (see google doc for more discriptions). GPU can |
| [#10874](https://github.com/vllm-project/vllm/pull/10874) | mentioned | 0.6 | [Core] Support offloading KV cache to CPU | ing KV cache to CPU ## An implementation for CPU KV cache offloading (#7697) TL; DR: **CPU offloading is better than prefix caching in our benchmark**, we also found that the evic… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
