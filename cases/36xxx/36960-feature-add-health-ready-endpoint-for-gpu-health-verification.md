# vllm-project/vllm#36960: [Feature]: Add /health/ready endpoint for GPU health verification

| 字段 | 值 |
| --- | --- |
| Issue | [#36960](https://github.com/vllm-project/vllm/issues/36960) |
| 状态 | open |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: Add /health/ready endpoint for GPU health verification

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **Problem**: vLLM's current `/health` endpoint only checks whether the engine process is alive (`engine_dead` boolean). When a GPU encounters a page fault or illegal memory access, the process remains alive but inference becomes impossible. The `/health` endpoint continues returning 200, causing Kubernetes to route traffic to a broken pod. I hit this exact scenario in production — GPU page fault / illegal memory access made inference fail, but the vLLM process itself was still running. K8s liveness probe passed, so traffic kept flowing to a pod that couldn't actually serve requests. **Solution**: Add a `/health/ready` endpoint that runs an actual GPU forward pass (1-token dummy batch) to verify the GPU can execute inference end-to-end. This aligns with K8s liveness/readiness probe separation: - `/health` → liveness (existing, process-level boolean check) - `/health/ready` → readiness (new, GPU forward pass verification) **Key design decisions:** - Reuses existing `execute_dummy_batch_async()` which calls `_dummy_run(1, uniform_decode=True)` — no new GPU code needed - Uses the `call_utility_async()` path (not the scheduler's request queue), s...

## 现有链接修复摘要

#1154 Allocate more shared memory to attention kernel

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: be passed, so traffic kept flowing to a pod that couldn't actually serve requests. **Solution**: Add a `/health/ready` endpoint that runs an actual GPU forward pass (1-token dummy batch) to verify the GPU can execute in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: /ready` → readiness (new, GPU forward pass verification) **Key design decisions:** - Reuses existing `execute_dummy_batch_async()` which calls `_dummy_run(1, uniform_decode=True)` — no new GPU code needed - Uses the `ca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ct/sglang#8444, sgl-project/sglang#8757, sgl-project/sglang#13320). 3. **CUDA error detection via signal handlers** — More invasive, doesn't catch all failure modes (e.g., driver-level hangs). ### Additional context - K...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: hrough the scheduler queue, competes with real requests, and can cause false timeouts under load. SGLang had to add multiple workarounds for this (PRs sgl-project/sglang#8444, sgl-project/sglang#8757, sgl-project/sglang...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ), so it doesn't compete with normal inference requests for scheduling - Configurable timeout via `VLLM_HEALTH_CHECK_GPU_TIMEOUT` env var (default 20s) - No breaking changes — existing `/health` is untouched **Prior art...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#1154](https://github.com/vllm-project/vllm/pull/1154) | mentioned | 0.45 | Allocate more shared memory to attention kernel | timeoutseconds: 25 ``` - sglang references: sgl-project/sglang#853, sgl-project/sglang#1154, sgl-project/sglang#8444, sgl-project/sglang#13320 - i have a draft pr ready for this f… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
