# vllm-project/vllm#13252: [Bug]: Using VLLM0.7.2 server to start DeepSeek-r1-awq model, there is a phenomenon of cuda out of memory and service shutting down.

| 字段 | 值 |
| --- | --- |
| Issue | [#13252](https://github.com/vllm-project/vllm/issues/13252) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using VLLM0.7.2 server to start DeepSeek-r1-awq model, there is a phenomenon of cuda out of memory and service shutting down.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None. INFO 02-14 08:44:26 engine.py:275] Added request chatcmpl-4fb99a59-2bdd-455f-97b8-99b8908e83de. INFO:172.16.18.69:52036- "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error CRITICAL 02-14 08:44:33 launcher.py:101] MQLLMEngine is already dead, terminating server process (VllmWorkerProcess pid=614) ERROR 02-14 08:44:33 multiproc_worker_utils.py:242] Exception in worker VllmWorkerProcess while processing method start_worker_execution_loop. (VllmWorkerProcess pid=614) ERROR 02-14 08:44:33 multiproc_worker_utils.py:242] Traceback (most recent call last): (VllmWorkerProcess pid=614)ERROR 02-14 08:44:33 multiproc_worker_utils.py:242]File "/opt/conda/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 236, in_run_worker_process (VllmWorkerProcess pid=614)ERROR 02-14 08:44:33 multiproc_worker_utils.py:242] output = run_method(worker, method, args, kwargs) (VllmWorkerProcess pid=614)ERROR 02-14 08:44:33 multiproc_worker_utils.py:242]File"/opt/conda/lib/python3.10/site-packages/vllm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: yTorch,with 76.00 MiB Tried to allocate 84.00 MiB. GPU 0 has a total capacity of 79.15 GiB of which 75.25MiB is free.Process 2193685 allocated in private pools (e.g.,CUDA Graphs), and 63.67 MiB is reserved by PyTorch bu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ere is a phenomenon of cuda out of memory and service shutting down. bug;stale ### Your current environment ### 🐛 Describe the bug truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory cuda;quantization crash;oom dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: LLM0.7.2 server to start DeepSeek-r1-awq model, there is a phenomenon of cuda out of memory and service shutting down. bug;stale ### Your current environment ### 🐛 Describe the bug truncate_prompt_tokens=None, guided_de...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: _api;model_support;quantization;scheduler_memory cuda;quantization crash;oom dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
