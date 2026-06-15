# vllm-project/vllm#43206: [Bug]: Port collision ([Errno 98] Address already in use) when launching multiple LLM(tensor_parallel_size=2) instances concurrently on a single node (V1 Engine)

| 字段 | 值 |
| --- | --- |
| Issue | [#43206](https://github.com/vllm-project/vllm/issues/43206) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Port collision ([Errno 98] Address already in use) when launching multiple LLM(tensor_parallel_size=2) instances concurrently on a single node (V1 Engine)

### Issue 正文摘录

### Your current environment vllm0.19.0 ### 🐛 Describe the bug I am trying to run data annotation on an 8-GPU node by launching 4 independent Python processes. Each process instantiates an LLM class with tensor_parallel_size=2 (handling 1/4 of the dataset each) to maximize overall throughput. To avoid port collisions, I explicitly isolated the environment variables for each process (e.g., MASTER_PORT, VLLM_PORT, VLLM_RPC_PORT, VLLM_IPC_PATH, etc.). However, the initialization still fails with [Errno 98] Address already in use during the V1 engine's collective_rpc initialization (EngineCore_DP0). It seems that the V1 engine's multiproc executor (vllm/v1/executor/multiproc_executor.py) either has hardcoded ports for its ZMQ/RPC communication or suffers from a race condition when finding free ports concurrently, ignoring the environment variable isolations. ``` (EngineCore_DP0 pid=640) Process EngineCore_DP0: (EngineCore_DP0 pid=640) Traceback (most recent call last): (EngineCore_DP0 pid=640) File "/opt/conda/envs/python3.10.13/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=640) self.run() (EngineCore_DP0 pid=640) File "/opt/conda/envs/python3...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: __ (EngineCore_DP0 pid=640) num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( (EngineCore_DP0 pid=640) File "/opt/conda/envs/python3.10.13/lib/python3.10/site-packages/vllm/tracing/otel.py",...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: r_parallel_size=2 (handling 1/4 of the dataset each) to maximize overall throughput. To avoid port collisions, I explicitly isolated the environment variables for each process (e.g., MASTER_PORT, VLLM_PORT, VLLM_RPC_POR...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: each) to maximize overall throughput. To avoid port collisions, I explicitly isolated the environment variables for each process (e.g., MASTER_PORT, VLLM_PORT, VLLM_RPC_PORT, VLLM_IPC_PATH, etc.). However, the initializ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ine/core.py", line 114, in __init__ (EngineCore_DP0 pid=640) num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( (EngineCore_DP0 pid=640) File "/opt/conda/envs/python3.10.13/lib/python3.10/site...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
