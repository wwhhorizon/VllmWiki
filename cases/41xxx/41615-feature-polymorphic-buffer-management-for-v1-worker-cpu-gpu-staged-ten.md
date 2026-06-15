# vllm-project/vllm#41615: [Feature]: Polymorphic buffer management for V1 worker (CPU/GPU staged tensors, lower hot-path overhead)

| 字段 | 值 |
| --- | --- |
| Issue | [#41615](https://github.com/vllm-project/vllm/issues/41615) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Polymorphic buffer management for V1 worker (CPU/GPU staged tensors, lower hot-path overhead)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Summary This proposes a polymorphic buffer management path for the V1 worker so internal staged tensors can be handled consistently across CPU and GPU, while reducing hot-path overhead from transient buffer work. **Prototype branch:** `masterFoad/vllm:pr-polymorphic-buffers-clean` **Branch URL:** https://github.com/masterFoad/vllm/tree/pr-polymorphic-buffers-clean **Head commit:** `31e0aa38c` ## Motivation The current buffer/staging flow can incur avoidable overhead in decode and input-prep paths due to temporary allocations and host-side staging patterns. A unified buffer abstraction should improve maintainability and reduce per-step overhead in performance-critical paths. ## Proposed Change - Introduce `DeviceMemoryManager` to centralize staged tensor allocation strategy. - Use polymorphic staged-write tensors via `.device_tensor` instead of GPU-only assumptions. - Keep CPU-compatible and CUDA-compatible staged write paths under one abstraction. - Refactor V1 worker callsites to use the new staged buffer flow. ## Scope in Prototype Branch Representative files touched: - `vllm/v1/worker/gpu/buffer_utils.py` - `vllm/v1/worker/gpu/model_ru...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: evice_tensor` instead of GPU-only assumptions. - Keep CPU-compatible and CUDA-compatible staged write paths under one abstraction. - Refactor V1 worker callsites to use the new staged buffer flow. ## Scope in Prototype...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: for V1 worker (CPU/GPU staged tensors, lower hot-path overhead) feature request ### 🚀 The feature, motivation and pitch ## Summary This proposes a polymorphic buffer management path for the V1 worker so internal staged...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: `2.11.0+cu129` - **vLLM:** `0.7.3` - **Model:** `Qwen2.5-1.5B-Instruct` Throughput result: | Branch | Throughput | |---|---:| | `main` | **4.37 req/s** | | `pr-polymorphic-buffers-clean` | **4.78 req/s** | **Delta:** `+...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s touched: - `vllm/v1/worker/gpu/buffer_utils.py` - `vllm/v1/worker/gpu/model_runner.py` - `vllm/v1/worker/gpu/states.py` - `vllm/v1/worker/gpu/block_table.py` - `vllm/v1/worker/gpu/model_states/default.py` - `vllm/v1/w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: staged tensors can be handled consistently across CPU and GPU, while reducing hot-path overhead from transient buffer work. **Prototype branch:** `masterFoad/vllm:pr-polymorphic-buffers-clean` **Branch URL:** https://gi...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
