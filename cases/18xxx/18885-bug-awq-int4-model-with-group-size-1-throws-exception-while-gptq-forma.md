# vllm-project/vllm#18885: [Bug]: AWQ INT4 Model with group_size=-1 throws exception while gptq format is fine

| 字段 | 值 |
| --- | --- |
| Issue | [#18885](https://github.com/vllm-project/vllm/issues/18885) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AWQ INT4 Model with group_size=-1 throws exception while gptq format is fine

### Issue 正文摘录

### Your current environment For qwen3-0.6B ~~~bash INFO 05-29 03:02:16 [gpu_model_runner.py:1515] Starting to load model /data5/wenhuach/test/Qwen3-0.6B-Base-w4g-1... ERROR 05-29 03:02:16 [core.py:500] EngineCore failed to start. ERROR 05-29 03:02:16 [core.py:500] Traceback (most recent call last): ERROR 05-29 03:02:16 [core.py:500] File "/home/wenhuach/vllm/./vllm/v1/engine/core.py", line 491, in run_engine_core ERROR 05-29 03:02:16 [core.py:500] engine_core = EngineCoreProc(*args, **kwargs) ERROR 05-29 03:02:16 [core.py:500] File "/home/wenhuach/vllm/./vllm/v1/engine/core.py", line 390, in __init__ ERROR 05-29 03:02:16 [core.py:500] super().__init__(vllm_config, executor_class, log_stats, ERROR 05-29 03:02:16 [core.py:500] File "/home/wenhuach/vllm/./vllm/v1/engine/core.py", line 71, in __init__ ERROR 05-29 03:02:16 [core.py:500] self.model_executor = executor_class(vllm_config) ERROR 05-29 03:02:16 [core.py:500] File "/home/wenhuach/vllm/./vllm/executor/executor_base.py", line 52, in __init__ ERROR 05-29 03:02:16 [core.py:500] self._init_executor() ERROR 05-29 03:02:16 [core.py:500] File "/home/wenhuach/vllm/./vllm/executor/uniproc_executor.py", line 47, in _init_executor ERRO...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: AWQ INT4 Model with group_size=-1 throws exception while gptq format is fine bug ### Your current environment For qwen3-0.6B ~~~bash INFO 05-29 03:02:16 [gpu_model_runner.py:1515] Starting to load model /data5/we...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: AWQ INT4 Model with group_size=-1 throws exception while gptq format is fine bug ### Your current environment For qwen3-0.6B ~~~bash INFO 05-29 03:02:16 [gpu_model_runner.py:1515] Starting to load model /data5/we...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ues ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: s/utils.py", line 626, in ERROR 05-29 03:02:16 [core.py:500] maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}")) ERROR 05-29 03:02:16 [core.py:500] File "/home/wenhuach/vllm/./vllm/model_executor/models/qwen2.py",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: y", line 322, in ERROR 05-29 03:02:16 [core.py:500] lambda prefix: decoder_layer_type(config=config, ERROR 05-29 03:02:16 [core.py:500] File "/home/wenhuach/vllm/./vllm/model_executor/models/qwen3.py", line 173, in __in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
