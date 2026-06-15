# vllm-project/vllm#36755: [Bug] Preemption + async scheduling race can corrupt prompt-token accounting and crash Prometheus counters

| 字段 | 值 |
| --- | --- |
| Issue | [#36755](https://github.com/vllm-project/vllm/issues/36755) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] Preemption + async scheduling race can corrupt prompt-token accounting and crash Prometheus counters

### Issue 正文摘录

### Current environment - vLLM V1 engine - local checkout: `v0.17.0rc0-134-g58928475e` - KV connector in use (`PegaKVConnector`) - 8 workers - model: Qwen3-8B - block size: 64 - async scheduling enabled in the failing configuration ### Describe the bug Under load, workers crash with: ```text ValueError: Counters can only be incremented by non-negative amounts. ``` Crash path: ```text output_handler -> PrometheusStatLogger.record() -> counter_prompt_tokens_by_source["local_cache_hit"].inc(...) -> ValueError -> propagate_error() -> all in-flight streaming requests return 500 ``` ### Findings There appear to be **two related problems**. #### 1. Preemption state reset is incomplete `_preempt_request()` resets `request.num_computed_tokens = 0` but does not reset `request.num_cached_tokens`. Without resetting `num_cached_tokens`, a resumed request can recompute / requery external KV state with a fresh `num_external_computed_tokens`, while `num_cached_tokens` still holds an older pre-preemption value. This can make prompt-token source accounting inconsistent and can produce negative values for `local_cache_hit`. A minimal fix for this part is: ```python # scheduler.py::_preempt_request()...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: -134-g58928475e` - KV connector in use (`PegaKVConnector`) - 8 workers - model: Qwen3-8B - block size: 64 - async scheduling enabled in the failing configuration ### Describe the bug Under load, workers crash with: ```t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ].inc(...) -> ValueError -> propagate_error() -> all in-flight streaming requests return 500 ``` ### Findings There appear to be **two related problems**. #### 1. Preemption state reset is incomplete `_preempt_request()...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: KV connector in use (`PegaKVConnector`) - 8 workers - model: Qwen3-8B - block size: 64 - async scheduling enabled in the failing configuration ### Describe the bug Under load, workers crash with: ```text ValueError: Cou...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Request state**, not a **schedule-time snapshot**. ### Root cause The deterministic root cause appears to be: > `update_from_output()` / `EngineCoreOutput(...)` reads mutable fields from `Request` at output-materializat...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Request state**, not a **schedule-time snapshot**. ### Root cause The deterministic root cause appears to be: > `update_from_output()` / `EngineCoreOutput(...)` reads mutable fields from `Request` at output-materializat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
