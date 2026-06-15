# vllm-project/vllm#1925: Question regarding vllm's lack of KV cache clearing?

| 字段 | 值 |
| --- | --- |
| Issue | [#1925](https://github.com/vllm-project/vllm/issues/1925) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cache;cuda;kernel |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Question regarding vllm's lack of KV cache clearing?

### Issue 正文摘录

Hello everybody, During my development of candle-vllm and before my recent work developing PagedAttention, I added some methods to clear the KV cache (deallocating the old tensors) of the models between requests. This is because I noticed a shape error occurs if the same model was run with a KV cache from an old inference cycle (even with the same prompt). Is this a recognized error, or perhaps a bug with the old KV cache implementation for the Llama-2 model? I have not run my implementation (although it is based on the vllm implementation), and am not sure if this cache-clearing is still necessary. I use the vllm CUDA kernels as well as basing my implementation on vllm as closely as the language and framework difference allows. I cannot seem to find any explicit cache clearing happening between inference request, but deallocating the cache would induce a dramatic performance overhead and defeat the point of PagedAttention, so I think that this is probably not being done? @WoosukKwon, could you please clarify why vllm does not need to clear the cache - is it a bug with my old KV cache implementation, or does it have to do with vllm's batching or something else? Thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: some methods to clear the KV cache (deallocating the old tensors) of the models between requests. This is because I noticed a shape error occurs if the same model was run with a KV cache from an old inference cycle (eve...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: anguage and framework difference allows. I cannot seem to find any explicit cache clearing happening between inference request, but deallocating the cache would induce a dramatic performance overhead and defeat the poin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nd am not sure if this cache-clearing is still necessary. I use the vllm CUDA kernels as well as basing my implementation on vllm as closely as the language and framework difference allows. I cannot seem to find any exp...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Question regarding vllm's lack of KV cache clearing? Hello everybody, During my development of candle-vllm and before my recent work developing PagedAttention, I added some methods to clear the KV cache (deallocating th...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: implementation, or does it have to do with vllm's batching or something else? Thanks! performance attention_kv_cache;frontend_api;model_support attention;cache;cuda;kernel shape Hello everybody,

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
