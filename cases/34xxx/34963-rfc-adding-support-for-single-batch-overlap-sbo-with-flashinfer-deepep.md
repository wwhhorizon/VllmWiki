# vllm-project/vllm#34963: [RFC]: Adding Support for Single Batch Overlap (SBO) With FlashInfer DeepEP LL NVFP4

| 字段 | 值 |
| --- | --- |
| Issue | [#34963](https://github.com/vllm-project/vllm/issues/34963) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;gemm_linear;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;gemm;kernel;moe;operator |
| 症状 | slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Adding Support for Single Batch Overlap (SBO) With FlashInfer DeepEP LL NVFP4

### Issue 正文摘录

# Background DeepEP's combine_v2 kernel supports overlapping the combine all-to-all with GEMM2 by polling per-expert completion signals instead of waiting for all experts to finish before sending. SGLang implements this but vllm does not. # DeepEP Support https://github.com/fzyzcjy/DeepEP/tree/gb200_blog_part_2/ (as per https://lmsys.org/blog/2025-09-25-gb200-part-2/) implements combine_v2, but https://github.com/elvircrn/DeepEP/tree/gb200_blog might be more convenient to use on CUDA 13 as it contains a patched CUDA 13 setup.py. # Relevant SGLang sources - python/sglang/srt/batch_overlap/single_batch_overlap.py — CombineOverlapArgs / DownGemmOverlapArgs dataclasses, signal tensor creation, SM partitioning - python/sglang/srt/layers/moe/flashinfer_cutedsl_moe.py — passes sm_count=down_sm_count, dst_signals=down_signals to GEMM2 - python/sglang/srt/layers/moe/token_dispatcher/deepep.py — launches combine on a secondary stream with overlap=True, src_signals=..., src_signal_expect_value=... # Tracing Estimating the potential impact of this change, tracing was done on the following setup: ``` E8/E32 P/D 500 ISL 1500 OSL DeepSeek R1 NVFP4 ``` Decode trace: The combine step is taking sin...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: llm does not. # DeepEP Support https://github.com/fzyzcjy/DeepEP/tree/gb200_blog_part_2/ (as per https://lmsys.org/blog/2025-09-25-gb200-part-2/) implements combine_v2, but https://github.com/elvircrn/DeepEP/tree/gb200_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: am with overlap=True, src_signals=..., src_signal_expect_value=... # Tracing Estimating the potential impact of this change, tracing was done on the following setup: ``` E8/E32 P/D 500 ISL 1500 OSL DeepSeek R1 NVFP4 ```...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Adding Support for Single Batch Overlap (SBO) With FlashInfer DeepEP LL NVFP4 RFC;stale # Background DeepEP's combine_v2 kernel supports overlapping the combine all-to-all with GEMM2 by polling per-expert completion sig...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: pEP's combine_v2 kernel supports overlapping the combine all-to-all with GEMM2 by polling per-expert completion signals instead of waiting for all experts to finish before sending. SGLang implements this but vllm does n...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: pport for Single Batch Overlap (SBO) With FlashInfer DeepEP LL NVFP4 RFC;stale # Background DeepEP's combine_v2 kernel supports overlapping the combine all-to-all with GEMM2 by polling per-expert completion signals inst...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
