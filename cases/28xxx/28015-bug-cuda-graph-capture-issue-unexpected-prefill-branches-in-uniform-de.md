# vllm-project/vllm#28015: [bug]: CUDA Graph Capture Issue: Unexpected Prefill Branches in Uniform Decode Graphs

| 字段 | 值 |
| --- | --- |
| Issue | [#28015](https://github.com/vllm-project/vllm/issues/28015) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | attention;cuda |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [bug]: CUDA Graph Capture Issue: Unexpected Prefill Branches in Uniform Decode Graphs

### Issue 正文摘录

# CUDA Graph Capture Issue: Unexpected Prefill Branches in Uniform Decode Graphs **Labels**: `bug`, `cuda-graphs`, `mla`, `attention-backend`, 'mtp=2' ## Summary When capturing uniform decode CUDA graphs for MLA backends with `QueryLenSupport.UNIFORM` (e.g., `ROCM_AITER_MLA`, `FLASHINFER_MLA`, `FLASHMLA`), if `uniform_decode_query_len > 1` (e.g., `q_len=3` in speculative decoding scenarios) and `num_tokens` is not divisible by `uniform_decode_query_len`, padding during capture causes requests with different query lengths to be incorrectly classified as prefill, leading to unexpected prefill branches in the captured uniform decode full graph. ## Environment - **Affected Backends**: All MLA backends with `QueryLenSupport.UNIFORM` - `ROCM_AITER_MLA` (`query_len_support = QueryLenSupport.UNIFORM`) - `FLASHINFER_MLA` (`query_len_support = QueryLenSupport.UNIFORM`) - `FLASHMLA` (`query_len_support = QueryLenSupport.UNIFORM`) - **Affected Modes**: CUDA Graph capture with uniform decode batches (e.g., MTP=2, q_len=3) ## Problem Description When using MLA attention backend with CUDA graph capture enabled, if `uniform_decode_query_len > 1` (e.g., `q_len=3` in speculative decoding scenarios)...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [bug]: CUDA Graph Capture Issue: Unexpected Prefill Branches in Uniform Decode Graphs performance # CUDA Graph Capture Issue: Unexpected Prefill Branches in Uniform Decode Graphs **Labels**: `bug`, `cuda-graphs`, `mla`,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: iform Decode Graphs **Labels**: `bug`, `cuda-graphs`, `mla`, `attention-backend`, 'mtp=2' ## Summary When capturing uniform decode CUDA graphs for MLA backends with `QueryLenSupport.UNIFORM` (e.g., `ROCM_AITER_MLA`, `FL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: y lengths. ### 2. Issue in MLA Attention Metadata Construction In the `build` method in `vllm/v1/attention/backends/mla/common.py`: ```python num_decodes, num_prefills, num_decode_tokens, num_prefill_tokens = ( split_de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [bug]: CUDA Graph Capture Issue: Unexpected Prefill Branches in Uniform Decode Graphs performance # CUDA Graph Capture Issue: Unexpected Prefill Branches in Uniform Decode Graphs **Labels**: `bug`, `cuda-graphs`, `mla`,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: quests (6 tokens, padded to 8) - Graph execution tries to access prefill metadata/branches ## Root Cause Analysis ### 1. Issue in Capture Phase (`_dummy_run`) In the `_dummy_run` method in `vllm/v1/worker/gpu_model_runn...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
