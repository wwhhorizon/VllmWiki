# vllm-project/vllm#39985: [Bug]: Qwen3.5-122B-A10B Engine hangs at Prefill phase under high concurrency (40 reqs) with multi-node PP=2 on dual 4090D nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#39985](https://github.com/vllm-project/vllm/issues/39985) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-122B-A10B Engine hangs at Prefill phase under high concurrency (40 reqs) with multi-node PP=2 on dual 4090D nodes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Description:** I am running a multi-node vLLM setup using two RTX 4090D nodes (8 GPUs each, total 16 GPUs) serving the **Qwen3.5-122B-A10B** model. The cluster is configured with `tensor-parallel-size=8` and `pipeline-parallel-size=2` over standard Ethernet (`NCCL_IB_DISABLE=1`). When I send a **single** streaming request, the engine processes it perfectly and streams the output as expected. However, when I send **40 concurrent requests**, the engine completely hangs/freezes during the Prefill phase. No tokens are generated, and the system deadlocks. During this hang, I observed an abnormally high CPU utilization (hovering around 200%) on the host machine. **Commands used to start the engine:** ```bash # ========== Leader Node (Rank 0) ========== NCCL_IB_DISABLE=1 GLOO_SOCKET_IFNAME=eth0 NCCL_SOCKET_IFNAME=eth0 VLLM_HOST_IP= \ vllm serve /path/to/Qwen3---5-122B-A10B-V1 \ --port 31111 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --trust-remote-code \ --served-model-name Qwen3.5-122B-A10B \ --gpu-memory-utilization 0.9 \ --max-model-len 16384 \ --enforce-eager \ --nnodes 2 \ --node-rank 0 \ --master-addr # ==========...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Qwen3.5-122B-A10B Engine hangs at Prefill phase under high concurrency (40 reqs) with multi-node PP=2 on dual 4090D nodes bug ### Your current environment ### 🐛 Describe the bug **Description:** I am running a mu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory cache;cuda;operator build_error;slowdown env_dependency...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: the bug **Description:** I am running a multi-node vLLM setup using two RTX 4090D nodes (8 GPUs each, total 16 GPUs) serving the **Qwen3.5-122B-A10B** model. The cluster is configured with `tensor-parallel-size=8` and `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5-122B-A10B Engine hangs at Prefill phase under high concurrency (40 reqs) with multi-node PP=2 on dual 4090D nodes bug ### Your current environment ### 🐛 Describe the bug **Description:** I am running a mu...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: eration throughput: 2.4 tokens/s, Running: 5 reqs, Waiting: 35 reqs, GPU KV cache usage: 5.0%, Prefix cache hit rate: 0.0% (APIServer pid=16) INFO 04-16 06:28:55 [loggers.py:259] Engine 000: Avg prompt throughput : 8576...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
