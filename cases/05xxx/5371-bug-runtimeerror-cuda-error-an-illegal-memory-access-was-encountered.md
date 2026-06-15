# vllm-project/vllm#5371: [Bug]: RuntimeError: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#5371](https://github.com/vllm-project/vllm/issues/5371) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;kernel |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` vllm 0.4.3 rtx4090 driver 555.99 ### 🐛 Describe the bug `2024-06-10 13:26:25 Exception in callback functools.partial( , error_callback= >) 2024-06-10 13:26:25 handle: , error_callback= >)> 2024-06-10 13:26:25 Traceback (most recent call last): 2024-06-10 13:26:25 File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 40, in _raise_exception_on_finish 2024-06-10 13:26:25 task.result() 2024-06-10 13:26:25 File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 521, in run_engine_loop 2024-06-10 13:26:25 has_requests_in_progress = await asyncio.wait_for( 2024-06-10 13:26:25 File "/usr/lib/python3.10/asyncio/tasks.py", line 445, in wait_for 2024-06-10 13:26:25 return fut.result() 2024-06-10 13:26:25 File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 495, in engine_step 2024-06-10 13:26:25 request_outputs = await self.engine.step_async() 2024-06-10 13:26:25 File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 226, in step_async 2024-06-10 13:26:25 output = await self.model_executor.exe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: engine_loop 2024-06-10 13:26:25 has_requests_in_progress = await asyncio.wait_for( 2024-06-10 13:26:25 File "/usr/lib/python3.10/asyncio/tasks.py", line 445, in wait_for 2024-06-10 13:26:25 return fut.result() 2024-06-1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RuntimeError: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` vllm 0.4.3 rtx4090 driver 555.99 ### 🐛 Describe the bug...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 24-06-10 13:26:25 output = self.model_runner.execute_model(seq_group_metadata_list, 2024-06-10 13:26:25 File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context 2024-06-10...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: py", line 226, in step_async 2024-06-10 13:26:25 output = await self.model_executor.execute_model_async( 2024-06-10 13:26:25 File "/usr/local/lib/python3.10/dist-packages/vllm/executor/gpu_executor.py", line 117, in exe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : RuntimeError: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` vllm 0.4.3 rtx4090 driver 555.99 ### 🐛 Describe the bug `2024...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
