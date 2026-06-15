# vllm-project/vllm#1001: AsyncEngineDeadError / RuntimeError: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#1001](https://github.com/vllm-project/vllm/issues/1001) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AsyncEngineDeadError / RuntimeError: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

While serving the CodeLLaMA 13B （`CodeLlama-13b-hf`) base model with `v1/completions` API with 1 A100, I encountered the following CUDA memory issue. The same thing happened with the 34B base model, too (`CodeLlama-34b-hf`). However, I did not encounter such an issue with any of the CodeLlama instruct series (with the same starting config). To make it easier to debug, I attached the complete log [here](https://uofi.box.com/s/3smovitftkk780v7xnoo827ym2oiayka) (it is too big, so i have to upload it somewhere else). The error log: ``` INFO 09-09 08:20:08 async_llm_engine.py:120] Aborted request cmpl-223dc522668143dfb7db9b23988ec0a1. INFO: 127.0.0.1:34054 - "POST /v1/completions HTTP/1.1" 500 Internal Server Error Exception in callback _raise_exception_on_finish(request_tracker= )( ) at /usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py:21 handle: )( ) at /usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py:21> Traceback (most recent call last): File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 27, in _raise_exception_on_finish task.result() File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ght be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. The above exception was the direct cause of the following exception: Traceback...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: DA error: an illegal memory access was encountered While serving the CodeLLaMA 13B （`CodeLlama-13b-hf`) base model with `v1/completions` API with 1 A100, I encountered the following CUDA memory issue. The same thing hap...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: AsyncEngineDeadError / RuntimeError: CUDA error: an illegal memory access was encountered While serving the CodeLLaMA 13B （`CodeLlama-13b-hf`) base model with `v1/completions` API with 1 A100, I encountered the followin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 780v7xnoo827ym2oiayka) (it is too big, so i have to upload it somewhere else). The error log: ``` INFO 09-09 08:20:08 async_llm_engine.py:120] Aborted request cmpl-223dc522668143dfb7db9b23988ec0a1. INFO: 127.0.0.1:34054...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line 718, in __call__ await route.handle(scope, receive, send) File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
