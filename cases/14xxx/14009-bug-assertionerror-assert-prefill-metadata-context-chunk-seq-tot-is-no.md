# vllm-project/vllm#14009: [Bug]: AssertionError, assert prefill_metadata.context_chunk_seq_tot is not None

| 字段 | 值 |
| --- | --- |
| Issue | [#14009](https://github.com/vllm-project/vllm/issues/14009) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AssertionError, assert prefill_metadata.context_chunk_seq_tot is not None

### Issue 正文摘录

### Your current environment - L20 x 3, 72 GPUs - TP=8, PP=3 - vLLM commit: 811a46bf06f872c28147f957b3a9d18d97d1c1ad - DeepSeek-R1 ### 🐛 Describe the bug ```bash [2025-02-27 21:37:38,998] [ERROR] [MainThread] [asyncio] >>> Exception in callback functools.partial( , error_callback= >) handle: , error_callback= >)> Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 58, in _log_task_completion return_value = task.result() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 825, in run_engine_loop result = task.result() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 748, in engine_step request_outputs = await self.engine.step_async(virtual_engine) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 353, in step_async outputs = await self.model_executor.execute_model_async( File "/usr/local/lib/python3.10/dist-packages/vllm/executor/ray_distributed_executor.py", line 591, in execute_model_async return await super().execute_model_async(execute_model_req) File "/usr/local/lib/python3.10/dist-packages/vllm/executor/exe...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: AssertionError, assert prefill_metadata.context_chunk_seq_tot is not None bug ### Your current environment - L20 x 3, 72 GPUs - TP=8, PP=3 - vLLM commit: 811a46bf06f872c28147f957b3a9d18d97d1c1ad - DeepSeek-R1 ###...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: AssertionError, assert prefill_metadata.context_chunk_seq_tot is not None bug ### Your current environment - L20 x 3, 72 GPUs - TP=8, PP=3 - vLLM commit: 811a46bf06f872c28147f957b3a9d18d97d1c1ad - DeepSeek-R1 ###...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: metadata) File "/usr/local/lib/python3.10/dist-packages/vllm/attention/backends/mla/common.py", line 1513, in forward output[:num_prefill_tokens] =*** File "/usr/local/lib/python3.10/dist-packages/vllm/attention/backend...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ibe the bug ```bash [2025-02-27 21:37:38,998] [ERROR] [MainThread] [asyncio] >>> Exception in callback functools.partial( , error_callback= >) handle: , error_callback= >)> Traceback (most recent call last): File "/usr/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
