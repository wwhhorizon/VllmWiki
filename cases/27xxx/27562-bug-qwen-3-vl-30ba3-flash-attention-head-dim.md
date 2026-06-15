# vllm-project/vllm#27562: [Bug]: Qwen 3 VL 30bA3 Flash Attention head dim

| 字段 | 值 |
| --- | --- |
| Issue | [#27562](https://github.com/vllm-project/vllm/issues/27562) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen 3 VL 30bA3 Flash Attention head dim

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` _DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] EngineCore failed to start. (EngineCore_DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] Traceback (most recent call last): (EngineCore_DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 770, in run_engine_core (EngineCore_DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 538, in __init__ (EngineCore_DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] super().__init__( (EngineCore_DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 109, in __init__ (EngineCore_DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( (EngineCore_DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (En...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen 3 VL 30bA3 Flash Attention head dim bug;stale ### Your current environment ### 🐛 Describe the bug ``` _DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] EngineCore failed to start. (EngineCore_DP0 pid=175) ERR...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: (EngineCore_DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( (EngineCore_DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] ^^^^^^^^^^^^^^^^^^^^^...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: re_DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] self.model_runner.profile_run() (EngineCore_DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_model_runne...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Qwen 3 VL 30bA3 Flash Attention head dim bug;stale ### Your current environment ### 🐛 Describe the bug ``` _DP0 pid=175) ERROR 10-27 08:33:41 [core.py:779] EngineCore failed to start. (EngineCore_DP0 pid=175) ERR...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 5) ERROR 10-27 08:33:41 [core.py:779] RuntimeError: This flash attention build does not support headdim not being a multiple of 32. (EngineCore_DP0 pid=175) Traceback (most recent call last): (EngineCore_DP0 pid=175) Fi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
