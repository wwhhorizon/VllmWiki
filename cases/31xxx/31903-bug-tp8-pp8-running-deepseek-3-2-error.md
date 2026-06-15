# vllm-project/vllm#31903: [Bug]: TP8+PP8 running deepseek-3.2 error

| 字段 | 值 |
| --- | --- |
| Issue | [#31903](https://github.com/vllm-project/vllm/issues/31903) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TP8+PP8 running deepseek-3.2 error

### Issue 正文摘录

### Your current environment vllm serve DeepSeek-V3.2 -tp=8 -pp=4 --distributed-executor-backend ray ``` (EngineCore_DP0 pid=749) INFO 01-07 00:15:33 [kv_cache_utils.py:1305] GPU KV cache size: 1,214,464 tokens (EngineCore_DP0 pid=749) INFO 01-07 00:15:33 [kv_cache_utils.py:1310] Maximum concurrency for 163,840 tokens per request: 7.41x (EngineCore_DP0 pid=749) (RayWorkerWrapper pid=347, ip=172.16.17.12) ERROR 01-07 00:15:31 [worker_base.py:344] Error executing method 'initialize_from_config'. This might cause deadlock in distributed execution. (EngineCore_DP0 pid=749) (RayWorkerWrapper pid=347, ip=172.16.17.12) ERROR 01-07 00:15:31 [worker_base.py:344] Traceback (most recent call last): (EngineCore_DP0 pid=749) (RayWorkerWrapper pid=347, ip=172.16.17.12) ERROR 01-07 00:15:31 [worker_base.py:344] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/worker_base.py", line 334, in execute_method (EngineCore_DP0 pid=749) (RayWorkerWrapper pid=347, ip=172.16.17.12) ERROR 01-07 00:15:31 [worker_base.py:344] return run_method(self, method, args, kwargs) (EngineCore_DP0 pid=749) (RayWorkerWrapper pid=347, ip=172.16.17.12) ERROR 01-07 00:15:31 [worker_base.py:344] ^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: TP8+PP8 running deepseek-3.2 error bug;stale ### Your current environment vllm serve DeepSeek-V3.2 -tp=8 -pp=4 --distributed-executor-backend ray ``` (EngineCore_DP0 pid=749) INFO 01-07 00:15:33 [kv_cache_utils.p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: environment vllm serve DeepSeek-V3.2 -tp=8 -pp=4 --distributed-executor-backend ray ``` (EngineCore_DP0 pid=749) INFO 01-07 00:15:33 [kv_cache_utils.py:1305] GPU KV cache size: 1,214,464 tokens (EngineCore_DP0 pid=749)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: r_base.py:344] File "/usr/local/lib/python3.12/dist-packages/ray/util/tracing/tracing_helper.py", line 461, in _resume_span (EngineCore_DP0 pid=749) (RayWorkerWrapper pid=347, ip=172.16.17.12) ERROR 01-07 00:15:31 [work...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 07 00:15:31 [worker_base.py:344] Error executing method 'initialize_from_config'. This might cause deadlock in distributed execution. (EngineCore_DP0 pid=749) (RayWorkerWrapper pid=347, ip=172.16.17.12) ERROR 01-07 00:1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ray ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
