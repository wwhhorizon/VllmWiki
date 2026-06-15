# vllm-project/vllm#24756: [Bug]: Occasional ZMQ port conflict

| 字段 | 值 |
| --- | --- |
| Issue | [#24756](https://github.com/vllm-project/vllm/issues/24756) |
| 状态 | closed |
| 标签 | bug;stale;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Occasional ZMQ port conflict

### Issue 正文摘录

For example: https://buildkite.com/vllm/ci/builds/30528#01993e5f-3468-41ac-b0c0-5df75fc677c2 ``` [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) self.engine_core = EngineCoreClient.make_async_mp_client( [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core_client.py", line 101, in make_async_mp_client [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) return DPLBAsyncMPClient(*client_args) [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core_client.py", line 1124, in __init__ [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) super().__init__(vllm_config, executor_class, log_stats, [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core_client.py", line 974, in __init__ [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) super().__init__(vllm_config, executor_class, log_stats, [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) File "/usr/local/lib/python3.12/dist-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Occasional ZMQ port conflict bug;stale;ci-failure For example: https://buildkite.com/vllm/ci/builds/30528#01993e5f-3468-41ac-b0c0-5df75fc677c2 ``` [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) self.engine_core =...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ().bind(addr) [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) File "zmq/backend/cython/_zmq.py", line 1009, in zmq.backend.cython._zmq.Socket.bind [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) _check_rc(rc) [2025-09-12T...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) super().__init__(vllm_config, executor_class, log_stats, [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core_cl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Occasional ZMQ port conflict bug;stale;ci-failure For example: https://buildkite.com/vllm/ci/builds/30528#01993e5f-3468-41ac-b0c0-5df75fc677c2 ``` [2025-09-12T15:42:57Z] (ApiServer_1 pid=20007) self.engine_core =...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
