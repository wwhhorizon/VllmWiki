# vllm-project/vllm#37974: [Bug]: [Bug]: Kimi-K2.5 on version 0.18.0 results in an keyerror when the pipeline parallelism (PP) is greater than or equal to 2

| 字段 | 值 |
| --- | --- |
| Issue | [#37974](https://github.com/vllm-project/vllm/issues/37974) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [Bug]: Kimi-K2.5 on version 0.18.0 results in an keyerror when the pipeline parallelism (PP) is greater than or equal to 2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using 64 H100 to run Kimi-K2.5 with vllm-0.18.0, and this is my startup command: ''' bash ./multi-node-serving.sh leader --ray_port=6379 --ray_cluster_size=8 && \ vllm serve /models/preset/moonshotai/Kimi-K2.5/v1.0 \ --port 8087 \ --distributed-executor-backend ray \ --trust-remote-code \ --tensor-parallel-size 8 \ --pipeline-parallel-size 8 \ --tool-call-parser kimi_k2 \ --reasoning-parser kimi_k2 ''' but it's failed with **KeyError: 'language_model.model.layers.30.self_attn.attn' [repeated 49x across cluster]** : ''' ``` EngineCore pid=114613) (RayWorkerWrapper pid=29113, ip=10.45.7.181) ERROR 03-24 15:39:40 [ray_utils.py:74] Error executing method 'initialize_from_config'. This might cause deadlock in distributed execution. [repeated 49x across cluster] (EngineCore pid=114613) (RayWorkerWrapper pid=29113, ip=10.45.7.181) ERROR 03-24 15:39:40 [ray_utils.py:74] Traceback (most recent call last): [repeated 49x across cluster] (EngineCore pid=114613) (RayWorkerWrapper pid=29113, ip=10.45.7.181) ERROR 03-24 15:39:40 [ray_utils.py:74] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/ray_utils.py", line 65, in exec...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: K2.5 on version 0.18.0 results in an keyerror when the pipeline parallelism (PP) is greater than or equal to 2 bug ### Your current environment ### 🐛 Describe the bug I am using 64 H100 to run Kimi-K2.5 with vllm-0.18.0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: [Bug]: Kimi-K2.5 on version 0.18.0 results in an keyerror when the pipeline parallelism (PP) is greater than or equal to 2 bug ### Your current environment ### 🐛 Describe the bug I am using 64 H100 to run Kimi-K2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -serving.sh leader --ray_port=6379 --ray_cluster_size=8 && \ vllm serve /models/preset/moonshotai/Kimi-K2.5/v1.0 \ --port 8087 \ --distributed-executor-backend ray \ --trust-remote-code \ --tensor-parallel-size 8 \ --pi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: /preset/moonshotai/Kimi-K2.5/v1.0 \ --port 8087 \ --distributed-executor-backend ray \ --trust-remote-code \ --tensor-parallel-size 8 \ --pipeline-parallel-size 8 \ --tool-call-parser kimi_k2 \ --reasoning-parser kimi_k...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: py:74] Error executing method 'initialize_from_config'. This might cause deadlock in distributed execution. [repeated 49x across cluster] (EngineCore pid=114613) (RayWorkerWrapper pid=29113, ip=10.45.7.181) ERROR 03-24...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
