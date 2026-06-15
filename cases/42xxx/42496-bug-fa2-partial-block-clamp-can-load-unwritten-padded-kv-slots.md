# vllm-project/vllm#42496: [Bug]: FA2 partial-block clamp can load unwritten padded KV slots

| 字段 | 值 |
| --- | --- |
| Issue | [#42496](https://github.com/vllm-project/vllm/issues/42496) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: FA2 partial-block clamp can load unwritten padded KV slots

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary I observed a possible robustness or documentation issue in the FlashAttention-2 paged KV partial block path. When the last KV block in an FA2 tile is only partially populated, `resolve_thread_kv_page_slice_offset` clamps extra threads to a fixed in-block row. This avoids reading past the block table, but it can also make those clamped threads physically load KV slots that were not written for the current request. Current outputs appear to remain correct because those padded positions are outside the true sequence length and are masked out before they affect softmax. I found nearby comments documenting the clamp and the last-block mask separately, but I could not find a comment documenting the combined contract: clamped FA2 paged-KV threads may physically load padded/unwritten KV slots, and correctness relies on the `seqlen_k`-derived mask. ## Question for maintainers Is this an expected FA2 implementation detail? In other words, are clamped threads allowed to physically read padded/unwritten slots as long as the `seqlen_k`-derived mask guarantees those positions cannot affect output? If this is intended, I think a shor...

## 现有链接修复摘要

#30887 [Bugfix] [Kernel] Triton attention kernels: mask out V blocks that fall outside sliding window

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: Summary I observed a possible robustness or documentation issue in the FlashAttention-2 paged KV partial block path. When the last KV block in an FA2 tile is only partially populated, `resolve_thread_kv_page_slice_offse...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: rrent implementation appears correct, but I could not find one that explicitly says the clamped paged-KV load may hit padded/unwritten slots inside the final physical block. I also saw the FlexAttention documentation/co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: re masking when K/V length is not a multiple of `kBlockN`, and that some smem tiles do not need clearing because the scores will be masked. - `flash-attention/csrc/flash_attn/src/mask.h` applies `-INFINITY` for position...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: FA2 partial-block clamp can load unwritten padded KV slots bug ### Your current environment ### 🐛 Describe the bug ## Summary I observed a possible robustness or documentation issue in the FlashAttention-2 paged...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: t` can correspond to a padded slot inside the final physical block. The model output was still correct in my tests, which is consistent with FA2's per-position causal/padding mask assigning zero probability to those pad...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#30887](https://github.com/vllm-project/vllm/pull/30887) | mentioned | 0.45 | [Bugfix] [Kernel] Triton attention kernels: mask out V blocks that fall outside sliding window | could make these physical reads observable. a related precedent is pr #30887, where an attention backend failed to fully mask out-of-window v values and those values could affect… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
