# vllm-project/vllm#37754: [Bug] FlashInfer + MTP speculative decoding crashes on SM121 (DGX Spark) with GQA=16 model

| 字段 | 值 |
| --- | --- |
| Issue | [#37754](https://github.com/vllm-project/vllm/issues/37754) |
| 状态 | open |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cuda;fp8;kernel;triton |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] FlashInfer + MTP speculative decoding crashes on SM121 (DGX Spark) with GQA=16 model

### Issue 正文摘录

## Summary FlashInfer attention backend + MTP speculative decoding (`num_speculative_tokens=2`) crashes with "illegal memory access" on NVIDIA GB10 (SM121 / DGX Spark) when serving Nemotron-3-Super-120B-A12B-NVFP4 (GQA ratio = 16). Triton attention backend works correctly. ## Reproduction ```bash # Works (Triton attention): vllm serve /models/nemotron-3-super \ --attention-backend triton_attn \ --speculative-config '{"method":"mtp","num_speculative_tokens":2}' \ --kv-cache-dtype fp8 \ --no-enable-chunked-prefill # Crashes (FlashInfer attention): vllm serve /models/nemotron-3-super \ --attention-backend flashinfer \ --speculative-config '{"method":"mtp","num_speculative_tokens":2}' \ --kv-cache-dtype fp8 \ --no-enable-chunked-prefill # → First request returns 500, BatchPrefillWithPagedKVCache illegal memory access ``` ### Key observations - `LLM().generate()` with FlashInfer + MTP=2 **works** (single synchronous request) - `vllm serve` with FlashInfer + MTP=2 **crashes** on the first request - Triton attention backend works perfectly at 22.4 tok/s with MTP=2 - MTP=1 with FlashInfer works; MTP=2+ crashes - The crash is in FlashInfer's `BatchPrefillWithPagedKVCacheRun` kernel ## Erro...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: NVIDIA GB10 (SM121 / DGX Spark) when serving Nemotron-3-Super-120B-A12B-NVFP4 (GQA ratio = 16). Triton attention backend works correctly. ## Reproduction ```bash # Works (Triton attention): vllm serve /models/nemotron-3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug] FlashInfer + MTP speculative decoding crashes on SM121 (DGX Spark) with GQA=16 model ## Summary FlashInfer attention backend + MTP speculative decoding (`num_speculative_tokens=2`) crashes with "illegal memory acc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug] FlashInfer + MTP speculative decoding crashes on SM121 (DGX Spark) with GQA=16 model ## Summary FlashInfer attention backend + MTP speculative decoding (`num_speculative_tokens=2`) crashes with "illegal memory acc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug] FlashInfer + MTP speculative decoding crashes on SM121 (DGX Spark) with GQA=16 model ## Summary FlashInfer attention backend + MTP speculative decoding (`num_speculative_tokens=2`) crashes with "illegal memory acc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nfer + MTP speculative decoding crashes on SM121 (DGX Spark) with GQA=16 model ## Summary FlashInfer attention backend + MTP speculative decoding (`num_speculative_tokens=2`) crashes with "illegal memory access" on NVID...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
