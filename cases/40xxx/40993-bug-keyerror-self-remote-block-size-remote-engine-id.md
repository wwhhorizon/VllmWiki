# vllm-project/vllm#40993: [Bug]: KeyError self.remote_block_size[remote_engine_id]

| 字段 | 值 |
| --- | --- |
| Issue | [#40993](https://github.com/vllm-project/vllm/issues/40993) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;moe;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | moe |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError self.remote_block_size[remote_engine_id]

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (Worker_DP1_TP0_EP4 pid=19507) ERROR 04-27 11:35:05 [v1/executor/multiproc_executor.py:932] File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/kv_transfer/kv_connector/utils.py", line 453, in block_size_ratio_from_engine_id (Worker_DP1_TP0_EP4 pid=19507) ERROR 04-27 11:35:05 [v1/executor/multiproc_executor.py:932] remote_block_size = self.remote_block_size[remote_engine_id] (Worker_DP1_TP0_EP4 pid=19507) ERROR 04-27 11:35:05 [v1/executor/multiproc_executor.py:932] ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^ (Worker_DP1_TP0_EP4 pid=19507) ERROR 04-27 11:35:05 [v1/executor/multiproc_executor.py:932] KeyError: 'f35e9d1d-f7fb-46cd-925b-d7478aa2b04a_dp1' PD Disaggregated : 1P1D 1P with2 nodes H100 80GB . 16GPU , 1D with4 nodes H100 80GB .32GPU , # prefill 1P (2 nodes) prefill 1: primary_node_ip="172.16.1.13" model_path="/data/deepseek-ai/DeepSeek-V3.2/" export VLLM_LOGGING_LEVEL=DEBUG export NCCL_NVLS_ENABLE=0 export NCCL_SOCKET_IFNAME=bond0 export GLOO_SOCKET_IFNAME=bond0 export VLLM_ENGINE_READY_TIMEOUT_S=1200 IP=$(hostname -I | awk '{print $1}') echo "IP=${IP}" VLLM_NIXL_SIDE_CHANNEL_HOST=${IP} VLLM_NIXL_SIDE_CHANNEL_PORT=...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: ANNEL_HOST=${IP} VLLM_NIXL_SIDE_CHANNEL_PORT=5600 export VLLM_USE_DEEP_GEMM=1 export VLLM_ALL2ALL_BACKEND="deepep_high_throughput" export VLLM_SKIP_P2P_CHECK=0 #export VLLM_MOE_ROUTING_SIMULATION_STRATEGY="uniform_rando...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: with2 nodes H100 80GB . 16GPU , 1D with4 nodes H100 80GB .32GPU , # prefill 1P (2 nodes) prefill 1: primary_node_ip="172.16.1.13" model_path="/data/deepseek-ai/DeepSeek-V3.2/" export VLLM_LOGGING_LEVEL=DEBUG export NCCL...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 0 export VLLM_USE_DEEP_GEMM=1 export VLLM_ALL2ALL_BACKEND="deepep_high_throughput" export VLLM_SKIP_P2P_CHECK=0 #export VLLM_MOE_ROUTING_SIMULATION_STRATEGY="uniform_random" export NVIDIA_GDRCOPY="enabled" export NVSHME...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: SIDE_CHANNEL_PORT=5600 export VLLM_USE_DEEP_GEMM=1 export VLLM_ALL2ALL_BACKEND="deepep_high_throughput" export VLLM_SKIP_P2P_CHECK=0 #export VLLM_MOE_ROUTING_SIMULATION_STRATEGY="uniform_random" export NVIDIA_GDRCOPY="e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -46cd-925b-d7478aa2b04a_dp1' PD Disaggregated : 1P1D 1P with2 nodes H100 80GB . 16GPU , 1D with4 nodes H100 80GB .32GPU , # prefill 1P (2 nodes) prefill 1: primary_node_ip="172.16.1.13" model_path="/data/deepseek-ai/Dee...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
