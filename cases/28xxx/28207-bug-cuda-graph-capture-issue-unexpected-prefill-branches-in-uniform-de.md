# vllm-project/vllm#28207: [Bug]: CUDA Graph Capture Issue: Unexpected Prefill Branches in Uniform Decode Graphs when MTP=2

| 字段 | 值 |
| --- | --- |
| Issue | [#28207](https://github.com/vllm-project/vllm/issues/28207) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8 |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA Graph Capture Issue: Unexpected Prefill Branches in Uniform Decode Graphs when MTP=2

### Issue 正文摘录

# CUDA Graph Capture Issue: Unexpected Prefill Branches in Uniform Decode Graphs when mtp=2 **Labels**: `bug`, `cuda-graphs`, `mla`, `attention-backend`, `Mtp=2` ## Summary When capturing uniform decode CUDA graphs for MLA backends with `QueryLenSupport.UNIFORM` (e.g., `ROCM_AITER_MLA`, `FLASHINFER_MLA`, `FLASHMLA`), if `uniform_decode_query_len > 1` (e.g., `q_len=3` with mtp=2) and `num_tokens` is not divisible by `uniform_decode_query_len`, padding during capture causes requests with different query lengths to be incorrectly classified as prefill, leading to unexpected prefill branches in the captured uniform decode full graph. ## Environment ### Affected Scenarios - **Affected Backends**: All MLA backends with `QueryLenSupport.UNIFORM` - `FLASHINFER_MLA` (`query_len_support = QueryLenSupport.UNIFORM`) - `FLASHMLA` (`query_len_support = QueryLenSupport.UNIFORM`) - `ROCM_AITER_MLA` (`query_len_support = QueryLenSupport.UNIFORM`) – Currently not merged - **Affected Modes**: CUDA Graph capture with uniform decode batches (e.g., MTP=2, q_len=3) ### server ```bash MODEL=deepseek-ai/DeepSeek-R1 VLLM_ATTENTION_BACKEND="FLASHINFER_MLA" \ VLLM_USE_V1=1 \ vllm serve $MODEL \ --tensor-para...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: CUDA Graph Capture Issue: Unexpected Prefill Branches in Uniform Decode Graphs when MTP=2 bug;stale # CUDA Graph Capture Issue: Unexpected Prefill Branches in Uniform Decode Graphs when mtp=2 **Labels**: `bug`, `...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: fig '{"cudagraph_mode": "FULL_AND_PIECEWISE"}' \ --trust-remote-code \ --block-size 64 \ --kv-cache-dtype fp8 \ --speculative-config='{"method": "deepseek_mtp", "num_speculative_tokens": 2}' ``` ### client ```bash MODEL...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: e Graphs when mtp=2 **Labels**: `bug`, `cuda-graphs`, `mla`, `attention-backend`, `Mtp=2` ## Summary When capturing uniform decode CUDA graphs for MLA backends with `QueryLenSupport.UNIFORM` (e.g., `ROCM_AITER_MLA`, `FL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: y lengths. ### 2. Issue in MLA Attention Metadata Construction In the `build` method in `vllm/v1/attention/backends/mla/common.py`: ```python num_decodes, num_prefills, num_decode_tokens, num_prefill_tokens = ( split_de...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: LL_AND_PIECEWISE"}' \ --trust-remote-code \ --block-size 64 \ --kv-cache-dtype fp8 \ --speculative-config='{"method": "deepseek_mtp", "num_speculative_tokens": 2}' ``` ### client ```bash MODEL=deepseek-ai/DeepSeek-R1 lm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
