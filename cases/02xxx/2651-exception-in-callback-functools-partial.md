# vllm-project/vllm#2651: Exception in callback functools.partial！

| 字段 | 值 |
| --- | --- |
| Issue | [#2651](https://github.com/vllm-project/vllm/issues/2651) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Exception in callback functools.partial！

### Issue 正文摘录

vllm==0.2.2 cuda==12.2 torch==2.1.2 transformers==4.36.2 when using vllm and chatglm2 model, some wrong happend, there are the wrong message.could you please tell me what make this happend and how to avoid this thing. Exception in callback functools.partial( , request_tracker= ) handle: , request_tracker= )> Traceback (most recent call last): File "/home/ubuntu/miniconda3/envs/vllm0.2.2/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish task.result() File "/home/ubuntu/miniconda3/envs/vllm0.2.2/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 350, in run_engine_loop has_requests_in_progress = await self.engine_step() File "/home/ubuntu/miniconda3/envs/vllm0.2.2/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 329, in engine_step request_outputs = await self.engine.step_async() File "/home/ubuntu/miniconda3/envs/vllm0.2.2/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 191, in step_async output = await self._run_workers_async( File "/home/ubuntu/miniconda3/envs/vllm0.2.2/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 219, in _run_workers_async all_output...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: _engine.py", line 219, in _run_workers_async all_outputs = await asyncio.gather(*coros) File "/home/ubuntu/miniconda3/envs/vllm0.2.2/lib/python3.10/concurrent/futures/thread.py", line 58, in run result = self.fn(*self.a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Exception in callback functools.partial！ vllm==0.2.2 cuda==12.2 torch==2.1.2 transformers==4.36.2 when using vllm and chatglm2 model, some wrong happend, there are the wrong message.could you please tell me what make th...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: frontend_api;model_support;sampling_logits cuda;kernel build_error;crash;mismatch env_dependency vllm==0.2.2
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. The above exception was the direct cause of the following exceptio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: da==12.2 torch==2.1.2 transformers==4.36.2 when using vllm and chatglm2 model, some wrong happend, there are the wrong message.could you please tell me what make this happend and how to avoid this thing. Exception in ca...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
