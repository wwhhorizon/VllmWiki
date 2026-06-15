# vllm-project/vllm#34234: [Feature]: Enable CUDA graph capture for Eagle speculator prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#34234](https://github.com/vllm-project/vllm/issues/34234) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Enable CUDA graph capture for Eagle speculator prefill

### Issue 正文摘录

## 🚀 The feature, motivation and pitch Eagle’s speculator currently runs prefill in eager mode, while decode can use CUDA graphs. There is an explicit TODO in the codebase to support CUDA graphs for the prefill path. I’m interested in working on this as my first contribution and wanted to check alignment before starting any implementation. Currently, the Eagle speculator contains the following TODO: - **Location:** `vllm/v1/worker/gpu/spec_decode/eagle.py` (around line 229) - **Current state:** Prefill always runs in eager mode - **Decode state:** CUDA graphs are supported for decode-only operations The TODO in the file: ```python # Prefill: Run the eagle speculator with eager mode. # TODO(woosuk): Support CUDA graph for prefill. ``` ### Goal Enable CUDA graph capture for Eagle's prefill operations where feasible, with appropriate fallback to eager mode when CUDA graphs cannot be used. **Scope considerations:** - Start with simpler batch configurations (e.g., uniform batches) to minimize risk - Respect existing `cudagraph_capture_sizes` configuration - Maintain backward compatibility with explicit fallbacks - Add test coverage for new behavior and regression prevention **Out of sc...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Enable CUDA graph capture for Eagle speculator prefill feature request ## 🚀 The feature, motivation and pitch Eagle’s speculator currently runs prefill in eager mode, while decode can use CUDA graphs. There i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: efill in eager mode, while decode can use CUDA graphs. There is an explicit TODO in the codebase to support CUDA graphs for the prefill path. I’m interested in working on this as my first contribution and wanted to chec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Enable CUDA graph capture for Eagle speculator prefill feature request ## 🚀 The feature, motivation and pitch Eagle’s speculator currently runs prefill in eager mode, while decode can use CUDA graphs. There i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: guration - Maintain backward compatibility with explicit fallbacks - Add test coverage for new behavior and regression prevention **Out of scope (for initial implementation):** - Complex batch configurations ### Questio...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: capture for Eagle's prefill operations where feasible, with appropriate fallback to eager mode when CUDA graphs cannot be used. **Scope considerations:** - Start with simpler batch configurations (e.g., uniform batches)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
