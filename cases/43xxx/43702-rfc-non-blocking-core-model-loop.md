# vllm-project/vllm#43702: [RFC]: Non-blocking core model loop

| 字段 | 值 |
| --- | --- |
| Issue | [#43702](https://github.com/vllm-project/vllm/issues/43702) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Non-blocking core model loop

### Issue 正文摘录

# Motivation The vLLM core engine process today **blocks** whenever it has no active requests. The non-DP loop ends up parked in `multiprocessing.Queue.get(block=True)`. In the DP case the wake-up is staged through a dedicated `DPCoordinator` process that broadcasts messages to bring all ranks out of their idle state together. ```python # vllm/v1/engine/core.py - current non-DP busy loop def run_busy_loop(self): while self._handle_shutdown(): # 1) Poll the input queue until there is work to do. self._process_input_queue() # blocks on input_queue.get(block=True) # 2) Step the engine core and return the outputs. self._process_engine_step() ``` The blocking model has worked well, but it has accumulated meaningful cost: ## Limitations of the current design ### 1. Multiplexing more than one wake-up source is awkward The engine needs to react to more than just new requests: `DPCoordinator` wave messages, KV-connector completion / failure events, FSM/grammar compilation futures, and future signals like async weight updates and elastic-EP changes. Today these are multiplexed via a background ZMQ-poller thread that feeds an in-process `Queue` the main thread blocks on. It works, but every...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: The vLLM core engine process today **blocks** whenever it has no active requests. The non-DP loop ends up parked in `multiprocessing.Queue.get(block=True)`. In the DP case the wake-up is staged through a dedicated `DPCo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: _IDLE_SLEEP_MS`, default `0`). The same lever applies to workers: when `dispatch_cg_and_sync_dp` (V2) or `coordinate_batch_across_dp` (V1, if adapted) returns the all-zero descriptor, the model runner sleeps for the con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: DPCoordinator` wave messages, KV-connector completion / failure events, FSM/grammar compilation futures, and future signals like async weight updates and elastic-EP changes. Today these are multiplexed via a background...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: Non-blocking core model loop RFC # Motivation The vLLM core engine process today **blocks** whenever it has no active requests. The non-DP loop ends up parked in `multiprocessing.Queue.get(block=True)`. In the DP...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: he XPUB/XSUB coordinator engine fabric goes away. * **Lower cold-request latency in DP deployments.** One fewer process and IPC hop on the request path. * **Uniform code path for non-DP and DP.** The two `run_busy_loop`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
