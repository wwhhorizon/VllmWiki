# vllm-project/vllm#2271: Error during inference with Mixtral 7bx8 GPTQ

| 字段 | 值 |
| --- | --- |
| Issue | [#2271](https://github.com/vllm-project/vllm/issues/2271) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error during inference with Mixtral 7bx8 GPTQ

### Issue 正文摘录

Traceback (most recent call last): File "/home/marco/Scrivania/TESI/serving/vllm/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish task.result() File "/home/marco/Scrivania/TESI/serving/vllm/vllm/engine/async_llm_engine.py", line 359, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/home/marco/Scrivania/TESI/serving/vllm/vllm/engine/async_llm_engine.py", line 338, in engine_step request_outputs = await self.engine.step_async() File "/home/marco/Scrivania/TESI/serving/vllm/vllm/engine/async_llm_engine.py", line 199, in step_async return self._process_model_outputs(output, scheduler_outputs) + ignored File "/home/marco/Scrivania/TESI/serving/vllm/vllm/engine/llm_engine.py", line 562, in _process_model_outputs self._process_sequence_group_outputs(seq_group, outputs) File "/home/marco/Scrivania/TESI/serving/vllm/vllm/engine/llm_engine.py", line 554, in _process_sequence_group_outputs self.scheduler.free_seq(seq) File "/home/marco/Scrivania/TESI/serving/vllm/vllm/core/scheduler.py", line 312, in free_seq self.block_manager.free(seq) File "/home/marco/Scrivania/TESI/serving/vllm/vllm/core/block_manager.py", line 277, in free self._free...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tte/middleware/base.py", line 108, in __call__ response = await self.dispatch_func(request, call_next) File "/home/marco/Scrivania/TESI/serving/vllm_server.py", line 63, in add_cors_header response = await call_next(req...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: m/vllm/engine/async_llm_engine.py", line 359, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/home/marco/Scrivania/TESI/serving/vllm/vllm/engine/async_llm_engine.py", line 338, in engine_st...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ESI/serving/vllm/vllm/core/scheduler.py", line 312, in free_seq self.block_manager.free(seq) File "/home/marco/Scrivania/TESI/serving/vllm/vllm/core/block_manager.py", line 277, in free self._free_block_table(block_tabl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e/async_llm_engine.py", line 199, in step_async return self._process_model_outputs(output, scheduler_outputs) + ignored File "/home/marco/Scrivania/TESI/serving/vllm/vllm/engine/llm_engine.py", line 562, in _process_mod...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ome/marco/miniconda3/envs/serving/lib/python3.10/site-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/home/marco/miniconda3/envs/serving/lib/python3.10/site-packages...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
