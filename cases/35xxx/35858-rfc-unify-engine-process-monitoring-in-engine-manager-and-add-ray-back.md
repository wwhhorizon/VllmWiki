# vllm-project/vllm#35858: [RFC]: Unify engine process monitoring in engine manager and add Ray backend support

| 字段 | 值 |
| --- | --- |
| Issue | [#35858](https://github.com/vllm-project/vllm/issues/35858) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Unify engine process monitoring in engine manager and add Ray backend support

### Issue 正文摘录

### Motivation. vLLM currently monitors the liveness of engine core processes, and executes shutdown logic when an engine process exits or becomes dead. However, the implementation is different across different launch modes, and the engine liveness monitoring logic is implemented in multiple places: 1. `start_engine_core_monitor` in class `MPClient` at `vllm/v1/engine/core_client.py` 2. `join_first` in class `CoreEngineProcManager` at `vllm/v1/engine/utils.py` (mainly for headless mode) 3. `wait_for_completion_or_failure` in `vllm/v1/utils.py` (mainly for multi_api_server mode) This scattered implementation leads to inconsistent logging and incomplete support in some execution paths: - **Data-parallel mode with `data-parallel-backend=ray`**: Engine liveness monitoring is not implemented. Killing an engine core process does not trigger vLLM shutdown, and the inference service can hang indefinitely. - **Headless mode**: Engine process exits do not provide clear additional logs or structured handling. Furthermore, **to support elastic EP scale-down**, we want to handle some engine process exits gracefully without immediately shutting down vLLM, allowing for additional recovery or fal...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: at `vllm/v1/engine/core_client.py` 2. `join_first` in class `CoreEngineProcManager` at `vllm/v1/engine/utils.py` (mainly for headless mode) 3. `wait_for_completion_or_failure` in `vllm/v1/utils.py` (mainly for multi_api...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [RFC]: Unify engine process monitoring in engine manager and add Ray backend support RFC;stale ### Motivation. vLLM currently monitors the liveness of engine core processes, and executes shutdown logic when an engine pr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: logic into the engine manager, which is used across all launch modes. Specifically: 1. **Centralize engine process monitoring** in `CoreEngineProcManager`, ensuring consistent behavior across different launch modes and...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ional logs or structured handling. Furthermore, **to support elastic EP scale-down**, we want to handle some engine process exits gracefully without immediately shutting down vLLM, allowing for additional recovery or fa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ine process monitoring in engine manager and add Ray backend support RFC;stale ### Motivation. vLLM currently monitors the liveness of engine core processes, and executes shutdown logic when an engine process exits or b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
