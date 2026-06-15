# vllm-project/vllm#18577: [Bug]: Killing local vLLM worker processes in  multiproc_worker_utils.py

| 字段 | 值 |
| --- | --- |
| Issue | [#18577](https://github.com/vllm-project/vllm/issues/18577) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Killing local vLLM worker processes in  multiproc_worker_utils.py

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I use Qwen 2.5 14B model (and 32B, 72B), I keep getting "INFO 05-22 20:32:10 multiproc_worker_utils.py:121] Killing local vLLM worker processes" ```python export VLLM_WORKER_MULTIPROC_METHOD=spawn VLLM_RPC_TIMEOUT=10000 vllm serve Qwen/Qwen2.5-14B-Instruct \ --trust-remote-code \ --dtype bfloat16 \ --max-model-len 8192 \ --distributed-executor-backend mp \ --tensor_parallel_size 2 \ --gpu-memory-utilization 0.95 \ --api-key token-abc123 \ --max-num-seqs 1 ``` My error is due to using multi GPU and P2P is not linked? ```python RuntimeError: CUDART error: CUDA-capable device(s) is/are busy or unavailable Process SpawnProcess-1: Traceback (most recent call last): File "/projectnb//conda_envs/env_agent/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/projectnb//conda_envs/env_agent/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/projectnb//conda_envs/env_agent/lib/python3.10/site-packages/vllm/distributed/device_communicators/custom_all_reduce_utils.py", line 34, in producer lib.cudaSetDevice(i) File "/projectnb//conda_envs/env_age...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: --max-num-seqs 1 ``` My error is due to using multi GPU and P2P is not linked? ```python RuntimeError: CUDART error: CUDA-capable device(s) is/are busy or unavailable Process SpawnProcess-1: Traceback (most recent call...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 0 vllm serve Qwen/Qwen2.5-14B-Instruct \ --trust-remote-code \ --dtype bfloat16 \ --max-model-len 8192 \ --distributed-executor-backend mp \ --tensor_parallel_size 2 \ --gpu-memory-utilization 0.95 \ --api-key token-abc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: --dtype bfloat16 \ --max-model-len 8192 \ --distributed-executor-backend mp \ --tensor_parallel_size 2 \ --gpu-memory-utilization 0.95 \ --api-key token-abc123 \ --max-num-seqs 1 ``` My error is due to using multi GPU a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s due to using multi GPU and P2P is not linked? ```python RuntimeError: CUDART error: CUDA-capable device(s) is/are busy or unavailable Process SpawnProcess-1: Traceback (most recent call last): File "/projectnb//conda_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tale ### Your current environment ### 🐛 Describe the bug When I use Qwen 2.5 14B model (and 32B, 72B), I keep getting "INFO 05-22 20:32:10 multiproc_worker_utils.py:121] Killing local vLLM worker processes" ```python ex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
