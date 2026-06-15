# vllm-project/vllm#15537: [Bug]: Distributed Inference and Serving BUG

| 字段 | 值 |
| --- | --- |
| Issue | [#15537](https://github.com/vllm-project/vllm/issues/15537) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;operator |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Distributed Inference and Serving BUG

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug INFO 03-26 09:15:05 [cuda.py:285] Using Flash Attention backend. (raylet) [2025-03-26 09:15:12,562 E 228 259] (raylet) file_system_monitor.cc:116: /tmp/ray/session_2025-03-26_08-55-15_777925_1 is over 95% full, available space: 16.7067 GB; capacity: 491.079 GB. Object creation will fail if spilling is required. [W326 09:15:16.969966369 socket.cpp:204] [c10d] The hostname of the client socket cannot be retrieved. err=-3 (RayWorkerWrapper pid=899, ip=192.168.8.223) [W326 09:15:17.028599736 socket.cpp:204] [c10d] The hostname of the client socket cannot be retrieved. err=-3 (raylet) [2025-03-26 09:15:22,570 E 228 259] (raylet) file_system_monitor.cc:116: /tmp/ray/session_2025-03-26_08-55-15_777925_1 is over 95% full, available space: 16.7066 GB; capacity: 491.079 GB. Object creation will fail if spilling is required. [W326 09:15:26.980225279 socket.cpp:204] [c10d] The hostname of the client socket cannot be retrieved. err=-3 (RayWorkerWrapper pid=901, ip=192.168.8.223) [W326 09:15:17.022189109 socket.cpp:204] [c10d] The hostname of the client socket cannot be retrieved. err=-3 [repeated 2x across cluster] (raylet) [2025-03-26 09:15:...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ment ### 🐛 Describe the bug INFO 03-26 09:15:05 [cuda.py:285] Using Flash Attention backend. (raylet) [2025-03-26 09:15:12,562 E 228 259] (raylet) file_system_monitor.cc:116: /tmp/ray/session_2025-03-26_08-55-15_777925_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: -26_08-55-15_777925_1 is over 95% full, available space: 16.7067 GB; capacity: 491.079 GB. Object creation will fail if spilling is required. [W326 09:15:16.969966369 socket.cpp:204] [c10d] The hostname of the client so...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: our current environment ### 🐛 Describe the bug INFO 03-26 09:15:05 [cuda.py:285] Using Flash Attention backend. (raylet) [2025-03-26 09:15:12,562 E 228 259] (raylet) file_system_monitor.cc:116: /tmp/ray/session_2025-03-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 6 [worker_base.py:620] init_worker_distributed_environment(self.vllm_config, self.rank, ERROR 03-26 09:15:56 [worker_base.py:620] File "/opt/venv/lib/python3.12/site-packages/vllm/worker/worker.py", line 505, in init_wo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Distributed Inference and Serving BUG bug;stale ### Your current environment ### 🐛 Describe the bug INFO 03-26 09:15:05 [cuda.py:285] Using Flash Attention backend. (raylet) [2025-03-26 09:15:12,562 E 228 259] (r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
