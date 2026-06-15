# vllm-project/vllm#36266: [Feature]: Add MLA + Quant support in vLLM (leveraging existing FlashInfer MLA support)

| 字段 | 值 |
| --- | --- |
| Issue | [#36266](https://github.com/vllm-project/vllm/issues/36266) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add MLA + Quant support in vLLM (leveraging existing FlashInfer MLA support)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch MLA + Quant` is currently marked as unsupported. https://github.com/vllm-project/vllm/issues/36066 FlashInfer already appears to provide substantial MLA support, plus several MLA-related quantization building blocks. ## Existing FlashInfer MLA pieces FlashInfer already has the following MLA-related components: - MLA decode wrapper: `flashinfer/decode.py` (`BatchDecodeMlaWithPagedKVCacheWrapper`) - MLA attention wrapper: `flashinfer/mla.py` (`BatchMLAPagedAttentionWrapper`) - `trtllm-gen` MLA decode path on `sm100/sm103`: `flashinfer/mla.py` (`trtllm_batch_decode_with_kv_cache_mla`) - XQA MLA path on `sm120/sm121`: `flashinfer/mla.py` (`xqa_batch_decode_with_kv_cache_mla`) - Blackwell CUTLASS MLA kernel wiring: `include/flashinfer/attention/cutlass_mla.cuh`, `include/flashinfer/attention/blackwell/device/sm100_mla.hpp`, `csrc/cutlass_mla.cu` - MLA-related FP8 preprocessing / cache utilities: `flashinfer/rope.py` (`mla_rope_quantize_fp8`, `rope_quantize_fp8_append_paged_kv_cache`) - Existing MLA tests: `tests/attention/test_deepseek_mla.py`, `tests/attention/test_trtllm_gen_mla.py`, `tests/attention/test_rope.py` vllm side need: implement `MLA...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: py` (`BatchMLAPagedAttentionWrapper`) - `trtllm-gen` MLA decode path on `sm100/sm103`: `flashinfer/mla.py` (`trtllm_batch_decode_with_kv_cache_mla`) - XQA MLA path on `sm120/sm121`: `flashinfer/mla.py` (`xqa_batch_decod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Add MLA + Quant support in vLLM (leveraging existing FlashInfer MLA support) feature request ### 🚀 The feature, motivation and pitch MLA + Quant` is currently marked as unsupported. https://github.com/vllm-pr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: o provide substantial MLA support, plus several MLA-related quantization building blocks. ## Existing FlashInfer MLA pieces FlashInfer already has the following MLA-related components: - MLA decode wrapper: `flashinfer/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: Add MLA + Quant support in vLLM (leveraging existing FlashInfer MLA support) feature request ### 🚀 The feature, motivation and pitch MLA + Quant` is currently marked as unsupported. https://github.com/vllm-pr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ant support in vLLM (leveraging existing FlashInfer MLA support) feature request ### 🚀 The feature, motivation and pitch MLA + Quant` is currently marked as unsupported. https://github.com/vllm-project/vllm/issues/36066...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
