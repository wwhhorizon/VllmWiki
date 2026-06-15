# vllm-project/vllm#31475: [Bug]: FP8 inference much slower than BF16 on MI300X for GLM-4.7 and MiniMax-M2.1

| 字段 | 值 |
| --- | --- |
| Issue | [#31475](https://github.com/vllm-project/vllm/issues/31475) |
| 状态 | open |
| 标签 | bug;rocm;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | fp8;kernel;moe |
| 症状 | build_error;slowdown |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FP8 inference much slower than BF16 on MI300X for GLM-4.7 and MiniMax-M2.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## FP8 inference is significantly slower than BF16 on MI300X for MoE models (GLM-4.7, MiniMax-M2.1) ### Summary On AMD MI300X, FP8 inference in vLLM is consistently **slower than BF16** in steady-state decoding for large MoE models. This contradicts expected FP8 performance characteristics and suggests inefficiencies or regressions in the FP8 execution path on ROCm. This issue is reproducible across both GLM-4.7 and MiniMax-M2.1 and persists after warm-up, compilation, and cache amortization. Load time is not a factor; all numbers below reflect sustained inference throughput (TPS). --- ### Environment - Hardware: **8× AMD MI300X** - Backend: ROCm - vLLM: `rocm/vllm-dev:nightly` (recent nightly at time of testing) - Serving mode: `vllm serve` (OpenAI-compatible API) - Tensor parallelism: TP=8 - Identical batching, prompts, output lengths, and server settings across runs - Measurements taken after warm-up (steady state) --- ### Models Tested 1. **GLM-4.7** (160-expert MoE) 2. **MiniMax-M2.1** (256 local experts, 8 experts per token) For MiniMax-M2.1, both: - the original FP8 / mixed-precision checkpoint, and - a (**manually convert...

## 现有链接修复摘要

#31653 [Hardware][AMD] Enable AITER by default for optimized ROCm performance

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: FP8 inference much slower than BF16 on MI300X for GLM-4.7 and MiniMax-M2.1 bug;rocm;stale ### Your current environment ### 🐛 Describe the bug ## FP8 inference is significantly slower than BF16 on MI300X for MoE m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: FP8 inference much slower than BF16 on MI300X for GLM-4.7 and MiniMax-M2.1 bug;rocm;stale ### Your current environment ### 🐛 Describe the bug ## FP8 inference is significantly slower than BF16 on MI300X for MoE m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: throughput (TPS). --- ### Environment - Hardware: **8× AMD MI300X** - Backend: ROCm - vLLM: `rocm/vllm-dev:nightly` (recent nightly at time of testing) - Serving mode: `vllm serve` (OpenAI-compatible API) - Tensor paral...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: contradicts expected FP8 performance characteristics and suggests inefficiencies or regressions in the FP8 execution path on ROCm. This issue is reproducible across both GLM-4.7 and MiniMax-M2.1 and persists after warm-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ug ## FP8 inference is significantly slower than BF16 on MI300X for MoE models (GLM-4.7, MiniMax-M2.1) ### Summary On AMD MI300X, FP8 inference in vLLM is consistently **slower than BF16** in steady-state decoding for l...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31653](https://github.com/vllm-project/vllm/pull/31653) | closes_keyword | 0.95 | [Hardware][AMD] Enable AITER by default for optimized ROCm performance | Fixes #31475 🤖 Generated with [Claude Code](https://claude.com/claude-code) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
