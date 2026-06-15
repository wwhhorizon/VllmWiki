# vllm-project/vllm#35104: [Bug]: V1 engine workers die after idle period (SystemError: PyCFunction / EngineDeadError) — TP=2, multiprocessing

| 字段 | 值 |
| --- | --- |
| Issue | [#35104](https://github.com/vllm-project/vllm/issues/35104) |
| 状态 | open |
| 标签 |  |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;moe;quantization |
| 症状 | crash;mismatch |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 engine workers die after idle period (SystemError: PyCFunction / EngineDeadError) — TP=2, multiprocessing

### Issue 正文摘录

### Your current environment ``` vLLM: 0.16.0rc2.dev216+g5bff999d1 Python: 3.12.12 (GCC 11.4.0) PyTorch: 2.10.0+cu129 CUDA: 12.9 FlashInfer: 0.6.3 Driver: 591.74 GPU: 3x NVIDIA GeForce RTX 4090 (using 2 with TP=2) OS: Docker on Windows 11 (Docker Desktop, Linux containers) Multiprocessing start method: fork ``` ### Model [QuantTrio/GLM-4.7-Flash-AWQ](https://huggingface.co/QuantTrio/GLM-4.7-Flash-AWQ) — 31B MoE (64 experts, top-4), AWQ 4-bit, MLA attention ### How to reproduce the error The engine crashes **spontaneously after idle periods** (no active requests). No specific user action is needed — just leave the server running with no incoming traffic. **Reproduction steps:** 1. Start vLLM with TP=2, V1 engine, multiprocessing backend: ```bash vllm serve QuantTrio/GLM-4.7-Flash-AWQ \ --tensor-parallel-size 2 \ --enable-expert-parallel \ --gpu-memory-utilization 0.92 \ --max-model-len 131072 \ --distributed-executor-backend mp \ --tool-call-parser glm47 \ --reasoning-parser glm45 ``` 2. Wait 10 minutes to several hours with **no inference requests** 3. Either: - Send a request → gets `TimeoutError: RPC call to sample_tokens timed out` → `EngineDeadError` - Or the worker process di...

## 现有链接修复摘要

#40303 [Bug] Fix shm_broadcast PyCFunction descriptor corruption under JIT loads

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 3 Driver: 591.74 GPU: 3x NVIDIA GeForce RTX 4090 (using 2 with TP=2) OS: Docker on Windows 11 (Docker Desktop, Linux containers) Multiprocessing start method: fork ``` ### Model [QuantTrio/GLM-4.7-Flash-AWQ](https://hug...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: rc2.dev216+g5bff999d1 Python: 3.12.12 (GCC 11.4.0) PyTorch: 2.10.0+cu129 CUDA: 12.9 FlashInfer: 0.6.3 Driver: 591.74 GPU: 3x NVIDIA GeForce RTX 4090 (using 2 with TP=2) OS: Docker on Windows 11 (Docker Desktop, Linux co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: rror The engine crashes **spontaneously after idle periods** (no active requests). No specific user action is needed — just leave the server running with no incoming traffic. **Reproduction steps:** 1. Start vLLM with T...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: g5bff999d1 Python: 3.12.12 (GCC 11.4.0) PyTorch: 2.10.0+cu129 CUDA: 12.9 FlashInfer: 0.6.3 Driver: 591.74 GPU: 3x NVIDIA GeForce RTX 4090 (using 2 with TP=2) OS: Docker on Windows 11 (Docker Desktop, Linux containers) M...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: AWQ) — 31B MoE (64 experts, top-4), AWQ 4-bit, MLA attention ### How to reproduce the error The engine crashes **spontaneously after idle periods** (no active requests). No specific user action is needed — just leave th...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40303](https://github.com/vllm-project/vllm/pull/40303) | closes_keyword | 0.95 | [Bug] Fix shm_broadcast PyCFunction descriptor corruption under JIT loads | Fixes #35104. Replaces the `with _memory_fence_lock:` (threading.Lock) memory barrier in [`shm_broadcast.memory_fence()`](https://github.com/vllm-project/vllm/blob/main/vllm/distr |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
