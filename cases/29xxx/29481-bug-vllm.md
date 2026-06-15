# vllm-project/vllm#29481: [Bug]: vllm显存碎片化导致一张显卡只能部署一个小模型

| 字段 | 值 |
| --- | --- |
| Issue | [#29481](https://github.com/vllm-project/vllm/issues/29481) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm显存碎片化导致一张显卡只能部署一个小模型

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 打算在一张4090上部署两个qwen3-0.6b的模型接口，按道理来说这么小的模型加上0.25的gpu-memory-utilization，每个接口应该只占6g显存，一张4090足够了，但是目前只能部起来一个，另一个报错了ERROR 11-26 14:34:34 [core.py:387] EngineCore hit an exception: Traceback (most recent call last): ERROR 11-26 14:34:34 [core.py:387] File "/root/miniconda3/envs/apirefcheck/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 378, in run_engine_core ERROR 11-26 14:34:34 [core.py:387] engine_core = EngineCoreProc(*args, **kwargs) ERROR 11-26 14:34:34 [core.py:387] File "/root/miniconda3/envs/apirefcheck/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 320, in __init__ ERROR 11-26 14:34:34 [core.py:387] super().__init__(vllm_config, executor_class, log_stats) ERROR 11-26 14:34:34 [core.py:387] File "/root/miniconda3/envs/apirefcheck/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 71, in __init__ ERROR 11-26 14:34:34 [core.py:387] self._initialize_kv_caches(vllm_config) ERROR 11-26 14:34:34 [core.py:387] File "/root/miniconda3/envs/apirefcheck/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 137, in _initialize_kv_caches ERROR 11-26 14:34:34 [core.py:387] kv_cache_configs = [ ERROR 11-...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e ### Your current environment ### 🐛 Describe the bug 打算在一张4090上部署两个qwen3-0.6b的模型接口，按道理来说这么小的模型加上0.25的gpu-memory-utilization，每个接口应该只占6g显存，一张4090足够了，但是目前只能部起来一个，另一个报错了ERROR 11-26 14:34:34 [core.py:387] EngineCore hit an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: led ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 14:34:34 [core.py:387] raise ValueError("No available memory for the cache blocks. " ERROR 11-26 14:34:34 [core.py:387] ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 34 [core.py:387] raise ValueError("No available memory for the cache blocks. " ERROR 11-26 14:34:34 [core.py:387] ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initia...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vllm显存碎片化导致一张显卡只能部署一个小模型 bug;stale ### Your current environment ### 🐛 Describe the bug 打算在一张4090上部署两个qwen3-0.6b的模型接口，按道理来说这么小的模型加上0.25的gpu-memory-utilization，每个接口应该只占6g显存，一张4090足够了，但是目前只能部起来一个，另一个报错了ERROR 11-26 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
