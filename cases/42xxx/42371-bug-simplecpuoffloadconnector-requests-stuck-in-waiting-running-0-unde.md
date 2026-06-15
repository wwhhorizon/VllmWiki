# vllm-project/vllm#42371: [Bug]: SimpleCPUOffloadConnector: requests stuck in Waiting (Running=0) under sustained load / CPU offload

| 字段 | 值 |
| --- | --- |
| Issue | [#42371](https://github.com/vllm-project/vllm/issues/42371) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SimpleCPUOffloadConnector: requests stuck in Waiting (Running=0) under sustained load / CPU offload

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Summary When serving Qwen3_5-35B-A3B with SimpleCPUOffloadConnector, hybrid KV cache manager enabled, prefix caching, and chunked prefill, the engine initially processes concurrent /v1/chat/completions successfully, then transitions to a state where Running: 0 and Waiting: N (e.g. 50) with zero prompt/generation throughput, while HTTP requests may still return 200 OK. GPU KV cache usage drops to 0%. This appears correlated with CPU KV offload / cache pressure (large cpu_bytes_to_use). Environment vLLM: 0.20.2rc1.dev129+g1acd67a79 (or your exact commit / wheel) Model: Qwen3_5-35B-A3B (local path), --language-model-only Hardware: 2× GPU (e.g. H20), tensor_parallel_size=2 OS / CUDA / PyTorch: (fill in) Configuration (minimal repro sketch) Approximate CLI (align with your deployment): vllm serve \ --tensor-parallel-size 2 \ --language-model-only \ --enable-prefix-caching \ --gpu-memory-utilization 0.85 \ --kv-transfer-config '{"kv_connector":"SimpleCPUOffloadConnector","kv_role":"kv_both","kv_connector_extra_config":{"cpu_bytes_to_use":137438953472}}' \ --no-disable-hybrid-kv-cache-manager \ --block-size 16 \ --max-model-len 128000 \...

## 现有链接修复摘要

#42568 Fix async KV loads counting toward scheduler request limit

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: SimpleCPUOffloadConnector: requests stuck in Waiting (Running=0) under sustained load / CPU offload bug ### Your current environment ### 🐛 Describe the bug Summary When serving Qwen3_5-35B-A3B with SimpleCPUOfflo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: . Environment vLLM: 0.20.2rc1.dev129+g1acd67a79 (or your exact commit / wheel) Model: Qwen3_5-35B-A3B (local path), --language-model-only Hardware: 2× GPU (e.g. H20), tensor_parallel_size=2 OS / CUDA / PyTorch: (fill in...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: SimpleCPUOffloadConnector: requests stuck in Waiting (Running=0) under sustained load / CPU offload bug ### Your current environment ### 🐛 Describe the bug Summary When serving Qwen3_5-35B-A3B with SimpleCPUOfflo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: our current environment ### 🐛 Describe the bug Summary When serving Qwen3_5-35B-A3B with SimpleCPUOffloadConnector, hybrid KV cache manager enabled, prefix caching, and chunked prefill, the engine initially processes co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: uage-model-only Hardware: 2× GPU (e.g. H20), tensor_parallel_size=2 OS / CUDA / PyTorch: (fill in) Configuration (minimal repro sketch) Approximate CLI (align with your deployment): vllm serve \ --tensor-parallel-size 2...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42568](https://github.com/vllm-project/vllm/pull/42568) | closes_keyword | 0.95 | Fix async KV loads counting toward scheduler request limit | Fixes #42371. Async KV-load requests enter `WAITING_FOR_REMOTE_KVS` and live in `skipped_waiting` while the transfer is in progress. They are not in `running`, but they have alr |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
