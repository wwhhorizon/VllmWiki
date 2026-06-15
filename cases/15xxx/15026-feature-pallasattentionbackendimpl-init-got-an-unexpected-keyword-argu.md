# vllm-project/vllm#15026: [Feature]: PallasAttentionBackendImpl.__init__() got an unexpected keyword argument 'q_lora_rank'

| 字段 | 值 |
| --- | --- |
| Issue | [#15026](https://github.com/vllm-project/vllm/issues/15026) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: PallasAttentionBackendImpl.__init__() got an unexpected keyword argument 'q_lora_rank'

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ``` clear && XLA_HLO_DEBUG=1 VLLM_USE_V1=1 vllm serve /mnt/jfs/models/DeepSeek-V2-Lite-Chat/ --seed 42 --disable-log-requests --download_dir "/mnt/disks/persist" --gpu-memory-utilization=0.95 --max-num-batched-tokens=512 --max-num-seqs=512 --tensor-parallel-size=1 --max-model-len=2048 --trust_remote_code &> log.txt ``` Got: ``` INFO 03-18 10:57:03 [tpu.py:39] Cannot use None backend on TPU. INFO 03-18 10:57:03 [tpu.py:42] Using Pallas V1 backend. ERROR 03-18 10:57:03 [core.py:340] EngineCore hit an exception: Traceback (most recent call last): ERROR 03-18 10:57:03 [core.py:340] File "/workspace/vllm/vllm/v1/engine/core.py", line 332, in run_engine_core ERROR 03-18 10:57:03 [core.py:340] engine_core = EngineCoreProc(*args, **kwargs) ERROR 03-18 10:57:03 [core.py:340] File "/workspace/vllm/vllm/v1/engine/core.py", line 287, in __init__ ERROR 03-18 10:57:03 [core.py:340] super().__init__(vllm_config, executor_class, log_stats) ERROR 03-18 10:57:03 [core.py:340] File "/workspace/vllm/vllm/v1/engine/core.py", line 59, in __init__ ERROR 03-18 10:57:03 [core.py:340] self.model_executor = executor_class(vllm_config) ERROR 03-18 10:57:03 [core.py:340...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Impl.__init__() got an unexpected keyword argument 'q_lora_rank' feature request;stale ### 🚀 The feature, motivation and pitch ``` clear && XLA_HLO_DEBUG=1 VLLM_USE_V1=1 vllm serve /mnt/jfs/models/DeepSeek-V2-Lite-Chat/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nd pitch ``` clear && XLA_HLO_DEBUG=1 VLLM_USE_V1=1 vllm serve /mnt/jfs/models/DeepSeek-V2-Lite-Chat/ --seed 42 --disable-log-requests --download_dir "/mnt/disks/persist" --gpu-memory-utilization=0.95 --max-num-batched-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: PallasAttentionBackendImpl.__init__() got an unexpected keyword argument 'q_lora_rank' feature request;stale ### 🚀 The feature, motivation and pitch ``` clear && XLA_HLO_DEBUG=1 VLLM_USE_V1=1 vllm serve /mnt/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 18 10:57:03 [core.py:340] self.impl = impl_cls(num_heads, head_size, scale, num_kv_heads, ERROR 03-18 10:57:03 [core.py:340] TypeError: PallasAttentionBackendImpl.__init__() got an unexpected keyword argument 'q_lora_ra...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
