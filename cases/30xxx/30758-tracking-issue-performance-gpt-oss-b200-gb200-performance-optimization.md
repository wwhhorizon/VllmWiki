# vllm-project/vllm#30758: [Tracking Issue][Performance] GPT-OSS B200/GB200 performance optimization tracker

| 字段 | 值 |
| --- | --- |
| Issue | [#30758](https://github.com/vllm-project/vllm/issues/30758) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;gemm_linear;model_support;moe;quantization;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | activation;attention;fp8;gemm;kernel;moe;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Tracking Issue][Performance] GPT-OSS B200/GB200 performance optimization tracker

### Issue 正文摘录

### Proposal to improve performance This issue tracks the ungoing/pending performance optimizations for GPT-OSS B200/GB200. **Max-Throughput** (e.g. TP1 conc1024) - [x] Enable FlashInfer autotuning. Done in https://github.com/vllm-project/vllm/pull/22346 - [x] Enable FlashInfer FP8-QKV attention with sink. Done in https://github.com/vllm-project/vllm/pull/25674 - [x] Support stream_interval to reduce host overhead at high concurrency. Done in https://github.com/vllm-project/vllm/pull/27869 **Min-Latency** (e.g. TP8 conc8) - [x] Avoid additional Slice before AR+Norm fused kernel. Done in https://github.com/vllm-project/vllm/pull/29631 - [x] Fuse Pad with MXFP8-Quantize (~1% perf gain, assigned to @elvischenv ) - See: https://github.com/vllm-project/vllm/pull/30647 - [x] Fuse MoE Finalize with Slice (~1% perf gain, assigned to @elvischenv ) - FlashInfer MXFP4 MoE supports fusion with Slice. See https://github.com/flashinfer-ai/flashinfer/pull/2217 - See: https://github.com/vllm-project/vllm/pull/30647 - [ ] RoPE+Q+CacheUpdate fusion (~2% perf gain, will be tracked in #24678 ) - We can use FlashInfer [rope_quantize_fp8_append_paged_kv_cache()](https://github.com/flashinfer-ai/flashin...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: https://github.com/vllm-project/vllm/pull/22346 - [x] Enable FlashInfer FP8-QKV attention with sink. Done in https://github.com/vllm-project/vllm/pull/25674 - [x] Support stream_interval to reduce host overhead at high...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ungoing/pending performance optimizations for GPT-OSS B200/GB200. **Max-Throughput** (e.g. TP1 conc1024) - [x] Enable FlashInfer autotuning. Done in https://github.com/vllm-project/vllm/pull/22346 - [x] Enable FlashInfe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Tracking Issue][Performance] GPT-OSS B200/GB200 performance optimization tracker performance ### Proposal to improve performance This issue tracks the ungoing/pending performance optimizations for GPT-OSS B200/GB200. *...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: nv ) - See: https://github.com/vllm-project/vllm/pull/30647 - [x] Fuse MoE Finalize with Slice (~1% perf gain, assigned to @elvischenv ) - FlashInfer MXFP4 MoE supports fusion with Slice. See https://github.com/flashinf...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: assigned) - Done in https://github.com/vllm-project/vllm/pull/37205 **Spec Decode** - [x] Support [nvidia/gpt-oss-120b-Eagle3-short-context](https://huggingface.co/nvidia/gpt-oss-120b-Eagle3-short-context) EAGLE model....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
