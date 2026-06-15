# vllm-project/vllm#32180: [Bug]: Performance Bottlenecks and V1 Engine Instability on AMD gfx1151 (Strix Halo)

| 字段 | 值 |
| --- | --- |
| Issue | [#32180](https://github.com/vllm-project/vllm/issues/32180) |
| 状态 | open |
| 标签 | bug;performance;feature request;rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;kernel;triton |
| 症状 | crash;oom;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Performance Bottlenecks and V1 Engine Instability on AMD gfx1151 (Strix Halo)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The Problem: We are currently unable to leverage the full potential of the vLLM V1 Engine on the gfx1151 architecture. During the HIP Graph capture phase, the engine encounters a driver-level timeout, leading to a total loss of communication between the API server and the engine core (observed as a Network/Socket Error). Current Workaround & Impact: To maintain system stability, we are forced to run with --enforce-eager. While this allows inference to proceed, it introduces significant technical debt: Disabled HIP Graphs: Every kernel is launched individually, causing massive CPU overhead and latency on a high-performance APU. V1 Engine Bypass: We cannot use the multi-step scheduling and optimized fused kernels that make vLLM V1 superior. Memory Bottleneck: We are unable to fully exploit the 128MB L3 (MALL) cache benefits of the Strix Halo for KV cache management due to the fallback to eager execution patterns. Specific Questions for the Roadmap: When is native, stable support for gfx1151 ISA expected for the vLLM V1 engine's graph capture? Are there specific Triton or CK (Composable Kernel) environment flags we should use to byp...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Instability on AMD gfx1151 (Strix Halo) bug;performance;feature request;rocm ### Your current environment ### 🐛 Describe the bug The Problem: We are currently unable to leverage the full potential of the vLLM V1 Engine...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Every kernel is launched individually, causing massive CPU overhead and latency on a high-performance APU. V1 Engine Bypass: We cannot use the multi-step scheduling and optimized fused kernels that make vLLM V1 superior...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ALL) cache benefits of the Strix Halo for KV cache management due to the fallback to eager execution patterns. Specific Questions for the Roadmap: When is native, stable support for gfx1151 ISA expected for the vLLM V1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: KV cache management due to the fallback to eager execution patterns. Specific Questions for the Roadmap: When is native, stable support for gfx1151 ISA expected for the vLLM V1 engine's graph capture? Are there specific...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: o fully exploit the 128MB L3 (MALL) cache benefits of the Strix Halo for KV cache management due to the fallback to eager execution patterns. Specific Questions for the Roadmap: When is native, stable support for gfx115...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
