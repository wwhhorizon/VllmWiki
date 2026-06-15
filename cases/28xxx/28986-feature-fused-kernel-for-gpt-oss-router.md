# vllm-project/vllm#28986: [Feature]: Fused Kernel for GPT-OSS Router

| 字段 | 值 |
| --- | --- |
| Issue | [#28986](https://github.com/vllm-project/vllm/issues/28986) |
| 状态 | open |
| 标签 | help wanted;good first issue;feature request;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;moe |
| 子分类 | install |
| Operator 关键词 | cuda;kernel;moe;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Fused Kernel for GPT-OSS Router

### Issue 正文摘录

### 🚀 The feature, motivation and pitch - Right now, we spend ~3.5% of the layer in the expert selection - The operation is unfused Write a fused kernel like we have for deepseek grouped_topk ### Alternatives - torch compile - triton - cuda ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#29237 [Optimization] Add Fused Triton Kernel for GPT-OSS Router | #30471 [Optimization]: Add fused router for GPTOSS

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: kernel like we have for deepseek grouped_topk ### Alternatives - torch compile - triton - cuda ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Feature]: Fused Kernel for GPT-OSS Router help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch - Right now, we spend ~3.5% of the layer in the expert selection - The operation is u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: for deepseek grouped_topk ### Alternatives - torch compile - triton - cuda ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e]: Fused Kernel for GPT-OSS Router help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch - Right now, we spend ~3.5% of the layer in the expert selection - The operation is unfused...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e we have for deepseek grouped_topk ### Alternatives - torch compile - triton - cuda ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, an...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29237](https://github.com/vllm-project/vllm/pull/29237) | closes_keyword | 0.95 | [Optimization] Add Fused Triton Kernel for GPT-OSS Router | Resolves: #28986 1. add a fused topk+softmax triton kernel for gptoss and others. 2. minimize modification in model's interface, by indicating custom_routing_function. ## Test P |
| [#30471](https://github.com/vllm-project/vllm/pull/30471) | closes_keyword | 0.95 | [Optimization]: Add fused router for GPTOSS | Resolves: #28986 Add fused routing, including topk,softmax,sub_bitmatrix_rows, two combined_routing* Only consider GPTOSS model's num_experts and topk ## Test Plan Add GPTOSS20B |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
