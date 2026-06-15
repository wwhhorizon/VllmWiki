# vllm-project/vllm#41820: [Performance]: Deepseek-V4 Support and Optimization on ROCm Backend

| 字段 | 值 |
| --- | --- |
| Issue | [#41820](https://github.com/vllm-project/vllm/issues/41820) |
| 状态 | open |
| 标签 | performance;rocm;DSv4 |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | activation;attention;fp8;kernel;moe;operator;triton |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Deepseek-V4 Support and Optimization on ROCm Backend

### Issue 正文摘录

## Motivation This issue tracks the end-to-end enablement and optimization checklist for **DeepSeek-V4 on ROCm backend**. DeepSeek-V4 includes multiple critical blocks (mHC/HCA/CSA/MoE/MTP), and ROCm readiness depends on both model-side kernels and system-side runtime behavior. We’re launching a joint effort to optimize DeepSeek V4 on the ROCm backend—please feel free to take on any task, and we’d love to hear more optimization ideas. ## Purpose - [ ] Track DeepSeek-V4 functionality and performance readiness on ROCm backend. - [ ] Keep module-level optimization items visible and actionable. - [ ] Align acceptance criteria for release and production readiness. --- ## Recipe - [ ] Recipe: `vLLM Recipe: DeepSeek-V4 on AMD (ROCm) Usage Guide - vLLM Recipes` https://github.com/vllm-project/recipes/pull/433 ## General Checklist ### 1) Functionality / Bugfix / Feature - [x] [Functionality] Base PR has been merged for functionality/accuracy readiness on MI35x for DeepSeek-V4-Pro and DeepSeek-V4-Flash. - [ ] [Functionality] DeepSeek-V4-Flash Base FP8 enablement PR: - [ ] [Functionality] MI30x support PR: - [ ] [Bugfix] Enable cross-node TP=16 FP8 serving for DeepSeek-V4: - [ ] [Feature][WI...

## 现有链接修复摘要

#43365 [ROCm][DSV4] Enable opt-in CSA multi-stream decode overlap on ROCm | #43718 [ROCm][DeepSeek-V4] Enable CSA multistream decode

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Performance]: Deepseek-V4 Support and Optimization on ROCm Backend performance;rocm;DSv4 ## Motivation This issue tracks the end-to-end enablement and optimization checklist for **DeepSeek-V4 on ROCm backend**. DeepSee...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ign acceptance criteria for release and production readiness. --- ## Recipe - [ ] Recipe: `vLLM Recipe: DeepSeek-V4 on AMD (ROCm) Usage Guide - vLLM Recipes` https://github.com/vllm-project/recipes/pull/433 ## General C...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ro and DeepSeek-V4-Flash. - [ ] [Functionality] DeepSeek-V4-Flash Base FP8 enablement PR: - [ ] [Functionality] MI30x support PR: - [ ] [Bugfix] Enable cross-node TP=16 FP8 serving for DeepSeek-V4: - [ ] [Feature][WIP]...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: m backend**. DeepSeek-V4 includes multiple critical blocks (mHC/HCA/CSA/MoE/MTP), and ROCm readiness depends on both model-side kernels and system-side runtime behavior. We’re launching a joint effort to optimize DeepSe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ist ### 1) High-Level Performance/Feature - [x] Full graph support for Decode path. Piecewise graph capture support for Prefill path. - [ ] Support MTP ### 2) Kernel Fusion #### Element-wise Fusion - [x] Avoid redundant...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43365](https://github.com/vllm-project/vllm/pull/43365) | closes_keyword | 0.95 | [ROCm][DSV4] Enable opt-in CSA multi-stream decode overlap on ROCm | Fixes #41820 (partial — CSA multi-stream item) Made with [Cursor](https://cursor.com) |
| [#43718](https://github.com/vllm-project/vllm/pull/43718) | mentioned | 0.6 | [ROCm][DeepSeek-V4] Enable CSA multistream decode | [ROCm][DeepSeek-V4] Enable CSA multistream decode Addresses #41820. ## Summary This PR enables ROCm DeepSeek-V4 CSA multistream decode. Changes: - Adds ROCm CSA multistream |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
