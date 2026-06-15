# vllm-project/vllm#24678: [Performance]: ROPE + KV-Cache-Write + pre-attn prepare-ops fusion

| 字段 | 值 |
| --- | --- |
| Issue | [#24678](https://github.com/vllm-project/vllm/issues/24678) |
| 状态 | open |
| 标签 | performance;keep-open |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;gemm_linear;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;operator;quantization;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Performance]: ROPE + KV-Cache-Write + pre-attn prepare-ops fusion

### Issue 正文摘录

### Proposal to improve performance Performance analysis of DeepSeekR1 and GPTOSS showed that there is non-trivial amount of overheads in the operations that come before the Attention kernel. Specifically, these are ROPE + KV-Cache-Write + attn elementwise/copy prepare ops (and sometimes small matrix multiplies for MLA). Here is a concrete breakdown for DeepSeekR1-FP8 batch-size 32 on 8xB200 GPUs: Before the attention kernel call (fmha::kernel), we can see 4 triton ops (ROPE), then cache_and_concat_mla, and then a torch BMM (matrix_multiply - K-Proj) followed by a bunch of elementwise and copy. The total time these ops take is about the same as the whole attention kernel, so we propose to fuse all of them to reduce HBM traffic bandwidth, since these ops are memory-bandwidth by their nature. A similar fusion is needed for GPTOSS as well, here a breakdown: This one is a bit simpler, since the attention kernel does not expose elementwise ops (or matmul) like in DeepSeekR1 model above. However, there is still the series of triton ops (ROPE) followed by reshape_and_cache_kernel. NVIDIA has a fused ROPE+KV-Cache-write+attn prepare ops kernel in TRT (@pavanimajety is part of the related...

## 现有链接修复摘要

#24914 [torch.compile] Make Query Quantization Fusable | #25774 Fuse RoPE and MLA KV-cache write | #25954 [Performance] Split FlashAttn attention and cache update

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: matrix multiplies for MLA). Here is a concrete breakdown for DeepSeekR1-FP8 batch-size 32 on 8xB200 GPUs: Before the attention kernel call (fmha::kernel), we can see 4 triton ops (ROPE), then cache_and_concat_mla, and t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: of overheads in the operations that come before the Attention kernel. Specifically, these are ROPE + KV-Cache-Write + attn elementwise/copy prepare ops (and sometimes small matrix multiplies for MLA). Here is a concrete...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ROPE + KV-Cache-Write + attn elementwise/copy prepare ops (and sometimes small matrix multiplies for MLA). Here is a concrete breakdown for DeepSeekR1-FP8 batch-size 32 on 8xB200 GPUs: Before the attention kernel call (...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: GPUs: Before the attention kernel call (fmha::kernel), we can see 4 triton ops (ROPE), then cache_and_concat_mla, and then a torch BMM (matrix_multiply - K-Proj) followed by a bunch of elementwise and copy. The total ti...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ? Can we do static per-tensor, dynamic per-token, and dynamic per-group (block quant)? 3. [@Lucas Wilkinson](https://vllm-dev.slack.com/team/U07QLKR3146) and @ProExpertProg talked about how to expose the cache and quant...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24914](https://github.com/vllm-project/vllm/pull/24914) | mentioned | 0.45 | [torch.compile] Make Query Quantization Fusable | tside unified attention.~ this is now handled in the attention layer: #24914. this won't change the semantic meaning of unified_attention as much because we're just changing the d… |
| [#25774](https://github.com/vllm-project/vllm/pull/25774) | mentioned | 0.45 | Fuse RoPE and MLA KV-cache write | -project/vllm/pull/25954) - add `concat_cache_mla_rope` cuda kernel: [#25774](https://github.com/vllm-project/vllm/pull/25774) performance keep-open |
| [#25954](https://github.com/vllm-project/vllm/pull/25954) | mentioned | 0.45 | [Performance] Split FlashAttn attention and cache update | roject/vllm/pull/25103) - separate kvcache from `unified_attention`: [#25954](https://github.com/vllm-project/vllm/pull/25954) - add `concat_cache_mla_rope` cuda kernel: [#25774](… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
