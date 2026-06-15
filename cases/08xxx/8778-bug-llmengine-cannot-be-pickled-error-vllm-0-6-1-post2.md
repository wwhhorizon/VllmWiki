# vllm-project/vllm#8778: [Bug]: LLMEngine cannot be pickled error vllm 0.6.1.post2

| 字段 | 值 |
| --- | --- |
| Issue | [#8778](https://github.com/vllm-project/vllm/issues/8778) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | gemm_linear;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLMEngine cannot be pickled error vllm 0.6.1.post2

### Issue 正文摘录

### Your current environment ### Model Input Dumps model="Qwen/Qwen2.5-72B-Instruct" guided_decoding_backend="outlines" vllm_command_flags={ "--gpu-memory-utilization": 0.99, "--max-num-seqs": 64, } max_model_len=8192, library_overrides={ "vllm": "vllm==0.6.1.post2", } ### 🐛 Describe the bug ``` ERROR 09-24 16:06:51 async_llm_engine.py:58] Engine background task failed ERROR 09-24 16:06:51 async_llm_engine.py:58] Traceback (most recent call last): ERROR 09-24 16:06:51 async_llm_engine.py:58] File "/local_disk0/.ephemeral_nfs/envs/pythonEnv-0b16fcdd-4fa2-42af-bf13-918419d0b49a/lib/python3.11/site-packages/vllm/worker/model_runner_base.py", line 112, in _wrapper ERROR 09-24 16:06:51 async_llm_engine.py:58] return func(*args, **kwargs) ERROR 09-24 16:06:51 async_llm_engine.py:58] ^^^^^^^^^^^^^^^^^^^^^ ERROR 09-24 16:06:51 async_llm_engine.py:58] File "/local_disk0/.ephemeral_nfs/envs/pythonEnv-0b16fcdd-4fa2-42af-bf13-918419d0b49a/lib/python3.11/site-packages/vllm/worker/model_runner.py", line 1546, in execute_model ERROR 09-24 16:06:51 async_llm_engine.py:58] hidden_or_intermediate_states = model_executable( ERROR 09-24 16:06:51 async_llm_engine.py:58] ^^^^^^^^^^^^^^^^^ ERROR 09-24 1...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ^^^^^^^^^^^^^ ERROR 09-24 16:06:51 async_llm_engine.py:58] RuntimeError: CUDA error: CUBLAS_STATUS_ALLOC_FAILED when calling `cublasCreate(handle)` ERROR 09-24 16:06:51 async_llm_engine.py:58] ERROR 09-24 16:06:51 async...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ed error vllm 0.6.1.post2 bug;stale ### Your current environment ### Model Input Dumps model="Qwen/Qwen2.5-72B-Instruct" guided_decoding_backend="outlines" vllm_command_flags={ "--gpu-memory-utilization": 0.99, "--max-n...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: LLMEngine cannot be pickled error vllm 0.6.1.post2 bug;stale ### Your current environment ### Model Input Dumps model="Qwen/Qwen2.5-72B-Instruct" guided_decoding_backend="outlines" vllm_command_flags={ "--gpu-mem...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ### Model Input Dumps model="Qwen/Qwen2.5-72B-Instruct" guided_decoding_backend="outlines" vllm_command_flags={ "--gpu-memory-utilization": 0.99, "--max-num-seqs": 64, } max_model_len=8192, library_overrides={ "vllm": "...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ly asked questions. performance gemm_linear;model_support cuda crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
