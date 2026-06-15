# vllm-project/vllm#37591: [Bug]: FlashInfer TRTLLM monolithic MoE produces 0% accuracy for Qwen3.5-35B/122B FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#37591](https://github.com/vllm-project/vllm/issues/37591) |
| 状态 | closed |
| 标签 | bug;qwen;nvidia |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | fp8;kernel;moe |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer TRTLLM monolithic MoE produces 0% accuracy for Qwen3.5-35B/122B FP8

### Issue 正文摘录

### Description The `flashinfer_trtllm` MoE backend selects the monolithic kernel (`trtllm_fp8_block_scale_moe`) for models using Renormalize routing. This kernel has a bug where all-negative router logits cause incorrect expert routing, producing 0% GSM8K accuracy for Qwen3.5-35B-A3B-FP8 and Qwen3.5-122B-A10B-FP8 with any DP+EP configuration. Upstream FlashInfer issue: https://github.com/flashinfer-ai/flashinfer/issues/2822 ### Workaround Remove `Renormalize` / `RenormalizeNaive` from `TrtLlmFp8ExpertsMonolithic._supports_routing_method()` in `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`. This causes the backend to select the modular variant (`TrtLlmFp8ExpertsModular`) which performs routing in Python and is not affected. Accuracy restored to 75-80%.

## 现有链接修复摘要

#37605 [Bugfix] Disable monolithic TRTLLM MoE for Renormalize routing (#37591) | #38859 [Bugfix] Re-enable Renormalize routing for TRT-LLM MoE experts

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ashInfer TRTLLM monolithic MoE produces 0% accuracy for Qwen3.5-35B/122B FP8 bug;qwen;nvidia ### Description The `flashinfer_trtllm` MoE backend selects the monolithic kernel (`trtllm_fp8_block_scale_moe`) for models us...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: FlashInfer TRTLLM monolithic MoE produces 0% accuracy for Qwen3.5-35B/122B FP8 bug;qwen;nvidia ### Description The `flashinfer_trtllm` MoE backend selects the monolithic kernel (`trtllm_fp8_block_scale_moe`) for...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: FlashInfer TRTLLM monolithic MoE produces 0% accuracy for Qwen3.5-35B/122B FP8 bug;qwen;nvidia ### Description The `flashinfer_trtllm` MoE backend selects the monolithic kernel (`trtllm_fp8_block_scale_moe`) for...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: FlashInfer TRTLLM monolithic MoE produces 0% accuracy for Qwen3.5-35B/122B FP8 bug;qwen;nvidia ### Description The `flashinfer_trtllm` MoE backend selects the monolithic kernel (`trtllm_fp8_block_scale_moe`) for...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: FlashInfer TRTLLM monolithic MoE produces 0% accuracy for Qwen3.5-35B/122B FP8 bug;qwen;nvidia ### Description The `flashinfer_trtllm` MoE backend selects the monolithic kernel (`trtllm_fp8_block_scale_moe`) for...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37605](https://github.com/vllm-project/vllm/pull/37605) | closes_keyword | 0.95 | [Bugfix] Disable monolithic TRTLLM MoE for Renormalize routing (#37591) | Fixes #37591, https://github.com/flashinfer-ai/flashinfer/issues/2822 ## Test plan - `python -m pytest test_trtllm_ep_bug.py -v -s -k "shift"` reproduces the kernel routin |
| [#38859](https://github.com/vllm-project/vllm/pull/38859) | mentioned | 0.6 | [Bugfix] Re-enable Renormalize routing for TRT-LLM MoE experts | ing for TRT-LLM MoE experts (BF16 and FP8). These were disabled in #37591 because the monolithic kernel's internal Renormalize routing produced output uncorrelated with the modula… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
