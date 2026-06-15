# vllm-project/vllm#8100: [Bug]: When use `guided choice` feature, vllm.engine.async_llm_engine.AsyncEngineDeadError

| 字段 | 值 |
| --- | --- |
| Issue | [#8100](https://github.com/vllm-project/vllm/issues/8100) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When use `guided choice` feature, vllm.engine.async_llm_engine.AsyncEngineDeadError

### Issue 正文摘录

### Your current environment ```text ERROR:asyncio:Exception in callback functools.partial( , error_ca llback= >) handle: , error_callback= >)> Traceback (most recent call last): File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 40, in _raise_ex ception_on_finish task.result() File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 521, in run_engi ne_loop has_requests_in_progress = await asyncio.wait_for( ^^^^^^^^^^^^^^^^^^^^^^^ File "/data/tangjiakai/anaconda3/lib/python3.11/asyncio/tasks.py", line 479, in wait_for return fut.result() ^^^^^^^^^^^^ File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 495, in engine_s tep request_outputs = await self.engine.step_async() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 226, in step_asy nc output = await self.model_executor.execute_model_async( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/vllm/executor/gpu_executor.py", line 117, in execute_mo del...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ngineDeadError bug;stale ### Your current environment ```text ERROR:asyncio:Exception in callback functools.partial( , error_ca llback= >) handle: , error_callback= >)> Traceback (most recent call last): File "/data/tan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ocessor.py", line 5 5, in forward logits *= self.scale RuntimeError: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace bel...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: | File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 680, in __aexit_ _ | raise BaseExceptionGroup( | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception) +-+--...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: tor/layers/logits_processor.py", line 5 5, in forward logits *= self.scale RuntimeError: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, s...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/tangjiakai/anaconda3/lib/python3.11/site-packages/torch/utils/_cont...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
