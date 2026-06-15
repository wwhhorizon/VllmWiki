# vllm-project/vllm#3407: Task finished unexpectedly. This should never happen! Please open an issue on Github.

| 字段 | 值 |
| --- | --- |
| Issue | [#3407](https://github.com/vllm-project/vllm/issues/3407) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;quantization |
| 症状 | crash;oom;slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Task finished unexpectedly. This should never happen! Please open an issue on Github.

### Issue 正文摘录

Hello I run 34B AWQ model on two A2 - `--tensor-parallel-size 2`. VRAM usage for both `14198MiB / 15356MiB`. I occurs from time to time on long requests: ``` uture exception was never retrieved future: Traceback (most recent call last): File "/workspace/vllm/engine/async_llm_engine.py", line 29, in _raise_exception_on_finish task.result() Exception in callback functools.partial( , request_tracker= ) handle: , request_tracker= )> File "/workspace/vllm/engine/async_llm_engine.py", line 33, in _raise_exception_on_finish raise AsyncEngineDeadError( vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. This should never happen! Please open an issue on Github. See stack trace above for the actual cause. ``` But then, one request seems stuck and spins infinitely fully consuming CPU - 100% and one of GPUs also 100% ``` INFO 03-04 14:42:13 metrics.py:161] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 1.8%, CPU KV cache usage: 0.0% ``` Restart seem helps Which direction I need to follow? Error mentions some CUDA memory params, also vllm log also mention something a...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ut: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 1.8%, CPU KV cache usage: 0.0% ``` Restart seem helps Which direction I need to follow? Error mentions some CUDA memory params, al...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: usage for both `14198MiB / 15356MiB`. I occurs from time to time on long requests: ``` uture exception was never retrieved future: Traceback (most recent call last): File "/workspace/vllm/engine/async_llm_engine.py", li...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: mance attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory cache;cuda;quantization crash;oom;slowdown Hello
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: start seem helps Which direction I need to follow? Error mentions some CUDA memory params, also vllm log also mention something about eager-something param, Can twearing one of these help to resolve this error? performa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: hould never happen! Please open an issue on Github. Hello I run 34B AWQ model on two A2 - `--tensor-parallel-size 2`. VRAM usage for both `14198MiB / 15356MiB`. I occurs from time to time on long requests: ``` uture exc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
