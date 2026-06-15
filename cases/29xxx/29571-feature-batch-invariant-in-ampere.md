# vllm-project/vllm#29571: [Feature]: Batch-invariant in Ampere

| 字段 | 值 |
| --- | --- |
| Issue | [#29571](https://github.com/vllm-project/vllm/issues/29571) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;moe |
| 子分类 |  |
| Operator 关键词 | attention;moe |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Batch-invariant in Ampere

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In the vLLM 0.11.1 release notes, I came across the following update: Batch-invariant torch.compile: Generalized batch-invariant support across attention and MoE backends, with explicit support for DeepGEMM and FlashInfer on Hopper and Blackwell GPUs. I attempted to enable batch-invariant functionality on Ampere architecture GPUs (specifically, RTX 3090), but it does not seem to work fully. 1. Is it feasible to adapt vLLM’s batch-invariant support for Ampere GPUs? 2. If so, what specific modifications would be needed in the batch_invariant.py(or related components) in vLLM versions 0.11.1 or 0.11.2 to achieve this? Any insights or references to relevant resources would be greatly @yewentao256 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: release notes, I came across the following update: Batch-invariant torch.compile: Generalized batch-invariant support across attention and MoE backends, with explicit support for DeepGEMM and FlashInfer on Hopper and Bl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Feature]: Batch-invariant in Ampere feature request;stale ### 🚀 The feature, motivation and pitch In the vLLM 0.11.1 release notes, I came across the following update: Batch-invariant torch.compile: Generalized batch-i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ch.compile: Generalized batch-invariant support across attention and MoE backends, with explicit support for DeepGEMM and FlashInfer on Hopper and Blackwell GPUs. I attempted to enable batch-invariant functionality on A...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: torch.compile: Generalized batch-invariant support across attention and MoE backends, with explicit support for DeepGEMM and FlashInfer on Hopper and Blackwell GPUs. I attempted to enable batch-invariant functionality o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Batch-invariant in Ampere feature request;stale ### 🚀 The feature, motivation and pitch In the vLLM 0.11.1 release notes, I came across the following update: Batch-invariant torch.compile: Generalized batch-i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
