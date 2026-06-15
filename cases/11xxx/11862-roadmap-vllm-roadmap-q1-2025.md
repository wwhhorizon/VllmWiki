# vllm-project/vllm#11862: [Roadmap] vLLM Roadmap Q1 2025

| 字段 | 值 |
| --- | --- |
| Issue | [#11862](https://github.com/vllm-project/vllm/issues/11862) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cache;kernel;moe |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Roadmap] vLLM Roadmap Q1 2025

### Issue 正文摘录

This page is accessible via [roadmap.vllm.ai](https://roadmap.vllm.ai/) This is a living document! For each item here, we intend to link the RFC as well as discussion Slack channel in the [vLLM Slack](https://slack.vllm.ai) ### vLLM Core _These projects will deliver performance enhancements to majority of workloads running on vLLM, and the core team has assigned priorities to signal what must get done. Help is also wanted here, especially for people want to get more involved in the core of vLLM._ **Ship a performant and modular V1 architecture (#8779, #sig-v1)** - [x] (P0) Optimized default path that is on by default - [x] (P0) Speculative decoding (n-gram on by default) - [ ] (P0) Efficient memory manager for different shapes of KV cache (#11382) - [x] (P1) Efficient structured decoding & Jump decoding in V1 (#11908) - [x] (P1) Full multi-modal support in V1 (no support encoder-decoder models). - [x] (P1) Pipeline parallelism - [x] (P1) LoRA (#10957) - [x] (P2) Hardware support: AMD first by Q1, TPU prototype. - [ ] ~(P2) Extension system: design ready.~ **Support large and long context models** - [x] (P0) Expert Parallelism for MoE - [ ] (P1) Productionize Prefill Disaggregation...

## 现有链接修复摘要

#10957 [V1] LoRA Support | #11330 [Model]: Add `transformers` backend support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: p.vllm.ai/) This is a living document! For each item here, we intend to link the RFC as well as discussion Slack channel in the [vLLM Slack](https://slack.vllm.ai) ### vLLM Core _These projects will deliver performance...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 8) - [x] (P1) Full multi-modal support in V1 (no support encoder-decoder models). - [x] (P1) Pipeline parallelism - [x] (P1) LoRA (#10957) - [x] (P2) Hardware support: AMD first by Q1, TPU prototype. - [ ] ~(P2) Extensi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Roadmap] vLLM Roadmap Q1 2025 stale This page is accessible via [roadmap.vllm.ai](https://roadmap.vllm.ai/) This is a living document! For each item here, we intend to link the RFC as well as discussion Slack channel i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: specially for people want to get more involved in the core of vLLM._ **Ship a performant and modular V1 architecture (#8779, #sig-v1)** - [x] (P0) Optimized default path that is on by default - [x] (P0) Speculative deco...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tree support for IBM Spyre and Ascend (#11162) ### Optimizations - [x] FlashAttention3 #12429 - [ ] ~AsyncTP~ - [ ] ~Design for sparse KV cache framework~ ### CI and Developer Productivity - [x] Wheel server - [x] Multi...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#10957](https://github.com/vllm-project/vllm/pull/10957) | mentioned | 0.45 | [V1] LoRA Support | r-decoder models). - [x] (p1) pipeline parallelism - [x] (p1) lora (#10957) - [x] (p2) hardware support: amd first by q1, tpu prototype. - [ ] ~(p2) extension system: design ready… |
| [#11330](https://github.com/vllm-project/vllm/pull/11330) | mentioned | 0.45 | [Model]: Add `transformers` backend support | nted) extensible sampler ### model support - [x] arbitrary hf model (#11330) - [ ] alternative or private checkpoint format ### hardware support - [x] pagedattention and chunked p… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
