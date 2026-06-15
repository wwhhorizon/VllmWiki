# vllm-project/vllm#32938: [Bug]: illegal memory access while running Qwen3-30B-A3B-Instruct-2507 on multi node with DeepEP backend

| 字段 | 值 |
| --- | --- |
| Issue | [#32938](https://github.com/vllm-project/vllm/issues/32938) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;moe |
| 子分类 |  |
| Operator 关键词 | cuda;moe;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: illegal memory access while running Qwen3-30B-A3B-Instruct-2507 on multi node with DeepEP backend

### Issue 正文摘录

### Your current environment - H200 hardware - vLLM v0.13.0 (upstream image) ### 🐛 Describe the bug Server Script ``` # Node 1 (Primary - handles incoming requests) NCCL_DEBUG=INFO VLLM_HOST_IP={node1 ip address} GLOO_SOCKET_FAMILY=AF_INET NCCL_SOCKET_FAMILY=AF_INET GLOO_SOCKET_IFNAME=eth0 NCCL_SOCKET_IFNAME=eth0 vllm serve Qwen/Qwen3-30B-A3B-Instruct-2507 \ --all2all-backend deepep_low_latency \ --tensor-parallel-size 1 \ --enable-expert-parallel \ --data-parallel-size 16 \ --data-parallel-size-local 8 \ --data-parallel-address {node1 ip address} \ --data-parallel-rpc-port 13345 \ --api-server-count=8 # Node 2 (Secondary - headless mode, no API server) NCCL_DEBUG=INFO VLLM_HOST_IP={node1 ip address} GLOO_SOCKET_FAMILY=AF_INET NCCL_SOCKET_FAMILY=AF_INET GLOO_SOCKET_IFNAME=eth0 NCCL_SOCKET_IFNAME=eth0 vllm serve Qwen/Qwen3-30B-A3B-Instruct-2507 \ --all2all-backend deepep_low_latency \ --tensor-parallel-size 1 \ --enable-expert-parallel \ --data-parallel-size 16 \ --data-parallel-size-local 8 \ --data-parallel-start-rank 8 \ --data-parallel-address {node1 ip address} \ --data-parallel-rpc-port 13345 \ --headless ``` Error Message `File "/usr/local/lib/python3.12/dist-packages/triton...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ``` Error Message `File "/usr/local/lib/python3.12/dist-packages/triton/compiler/compiler.py", line 473, in _init_handles self.module, self.function, self.n_regs, self.n_spills, self.n_max_threads = driver.active.utils....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: serve Qwen/Qwen3-30B-A3B-Instruct-2507 \ --all2all-backend deepep_low_latency \ --tensor-parallel-size 1 \ --enable-expert-parallel \ --data-parallel-size 16 \ --data-parallel-size-local 8 \ --data-parallel-address {nod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: cess while running Qwen3-30B-A3B-Instruct-2507 on multi node with DeepEP backend bug ### Your current environment - H200 hardware - vLLM v0.13.0 (upstream image) ### 🐛 Describe the bug Server Script ``` # Node 1 (Primar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ RuntimeError: Triton Error [CUDA]: an illegal memory access was encountered` Status Trace ``` vllm/v1/engine/core.py:109 (_initialize_kv_caches) → vllm/v1/executor/abstract.py:126 (deter...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: illegal memory access while running Qwen3-30B-A3B-Instruct-2507 on multi node with DeepEP backend bug ### Your current environment - H200 hardware - vLLM v0.13.0 (upstream image) ### 🐛 Describe the bug Server Scr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
