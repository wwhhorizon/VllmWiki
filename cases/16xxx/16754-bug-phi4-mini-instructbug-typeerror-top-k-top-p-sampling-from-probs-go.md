# vllm-project/vllm#16754: [Bug]: phi4-mini-instructBUG     TypeError: top_k_top_p_sampling_from_probs() got an unexpected keyword argument 'deterministic'

| 字段 | 值 |
| --- | --- |
| Issue | [#16754](https://github.com/vllm-project/vllm/issues/16754) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: phi4-mini-instructBUG     TypeError: top_k_top_p_sampling_from_probs() got an unexpected keyword argument 'deterministic'

### Issue 正文摘录

### Your current environment transformers 4.51.3 vllm 0.8.4 ### 🐛 Describe the bug RROR 04-17 11:42:20 [core.py:387] EngineCore hit an exception: Traceback (most recent call last): ERROR 04-17 11:42:20 [core.py:387] File "/root/miniforge3/envs/vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 378, in run_engine_core ERROR 04-17 11:42:20 [core.py:387] engine_core = EngineCoreProc(*args, **kwargs) ERROR 04-17 11:42:20 [core.py:387] File "/root/miniforge3/envs/vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 320, in __init__ ERROR 04-17 11:42:20 [core.py:387] super().__init__(vllm_config, executor_class, log_stats) ERROR 04-17 11:42:20 [core.py:387] File "/root/miniforge3/envs/vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 71, in __init__ ERROR 04-17 11:42:20 [core.py:387] self._initialize_kv_caches(vllm_config) ERROR 04-17 11:42:20 [core.py:387] File "/root/miniforge3/envs/vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 133, in _initialize_kv_caches ERROR 04-17 11:42:20 [core.py:387] available_gpu_memory = self.model_executor.determine_available_memory() ERROR 04-17 11:42:20 [core.py:387] File "/root/miniforge3/envs/vllm/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: in __init__ ERROR 04-17 11:42:20 [core.py:387] super().__init__(vllm_config, executor_class, log_stats) ERROR 04-17 11:42:20 [core.py:387] File "/root/miniforge3/envs/vllm/lib/python3.10/site-packages/vllm/v1/engine/cor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: r: top_k_top_p_sampling_from_probs() got an unexpected keyword argument 'deterministic' bug ### Your current environment transformers 4.51.3 vllm 0.8.4 ### 🐛 Describe the bug RROR 04-17 11:42:20 [core.py:387] EngineCore...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -packages/vllm/v1/sample/ops/topk_topp_sampler.py", line 116, in forward_cuda ERROR 04-17 11:42:20 [core.py:387] return flashinfer_sample(probs, k, p, generators) ERROR 04-17 11:42:20 [core.py:387] File "/root/miniforge...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: line 116, in forward_cuda ERROR 04-17 11:42:20 [core.py:387] return flashinfer_sample(probs, k, p, generators) ERROR 04-17 11:42:20 [core.py:387] File "/root/miniforge3/envs/vllm/lib/python3.10/site-packages/vllm/v1/sam...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: r: top_k_top_p_sampling_from_probs() got an unexpected keyword argument 'deterministic' bug ### Your current environment transformers 4.51.3 vllm 0.8.4 ### 🐛 Describe the bug RROR 04-17 11:42:20 [core.py:387] EngineCore...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
