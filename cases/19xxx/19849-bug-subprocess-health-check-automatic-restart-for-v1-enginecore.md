# vllm-project/vllm#19849: [Bug]: Subprocess health check / automatic restart for V1 EngineCore

| 字段 | 值 |
| --- | --- |
| Issue | [#19849](https://github.com/vllm-project/vllm/issues/19849) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Subprocess health check / automatic restart for V1 EngineCore

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I’ve been experimenting with the new V1 engine in vLLM because of its impressive speed and much lower memory usage compared to V0. I understand that V1 is still experimental, but these performance gains are exactly what I need. Unfortunately, there’s a blocker that’s making it effectively unusable for me right now. --- ### What’s happening When I spin up an `AsyncLLMEngine`, vLLM correctly launches a separate `EngineCore` subprocess. However, if that subprocess crashes (OOM, segfault, manual kill, etc.), the parent process never notices. The built-in health check is literally: ```python async def check_health(self) -> None: logger.debug("Called check_health.") ``` So it just returns immediately and keeps sending RPCs to a dead socket. No errors, no restart—just a silent hang. Additionally, if the **parent process** itself restarts (for example, due to an orchestrator reboot or code reload), the **EngineCore** process sometimes remains alive, continues to hold GPU memory, and blocks any subsequent vLLM restart because the memory cannot be reclaimed. --- ### Expected behavior 1. A crash or unexpected exit of the `EngineCore` subpro...

## 现有链接修复摘要

#36451 [CORE][V1] fix: alive-but-hung EngineCore not being detected by `/health` endpoint. | #40935 [V1][Bugfix] Reap EngineCore on parent death (#19849)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: w ones. --- ### Questions / Request for guidance 1. **Is there an officially recommended way** to health-check or automatically restart a dead V1 `EngineCore`? 2. **Would it make sense for vLLM** to expose a built-in wa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Subprocess health check / automatic restart for V1 EngineCore bug;stale ### Your current environment ### 🐛 Describe the bug I’ve been experimenting with the new V1 engine in vLLM because of its impressive speed a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ce! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: a separate `EngineCore` subprocess. However, if that subprocess crashes (OOM, segfault, manual kill, etc.), the parent process never notices. The built-in health check is literally: ```python async def check_health(self...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf;oom env_dependency #36451 [CORE][V1] fix: alive-but-hung EngineCore not being detected by `/health` endpoint. | #...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36451](https://github.com/vllm-project/vllm/pull/36451) | mentioned | 0.6 | [CORE][V1] fix: alive-but-hung EngineCore not being detected by `/health` endpoint. | DeadError</code> → <code>/health</code> returns 503.</p> <p>Addresses #19849. Related: #24910</p> <p><strong>Config:</strong></p> <ul> <li><code>VLLM_HEALTH_CHECK_TIMEOUT</code> (… |
| [#40935](https://github.com/vllm-project/vllm/pull/40935) | closes_keyword | 0.95 | [V1][Bugfix] Reap EngineCore on parent death (#19849) | fix the no-op `engine.check_health()` in #19849 example 1. The watchdog fixes example 2 (orphaned child after parent dies). AI assistance was used in drafting this PR. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
