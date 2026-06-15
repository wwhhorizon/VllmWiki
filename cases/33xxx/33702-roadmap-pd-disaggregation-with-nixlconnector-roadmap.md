# vllm-project/vllm#33702: [Roadmap]: PD Disaggregation with `NixlConnector` Roadmap

| 字段 | 值 |
| --- | --- |
| Issue | [#33702](https://github.com/vllm-project/vllm/issues/33702) |
| 状态 | open |
| 标签 | help wanted;feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8 |
| 症状 | mismatch;slowdown |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Roadmap]: PD Disaggregation with `NixlConnector` Roadmap

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Description This RFC tracks the current state and planned improvements for Prefill-Decode (P/D) Disaggregation using the NixlConnector, which enables high-performance KV cache transfer between prefill and decode instances using the NIXL library. # Currently Supported Features Core Infrastructure - [x] NIXL Integration - Core P/D disaggregation framework (https://github.com/vllm-project/vllm/pull/17751) **Async KV Cache Transfers** - [x] Fully asynchronous KV cache transfers - https://github.com/vllm-project/vllm/pull/33377 - Bugfix for async scheduling + request abort + async KV transfer - https://github.com/vllm-project/vllm/pull/28327 - Simplify async KV output aggregation - https://github.com/vllm-project/vllm/pull/27648 - Async scheduling support - https://github.com/vllm-project/vllm/pull/31583 - Fix resuming preempted requests after async load **Multi-Transport Backend Support** - [x] Multi-transport backend support - UCX (default), LIBFABRIC, and other NIXL plugins - ROCm support through RIXL library - Support for OOT NIXL backends via kv_connector_extra_config (https://github.com/vllm-project/vllm/pull/33552) **Tensor Parallelism*...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: d logging with failure context for easier debugging - [ ] Enable drain scaledown mode for single process deployments - https://github.com/vllm-project/vllm/pull/32420 - [x] Speculative decoding integration - P/D disaggr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: map]: PD Disaggregation with `NixlConnector` Roadmap help wanted;feature request ### 🚀 The feature, motivation and pitch ## Description This RFC tracks the current state and planned improvements for Prefill-Decode (P/D)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: backend support - UCX (default), LIBFABRIC, and other NIXL plugins - ROCm support through RIXL library - Support for OOT NIXL backends via kv_connector_extra_config (https://github.com/vllm-project/vllm/pull/33552) **Te...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: RIXL library - Support for OOT NIXL backends via kv_connector_extra_config (https://github.com/vllm-project/vllm/pull/33552) **Tensor Parallelism** - [x] Homogeneous Tensor Parallelism - P and D instances with matching...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: - Fix resuming preempted requests after async load **Multi-Transport Backend Support** - [x] Multi-transport backend support - UCX (default), LIBFABRIC, and other NIXL plugins - ROCm support through RIXL library - Suppo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
