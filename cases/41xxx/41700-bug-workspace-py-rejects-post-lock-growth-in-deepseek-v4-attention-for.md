# vllm-project/vllm#41700: [Bug]: workspace.py rejects post-lock growth in deepseek_v4_attention._forward_prefill (DSV4 #40991) — patch attached

| 字段 | 值 |
| --- | --- |
| Issue | [#41700](https://github.com/vllm-project/vllm/issues/41700) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | attention;fp8;moe;quantization;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: workspace.py rejects post-lock growth in deepseek_v4_attention._forward_prefill (DSV4 #40991) — patch attached

### Issue 正文摘录

## Summary `vllm/v1/worker/workspace.py:_ensure_workspace_size` locks the per-rank attention workspace at the post-profile size and refuses growth. DeepSeek-V4-Flash's `_forward_prefill` (added in #40991) then fails with an `AssertionError` on real prompts that need slightly more workspace than the dummy profile run sized for. The locked size is structural and not influenced by `--max-num-batched-tokens`, `--max-num-seqs`, or `--gpu-memory-utilization`. The currently published workaround is `--enforce-eager`, which costs ~4× decode throughput. The smoking gun is in the source: `deepseek_v4_attention.py:170-172` carries this comment: ```python # Prefill is processed in fixed-size chunks; this bounds the bf16 kv-gather # workspace allocated at _forward_prefill (and the matching profile-time # reservation in attention_impl's dummy-run branch). PREFILL_CHUNK_SIZE = 4 ``` The "matching profile-time reservation in attention_impl's dummy-run branch" implies a pre-allocation hook was always intended. It just isn't there: the dummy-run path (`attention_impl`, `if not isinstance(attn_metadata, dict)`) returns early without ever calling through to `_forward_prefill`, so warmup never sees pre...

## 现有链接修复摘要

#40991 [DSv4][Nvidia] SM12x DeepSeek V4 support | #41276 [WIP] [DSV4] Quantization Support

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ```python # Prefill is processed in fixed-size chunks; this bounds the bf16 kv-gather # workspace allocated at _forward_prefill (and the matching profile-time # reservation in attention_impl's dummy-run branch). PREFILL...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: n't there: the dummy-run path (`attention_impl`, `if not isinstance(attn_metadata, dict)`) returns early without ever calling through to `_forward_prefill`, so warmup never sees prefill workspace requirements, and `lock...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: workspace.py rejects post-lock growth in deepseek_v4_attention._forward_prefill (DSV4 #40991) — patch attached ## Summary `vllm/v1/worker/workspace.py:_ensure_workspace_size` locks the per-rank attention workspace at th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: wed after locking. ``` The 21.62 MB locked size is identical across two builds 28 vLLM commits apart (only the file line number moved 1454→1457). Real-prompt sizes range 21.80 MB → 24.89 MB. Even when `--max-num-batched...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ob/main/scripts/patch_v4_packed_mapping.py)) - transformers: 5.8.0.dev0 (HF main; PR #45643 add-deepseek-v4 was merged 2026-05-02) - compressed-tensors: 0.15.1.a20260428 - Hardware: 2× NVIDIA DGX Spark GB10 (SM 12.1a, 1...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40991](https://github.com/vllm-project/vllm/pull/40991) | mentioned | 0.45 | [DSv4][Nvidia] SM12x DeepSeek V4 support | ace was never sized" bugs. ## cross-references - dsv4 main vllm pr: #40991 (cc @jasl) - compressed-tensors v4 attention pr: #41276 (cc @kylesayrs) - related workspace allocation f… |
| [#41276](https://github.com/vllm-project/vllm/pull/41276) | mentioned | 0.45 | [WIP] [DSV4] Quantization Support | main vllm pr: #40991 (cc @jasl) - compressed-tensors v4 attention pr: #41276 (cc @kylesayrs) - related workspace allocation failure (different scenario, same `workspace.py`): #407… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
