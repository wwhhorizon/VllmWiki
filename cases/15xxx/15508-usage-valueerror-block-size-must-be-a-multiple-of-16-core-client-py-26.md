# vllm-project/vllm#15508: [Usage]: ValueError: Block size must be a multiple of 16.  [core_client.py:269] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.

| 字段 | 值 |
| --- | --- |
| Issue | [#15508](https://github.com/vllm-project/vllm/issues/15508) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: ValueError: Block size must be a multiple of 16.  [core_client.py:269] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.

### Issue 正文摘录

### Your current environment ```shell INFO 03-26 08:41:09 [kv_cache_utils.py:537] GPU KV cache size: 17,328 tokens INFO 03-26 08:41:09 [kv_cache_utils.py:540] Maximum concurrency for 5,120 tokens per request: 3.38x ERROR 03-26 08:41:09 [core.py:340] EngineCore hit an exception: Traceback (most recent call last): ERROR 03-26 08:41:09 [core.py:340] File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 332, in run_engine_core ERROR 03-26 08:41:09 [core.py:340] engine_core = EngineCoreProc(*args, **kwargs) ERROR 03-26 08:41:09 [core.py:340] File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 287, in __init__ ERROR 03-26 08:41:09 [core.py:340] super().__init__(vllm_config, executor_class, log_stats) ERROR 03-26 08:41:09 [core.py:340] File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 62, in __init__ ERROR 03-26 08:41:09 [core.py:340] num_gpu_blocks, num_cpu_blocks = self._initialize_kv_caches( ERROR 03-26 08:41:09 [core.py:340] File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 135, in _initialize_kv_caches ERROR 03-26 08:41:09...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: in __init__ ERROR 03-26 08:41:09 [core.py:340] super().__init__(vllm_config, executor_class, log_stats) ERROR 03-26 08:41:09 [core.py:340] File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/v1/engine/cor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _cache ERROR 03-26 08:41:09 [core.py:340] kv_cache_shape = self.attn_backend.get_kv_cache_shape( ERROR 03-26 08:41:09 [core.py:340] File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/v1/attention/backend...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: nt environment ```shell INFO 03-26 08:41:09 [kv_cache_utils.py:537] GPU KV cache size: 17,328 tokens INFO 03-26 08:41:09 [kv_cache_utils.py:540] Maximum concurrency for 5,120 tokens per request: 3.38x ERROR 03-26 08:41:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Usage]: ValueError: Block size must be a multiple of 16. [core_client.py:269] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue. usage ### Your current environment ```she...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
