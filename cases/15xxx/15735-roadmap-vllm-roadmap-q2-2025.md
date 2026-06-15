# vllm-project/vllm#15735: [Roadmap] vLLM Roadmap Q2 2025

| 字段 | 值 |
| --- | --- |
| Issue | [#15735](https://github.com/vllm-project/vllm/issues/15735) |
| 状态 | closed |
| 标签 |  |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;moe |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Roadmap] vLLM Roadmap Q2 2025

### Issue 正文摘录

This page is accessible via [roadmap.vllm.ai](https://roadmap.vllm.ai/) This is a living document! For each item here, we intend to link the RFC as well as discussion Slack channel in the [vLLM Slack](https://slack.vllm.ai) --- #### Core Themes **Path to vLLM v1.0.0** *We want to fully remove the V0 engine and clean up the codebase for unpopular and unsupported features. The v1.0.0 version of vLLM will be performant and easy to maintain, as well as modular and extensible, with backward compatibility.* - [ ] V1 core feature set - [x] Hybrid memory allocators - [ ] ~Jump decoding~ - [x] Redesigned native support for pipeline parallelism - [x] Redesigned spec decode - [ ] Redesigned sampler with modularity support - [ ] Close the feature gaps and fully remove V0 - [x] Attention backends - [ ] Pooling models - [ ] Mamba/Hybrid models - [ ] (TBD) encoder and encoder decoder - [x] Hardware support - [ ] Performance - [ ] Further lower scheduler overhead - [x] Further enhance LoRA performance - [x] API Server Scale-out **Cluster Scale Serving** *As the model expands in size, serving them in multi-node scale-out and disaggregating prefill and decode becomes the way to go. We are fully com...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: t - [ ] Close the feature gaps and fully remove V0 - [x] Attention backends - [ ] Pooling models - [ ] Mamba/Hybrid models - [ ] (TBD) encoder and encoder decoder - [x] Hardware support - [ ] Performance - [ ] Further l...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [x] API Server and Engine decoupling (any to any communication) - [x] Expert Parallelism - [x] DeepEP and pplx integrations - [x] Transition from fused\_moe to cutlass based grouped gemm. - [ ] Online Reconfiguration (e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: designed native support for pipeline parallelism - [x] Redesigned spec decode - [ ] Redesigned sampler with modularity support - [ ] Close the feature gaps and fully remove V0 - [x] Attention backends - [ ] Pooling mode...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: p.vllm.ai/) This is a living document! For each item here, we intend to link the RFC as well as discussion Slack channel in the [vLLM Slack](https://slack.vllm.ai) --- #### Core Themes **Path to vLLM v1.0.0** *We want t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Jump decoding~ - [x] Redesigned native support for pipeline parallelism - [x] Redesigned spec decode - [ ] Redesigned sampler with modularity support - [ ] Close the feature gaps and fully remove V0 - [x] Attention back...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
