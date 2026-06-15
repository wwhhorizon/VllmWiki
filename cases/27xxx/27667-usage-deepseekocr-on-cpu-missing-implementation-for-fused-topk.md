# vllm-project/vllm#27667: [Usage]: DeepseekOCR on CPU missing implementation for fused_topk

| 字段 | 值 |
| --- | --- |
| Issue | [#27667](https://github.com/vllm-project/vllm/issues/27667) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: DeepseekOCR on CPU missing implementation for fused_topk

### Issue 正文摘录

### Your current environment Try to test if it is possible to run DeepseekOCR on CPU using current git main branch. Fails because there is no implementation of `fused_topk` for CPU. ``` INFO 10-28 15:41:18 [v1/worker/cpu_model_runner.py:77] Warming up model for the compilation... ERROR: Traceback (most recent call last): File "/opt/venv/lib/python3.12/site-packages/starlette/routing.py", line 677, in lifespan async with self.lifespan_context(app) as maybe_state: ^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/venv/lib/python3.12/site-packages/starlette/routing.py", line 566, in __aenter__ await self._router.startup() File "/opt/venv/lib/python3.12/site-packages/starlette/routing.py", line 654, in startup await handler() File "/app/start_server.py", line 161, in startup_event initialize_model() File "/app/start_server.py", line 84, in initialize_model llm = LLM( ^^^^ File "/opt/venv/lib/python3.12/site-packages/vllm/entrypoints/llm.py", line 336, in __init__ self.llm_engine = LLMEngine.from_engine_args( ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/venv/lib/python3.12/site-packages/vllm/v1/engine/llm_engine.py", line 188, in from_engine_args return cls( ^^^^ File "/opt/venv/lib/python3.12/site-pack...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Usage]: DeepseekOCR on CPU missing implementation for fused_topk usage;stale ### Your current environment Try to test if it is possible to run DeepseekOCR on CPU using current git main branch. Fails because there is no...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ent call last): File "/opt/venv/lib/python3.12/site-packages/starlette/routing.py", line 677, in lifespan async with self.lifespan_context(app) as maybe_state: ^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/venv/lib/python3.12/s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ntation of `fused_topk` for CPU. ``` INFO 10-28 15:41:18 [v1/worker/cpu_model_runner.py:77] Warming up model for the compilation... ERROR: Traceback (most recent call last): File "/opt/venv/lib/python3.12/site-packages/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: stract.py", line 113, in initialize_from_config self.collective_rpc("compile_or_warm_up_model") File "/opt/venv/lib/python3.12/site-packages/vllm/v1/executor/uniproc_executor.py", line 73, in collective_rpc return [run_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: PU. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
