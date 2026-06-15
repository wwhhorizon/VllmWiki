# vllm-project/vllm#16819: [Bug]: When configuring Ray with a custom temporary directory using the --temp-dir parameter, the distributed multi-node inference cluster fails to deploy successfully.

| 字段 | 值 |
| --- | --- |
| Issue | [#16819](https://github.com/vllm-project/vllm/issues/16819) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When configuring Ray with a custom temporary directory using the --temp-dir parameter, the distributed multi-node inference cluster fails to deploy successfully.

### Issue 正文摘录

### Your current environment Use two H20 nodes ```text # python 3.10 pip install vllm==0.8.4 pip install pyarrow pandas ``` ### 🐛 Describe the bug When configuring Ray with a custom temporary directory using the --temp-dir parameter, the distributed multi-node inference cluster fails to deploy successfully. ``` ray start --head --port 6379 --temp-dir /data/ray --node-ip-address dead-ip ``` All nodes (head and workers) have the same /data directory Start vllm ``` vllm serve /data/models/DeepSeek-V3-0324 \ --served-model-name deepseek-v3 \ --host 0.0.0.0 \ --port 8000 \ --trust-remote-code \ --gpu-memory-utilization 0.9 \ --tensor-parallel-size 8 \ --enable-chunked-prefill \ --enable-prefix-caching \ --enable-expert-parallel \ --pipeline-parallel-size 2 \ --distributed-executor-backend=ray ``` err ``` Started a local Ray instance WARNING 02-02 19:54:20 ray_utils.py:315] The number of required GPUs exceeds the total number of available GPUs in the placement group. INFO 02-02 19:54:30 ray_utils.py:212] Waiting for creating a placement group of specs for 10 seconds. specs=[{'GPU': 1.0, 'node:172.31.42.4': 0.001}, {'GPU': 1.0}, {'GPU': 1.0}, {'GPU': 1.0}, {'GPU': 1.0}, {'GPU': 1.0}, {'G...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: buted multi-node inference cluster fails to deploy successfully. bug;ray;stale ### Your current environment Use two H20 nodes ```text # python 3.10 pip install vllm==0.8.4 pip install pyarrow pandas ``` ### 🐛 Describe t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: When configuring Ray with a custom temporary directory using the --temp-dir parameter, the distributed multi-node inference cluster fails to deploy successfully. bug;ray;stale ### Your current environment Use two...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -expert-parallel \ --pipeline-parallel-size 2 \ --distributed-executor-backend=ray ``` err ``` Started a local Ray instance WARNING 02-02 19:54:20 ray_utils.py:315] The number of required GPUs exceeds the total number o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: # Your current environment Use two H20 nodes ```text # python 3.10 pip install vllm==0.8.4 pip install pyarrow pandas ``` ### 🐛 Describe the bug When configuring Ray with a custom temporary directory using the --temp-di...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ize 8 \ --enable-chunked-prefill \ --enable-prefix-caching \ --enable-expert-parallel \ --pipeline-parallel-size 2 \ --distributed-executor-backend=ray ``` err ``` Started a local Ray instance WARNING 02-02 19:54:20 ray...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
