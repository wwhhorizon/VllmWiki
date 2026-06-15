# vllm-project/vllm#33980: [RFC]: Sparse attention KV cache offloading to support longer sequence length

| 字段 | 值 |
| --- | --- |
| Issue | [#33980](https://github.com/vllm-project/vllm/issues/33980) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;kernel;sampling |
| 症状 |  |
| 根因提示 | memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Sparse attention KV cache offloading to support longer sequence length

### Issue 正文摘录

## Motivation. In long sequence inference scenario, KV cache size has become one of the inference bottlenecks. To save GPU memory usage of KV cache and support longer sequence length, we have proposed a layerwise KV cache offloading approach in RFC ([#33398](https://github.com/vllm-project/vllm/issues/33398)). However, during development we find out that the available offload layer number is limited by the loading speed: Based on a rough estimation, the loading time is $\frac{kv\\_cache\\_size}{bandwidth\\_dram2hbm}$, and since decoding is memory bound, the computing time can be approximated to $\frac{kv\\_cache\\_size}{bandwidth\\_hbm2cuda\\_core}$. So the ratio of $\frac{loading\\_time}{computing\\_time}$ should be approximated to $\frac{bandwidth\\_hbm2cuda\\_core}{bandwidth\\_dram2hbm}$, which is about 10x, matches [a test result](https://github.com/vllm-project/vllm/issues/33398#issuecomment-3831107982) based on llama-3.1-8B & NVIDIA H100. Thus the available offload layer number is limited to a lower range ( ## Proposed Change. ### KV cache management We plan to use a `topk_kv_buffer` on GPU with a fixed size of topk tokens to store the needed topk KV cache. In each step, we...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: s to store the needed topk KV cache. In each step, we first allocate GPU blocks for new scheduled tokens and store new computed KV in GPU blocks (a), this is because we still need original GPU blocks to offload or trans...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ng time can be approximated to $\frac{kv\\_cache\\_size}{bandwidth\\_hbm2cuda\\_core}$. So the ratio of $\frac{loading\\_time}{computing\\_time}$ should be approximated to $\frac{bandwidth\\_hbm2cuda\\_core}{bandwidth\\...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [RFC]: Sparse attention KV cache offloading to support longer sequence length RFC ## Motivation. In long sequence inference scenario, KV cache size has become one of the inference bottlenecks. To save GPU memory usage o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: needs offloading, since we may need to free some blocks before the whole request is freed. As for the k_cache needed by indexer, currently we plan to keep it on device so it can still use the original `FullAttentionMana...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: hub.com/vllm-project/vllm/issues/33398#issuecomment-3831107982) based on llama-3.1-8B & NVIDIA H100. Thus the available offload layer number is limited to a lower range ( ## Proposed Change. ### KV cache management We p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
