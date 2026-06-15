# vllm-project/vllm#27676: [Bug]: DeepEP low latency + dp + ep crahsed without any log

| 字段 | 值 |
| --- | --- |
| Issue | [#27676](https://github.com/vllm-project/vllm/issues/27676) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepEP low latency + dp + ep crahsed without any log

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve deepseek-ai/DeepSeek-V2-lite -dp 2 --enable_expert_parallel` ```bash home/wentao/ep_kernels_workspace/nvshmem_src/src/host/transport/transport.cpp:nvshmemi_transport_init:275: init failed for transport: IBGDA /home/wentao/ep_kernels_workspace/nvshmem_src/src/host/transport/transport.cpp:nvshmemi_transport_init:287: Unable to initialize any transports. returning error. /home/wentao/ep_kernels_workspace/nvshmem_src/src/host/init/init.cu:995: non-zero status: 7 nvshmem detect topo failed /home/wentao/ep_kernels_workspace/nvshmem_src/src/host/init/init.cu:nvshmemi_check_state_and_init:1080: nvshmem initialization failed, exiting WARN: cudaHostRegister with IoMemory failed with error=800. We may need to use a fallback path. WARN: ibgda_nic_mem_gpu_map failed. We may need to use the CPU fallback path. WARN: ibgda_alloc_and_map_qp_uar with GPU as handler failed. We may need to enter the CPU fallback path. WARN: GPU cannot map UAR of device mlx5_15. Skipping... /home/wentao/ep_kernels_workspace/nvshmem_src/src/host/transport/transport.cpp:nvshmemi_transport_init:275: init failed for transport: IBGDA /home/wentao/ep_kernels_wo...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: daHostRegister with IoMemory failed with error=800. We may need to use a fallback path. WARN: ibgda_nic_mem_gpu_map failed. We may need to use the CPU fallback path. WARN: ibgda_alloc_and_map_qp_uar with GPU as handler...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: /__init__.py", line 109, in run (APIServer pid=2729727) return __asyncio.run( (APIServer pid=2729727) ^^^^^^^^^^^^^^ (APIServer pid=2729727) File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run (APIServer pid...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: heck_state_and_init:1080: nvshmem initialization failed, exiting WARN: cudaHostRegister with IoMemory failed with error=800. We may need to use a fallback path. WARN: ibgda_nic_mem_gpu_map failed. We may need to use the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: DeepEP low latency + dp + ep crahsed without any log bug ### Your current environment ### 🐛 Describe the bug `vllm serve deepseek-ai/DeepSeek-V2-lite -dp 2 --enable_expert_parallel` ```bash home/wentao/ep_kernels...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: m_engine_args (APIServer pid=2729727) async_llm = AsyncLLM.from_vllm_config( (APIServer pid=2729727) ^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=2729727) File "/home/wentao/vllm-source/vllm/utils/func_utils.py", line 116,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
