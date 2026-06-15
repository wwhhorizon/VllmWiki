# vllm-project/vllm#3341: Bug when input top_k as a float that is outside of range

| 字段 | 值 |
| --- | --- |
| Issue | [#3341](https://github.com/vllm-project/vllm/issues/3341) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Bug when input top_k as a float that is outside of range

### Issue 正文摘录

Hello, I found a small bug which takes me the whole morning to deal with. If we accidentally send a request with top_k = .01 for some float, the request will fail, which is obvious. However, this request will crash the whole server so that every subsequent requests even with correct top_k will not be served, I need to manually restart the server. It is possible ensure the input data in correct type and so on, however, it must be nice when the server is in this crashed stage it send some thing to supervisord to be rebooted. This happened in vllm: 0.3.3 and 0.3.2 nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2023 NVIDIA Corporation Built on Mon_Apr__3_17:16:06_PDT_2023 Cuda compilation tools, release 12.1, V12.1.105 Build cuda_12.1.r12.1/compiler.32688072_0 Traceback (most recent call last): File "uvloop/cbhandles.pyx", line 63, in uvloop.loop.Handle._run File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 38, in _raise_exception_on_finish raise exc File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 33, in _raise_exception_on_finish raise AsyncEngineDeadError( vllm.engine.async_llm_engine.AsyncEngineDeadErro...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: found a small bug which takes me the whole morning to deal with. If we accidentally send a request with top_k = .01 for some float, the request will fail, which is obvious. However, this request will crash the whole ser...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/usr/local/lib/python3.8/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) Fil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n input top_k as a float that is outside of range stale Hello, I found a small bug which takes me the whole morning to deal with. If we accidentally send a request with top_k = .01 for some float, the request will fail,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Bug when input top_k as a float that is outside of range stale Hello, I found a small bug which takes me the whole morning to deal with. If we accidentally send a request with top_k = .01 for some float, the request wil...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: eceive, sender) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line 758, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
