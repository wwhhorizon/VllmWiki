# vllm-project/vllm#17023: [Bug]: The shape of the kv cache in the FlashAttention component of the LLM model in Qwen2.5 is very strange.

| 字段 | 值 |
| --- | --- |
| Issue | [#17023](https://github.com/vllm-project/vllm/issues/17023) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;model_support |
| 子分类 | shape_align |
| Operator 关键词 | attention;cache;cuda;operator |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The shape of the kv cache in the FlashAttention component of the LLM model in Qwen2.5 is very strange.

### Issue 正文摘录

### Your current environment - vllm version:0.7.2 - transformers version:4.52.0.dev - model: qwen2.5 vl ### 🐛 Describe the bug I'm trying to debug and align the output accuracy of Qwen2.5vl with that of Hugging Face Transformers, but I found that the shape of the kv cache in FlashAttention of the LLM part (Qwen2) is very strange. In the torch.ops._vllm_fa2_C.fwd_kvcache function call, the k_cache and v_cache have a shape of torch.Size([1591, 16, 4, 128]). I'm confused about the first dimension of 1591, which I think should represent the sequence length. However, in Transformers, the sequence length is 1662, which seems more reasonable. For reference, I printed the `forward_context.attn_metadata` of this layer as follows: ``` FlashAttentionMetadata(num_prefills=0, num_prefill_tokens=0, num_decode_tokens=1, slot_mapping=tensor([1661], device='cuda:0'), multi_modal_placeholder_index_maps={}, enable_kv_scales_calculation=True, seq_lens=[1662], seq_lens_tensor=tensor([1662], device='cuda:0', dtype=torch.int32), max_prefill_seq_len=0, max_decode_seq_len=1662, context_lens_tensor=tensor([1661], device='cuda:0', dtype=torch.int32), block_tables=tensor([[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: ems more reasonable. For reference, I printed the `forward_context.attn_metadata` of this layer as follows: ``` FlashAttentionMetadata(num_prefills=0, num_prefill_tokens=0, num_decode_tokens=1, slot_mapping=tensor([1661...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: lashAttention component of the LLM model in Qwen2.5 is very strange. bug;stale ### Your current environment - vllm version:0.7.2 - transformers version:4.52.0.dev - model: qwen2.5 vl ### 🐛 Describe the bug I'm trying to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Qwen2.5 is very strange. bug;stale ### Your current environment - vllm version:0.7.2 - transformers version:4.52.0.dev - model: qwen2.5 vl ### 🐛 Describe the bug I'm trying to debug and align the output accuracy of Qwen...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 661], device='cuda:0'), multi_modal_placeholder_index_maps={}, enable_kv_scales_calculation=True, seq_lens=[1662], seq_lens_tensor=tensor([1662], device='cuda:0', dtype=torch.int32), max_prefill_seq_len=0, max_decode_se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: efill_tokens=0, num_decode_tokens=1, slot_mapping=tensor([1661], device='cuda:0'), multi_modal_placeholder_index_maps={}, enable_kv_scales_calculation=True, seq_lens=[1662], seq_lens_tensor=tensor([1662], device='cuda:0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
