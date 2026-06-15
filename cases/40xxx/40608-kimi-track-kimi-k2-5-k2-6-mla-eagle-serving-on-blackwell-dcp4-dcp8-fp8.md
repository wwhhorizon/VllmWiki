# vllm-project/vllm#40608: [Kimi] Track Kimi K2.5/K2.6 MLA + EAGLE serving on Blackwell (DCP4/DCP8, FP8 KV, draft backend split)

| 字段 | 值 |
| --- | --- |
| Issue | [#40608](https://github.com/vllm-project/vllm/issues/40608) |
| 状态 | open |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Kimi] Track Kimi K2.5/K2.6 MLA + EAGLE serving on Blackwell (DCP4/DCP8, FP8 KV, draft backend split)

### Issue 正文摘录

This issue tracks the Kimi-K2.6 + Eagle3-MLA MTP serving stack validated on Blackwell, and the PR stack needed to reconstruct it from upstream vLLM. ## Canonical stack Target workload: - target model: `moonshotai/Kimi-K2.6` - draft model: `lightseekorg/kimi-k2.5-eagle3-mla` - speculative method: `eagle3`, `num_speculative_tokens=3`, probabilistic rejection sampling Hardware/runtime assumptions: - 8x RTX 6000 Pro Blackwell / sm120 - TP=8 - DCP=1, DCP=4, or DCP=8 depending on latency/KV-cache target - `TRITON_MLA` for target and draft - fp8 KV cache - external NCCL graph XML is still the best-known runtime recipe for this machine class Validated shipping image: - `voipmonitor/vllm:cu130-mtp-tuned-v3-20260423` Reference documentation: - https://github.com/voipmonitor/rtx6kpro/tree/master/models/kimi-k26-mtp-long-ctx-wip - Plan/review notes: `upstream-pr-plan.md`, `upstream-pr-plan-review.md` - Verbatim Docker source snapshots: `patches/triton_mla_final.py`, `patches/triton_mla_tuning.py` ## Why this issue exists The original long-context MTP path was slow because `TRITON_MLA` did not support full CUDA graph capture for the uniform spec-verify decode shapes used by Eagle3/MTP. The ser...

## 现有链接修复摘要

#40613 [SpecDecode] Add seq-length gate for speculative decode | #40614 [Attention] Tune TRITON_MLA for SM120 + FP8 decode | #40750 [Attention] Enable TRITON_MLA MTP full CUDA graphs for Kimi on Blackwell

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: rack Kimi K2.5/K2.6 MLA + EAGLE serving on Blackwell (DCP4/DCP8, FP8 KV, draft backend split) This issue tracks the Kimi-K2.6 + Eagle3-MLA MTP serving stack validated on Blackwell, and the PR stack needed to reconstruct...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: fp8 KV cache - external NCCL graph XML is still the best-known runtime recipe for this machine class Validated shipping image: - `voipmonitor/vllm:cu130-mtp-tuned-v3-20260423` Reference documentation: - https://github.c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Kimi] Track Kimi K2.5/K2.6 MLA + EAGLE serving on Blackwell (DCP4/DCP8, FP8 KV, draft backend split) This issue tracks the Kimi-K2.6 + Eagle3-MLA MTP serving stack validated on Blackwell, and the PR stack needed to rec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ct it from upstream vLLM. ## Canonical stack Target workload: - target model: `moonshotai/Kimi-K2.6` - draft model: `lightseekorg/kimi-k2.5-eagle3-mla` - speculative method: `eagle3`, `num_speculative_tokens=3`, probabi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: 6000 Pro Blackwell / sm120 - TP=8 - DCP=1, DCP=4, or DCP=8 depending on latency/KV-cache target - `TRITON_MLA` for target and draft - fp8 KV cache - external NCCL graph XML is still the best-known runtime recipe for thi...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40613](https://github.com/vllm-project/vllm/pull/40613) | mentioned | 0.6 | [SpecDecode] Add seq-length gate for speculative decode | ath and in the worker-side drafter fit check ## Context Tracked from #40608. ## Why For Kimi MLA long-context workloads, speculative decode can become slower than target-only deco… |
| [#40614](https://github.com/vllm-project/vllm/pull/40614) | mentioned | 0.6 | [Attention] Tune TRITON_MLA for SM120 + FP8 decode | `BLOCK_H` for the same narrow configuration ## Context Tracked from #40608. ## Why For Blackwell/SM120 MLA decode with FP8 KV cache, the default split heuristic can overshoot and… |
| [#40750](https://github.com/vllm-project/vllm/pull/40750) | mentioned | 0.6 | [Attention] Enable TRITON_MLA MTP full CUDA graphs for Kimi on Blackwell | ode/prefill throughput against the final image benchmark reference in #40608. ## Notes for review This is opened as a draft consolidation PR so the full runnable stack can be test… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
