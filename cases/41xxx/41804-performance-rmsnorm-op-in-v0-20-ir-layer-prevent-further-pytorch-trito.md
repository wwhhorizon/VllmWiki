# vllm-project/vllm#41804: [Performance]: RMSNorm op in v0.20 IR layer prevent further pytorch/triton op fusion

| 字段 | 值 |
| --- | --- |
| Issue | [#41804](https://github.com/vllm-project/vllm/issues/41804) |
| 状态 | open |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;model_support |
| 子分类 |  |
| Operator 关键词 | activation;cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: RMSNorm op in v0.20 IR layer prevent further pytorch/triton op fusion

### Issue 正文摘录

### Proposal to improve performance N/A ### Report of performance regression This is discovered when vLLM-Omni uses vllm's RMSNorm op and observes a performance regression. All discussion below assumes torch compile is enabled and the platform is H200 with CUDA platform ## Background/Our downstream analysis & setup - https://github.com/vllm-project/vllm-omni/issues/3266 - https://github.com/vllm-project/vllm-omni/pull/3352 ## TLDR In vllm v0.19 (with torch 2.10 and CUDA 12.9), RMSNorm becomes several native ops in torch Dynamo output, which further gets fused into a torch inductor. In vllm v0.20 (with torch 2.11 and CUDA 13.0), RMSNorm is seemingly wrapped in one atomic torch op, preventing torch to later fusing it no matter what. ## Suggestion 1 When VLLM IR set `ir_op_priority` to `native`, it wraps up those unfused native ops, potentially making torch inductor fail to fuse it, leading to ~15%-20% performance regression. CUDA graphs below: **vllm v0.19** **vllm v0.20, with `ir_op_priority` set to `native`** (The huge pink block above corresponds to the flagged area) Since this is "the platform defaults (when compiling with Inductor)", I assume the expected behavior is to "not fu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nd observes a performance regression. All discussion below assumes torch compile is enabled and the platform is H200 with CUDA platform ## Background/Our downstream analysis & setup - https://github.com/vllm-project/vll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ion below assumes torch compile is enabled and the platform is H200 with CUDA platform ## Background/Our downstream analysis & setup - https://github.com/vllm-project/vllm-omni/issues/3266 - https://github.com/vllm-proj...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: **vllm v0.20, with `ir_op_priority` set to `native`** (The huge pink block above corresponds to the flagged area) Since this is "the platform defaults (when compiling with Inductor)", I assume the expected behavior is t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ance ### Proposal to improve performance N/A ### Report of performance regression This is discovered when vLLM-Omni uses vllm's RMSNorm op and observes a performance regression. All discussion below assumes torch compil...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Performance]: RMSNorm op in v0.20 IR layer prevent further pytorch/triton op fusion performance ### Proposal to improve performance N/A ### Report of performance regression This is discovered when vLLM-Omni uses vllm's...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
