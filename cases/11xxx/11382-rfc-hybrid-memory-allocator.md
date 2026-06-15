# vllm-project/vllm#11382: [RFC]: Hybrid Memory Allocator

| 字段 | 值 |
| --- | --- |
| Issue | [#11382](https://github.com/vllm-project/vllm/issues/11382) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache |
| 症状 | build_error |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Hybrid Memory Allocator

### Issue 正文摘录

### Motivation. In addition to standard self-attention only models, we now having more and more hybrid models with more than one type of layer, for example: 1. Sliding window attention + self attention: Gemma2 Ministral (https://github.com/vllm-project/vllm/issues/9464) 2. Cross attention + self attention: mllama 3. Mamba layer + self attention: Jamba, Bamba The KV cache size of different tokens are no longer the same in the above models. However, vLLM can only allocate the same KV cache size for all tokens, as shown in the below figure (mllama with BLOCK_SIZE=1). The memory waste can be 79.6% in mllama, 25% in Gemma-2, and 56.25% in Ministral. And for mamba layers, vLLM has a special MambaCacheManager in `model_executor/models/mamba_cache.py`, which is not compatible with prefix caching. We want a new memory manager to: 1. Allocate kv cache for these models with minimum fragmentation 2. Support prefix caching for these models We can support them mainly in two milestones: **Milestone 1: per-layer memory allocation, each layer has the same kv cache size per token** In this milestone, we assume that all layers have the same kv_hidden_size but different number of tokens due to differ...

## 现有链接修复摘要

#12655 [WIP] Hybrid allocator for full attention & sliding window attention interleaved models | #20016 Enable V1 for Hybrid SSM/Attention Models

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 6: KV cache size for all tokens, as shown in the below figure (mllama with BLOCK_SIZE=1). The memory waste can be 79.6% in mllama, 25% in Gemma-2, and 56.25% in Ministral. And for mamba layers, vLLM has a special MambaCach...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [RFC]: Hybrid Memory Allocator RFC;stale ### Motivation. In addition to standard self-attention only models, we now having more and more hybrid models with more than one type of layer, for example: 1. Sliding window att...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: r RFC;stale ### Motivation. In addition to standard self-attention only models, we now having more and more hybrid models with more than one type of layer, for example: 1. Sliding window attention + self attention: Gemm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: slots based on layer type, and different slot mapping. The software architecture will be as following, with the memory manager for each layer be one of [SelfAttentionManager, SlidingWindowManager, MambaManager, CrossAtt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Gemma-2, and 56.25% in Ministral. And for mamba layers, vLLM has a special MambaCacheManager in `model_executor/models/mamba_cache.py`, which is not compatible with prefix caching. We want a new memory manager to: 1. Al...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#12655](https://github.com/vllm-project/vllm/pull/12655) | mentioned | 0.6 | [WIP] Hybrid allocator for full attention & sliding window attention interleaved models | vllm:hybrid_allocator This pr is working on hybrid memory allocator (#11382), and does the following things: 1. Extend `KVCacheManger` to support multiple KV cache groups 2. Intro… |
| [#20016](https://github.com/vllm-project/vllm/pull/20016) | mentioned | 0.6 | Enable V1 for Hybrid SSM/Attention Models | models that use both SSM and attention layers. Related RFCs: #18571 #11382 cc @heheda12345 @tlrmchlsmth ## Implementation The current hybrid cache allocator implementation assume |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
