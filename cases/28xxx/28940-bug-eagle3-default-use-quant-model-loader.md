# vllm-project/vllm#28940: [Bug]: eagle3 default use quant model loader

| 字段 | 值 |
| --- | --- |
| Issue | [#28940](https://github.com/vllm-project/vllm/issues/28940) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support;quantization;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | quantization |
| 症状 | crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: eagle3 default use quant model loader

### Issue 正文摘录

### Your current environment Currently, Eagle3 defaults to using the quantized model loader, which prevents the use of previous non-quantized Eagle models and causes a key mismatch error during loading. ### 🐛 Describe the bug (EngineCore_DP0 pid=2326) ERROR 11-18 15:34:49 [core.py:708] EngineCore failed to start. (EngineCore_DP0 pid=2326) ERROR 11-18 15:34:49 [core.py:708] Traceback (most recent call last): (EngineCore_DP0 pid=2326) ERROR 11-18 15:34:49 [core.py:708] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 699, in run_engine_core (EngineCore_DP0 pid=2326) ERROR 11-18 15:34:49 [core.py:708] engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=2326) ERROR 11-18 15:34:49 [core.py:708] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=2326) ERROR 11-18 15:34:49 [core.py:708] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 498, in __init__ (EngineCore_DP0 pid=2326) ERROR 11-18 15:34:49 [core.py:708] super().__init__(vllm_config, executor_class, log_stats, (EngineCore_DP0 pid=2326) ERROR 11-18 15:34:49 [core.py:708] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 83, in __init__ (E...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: eagle3 default use quant model loader bug;stale ### Your current environment Currently, Eagle3 defaults to using the quantized model loader, which prevents the use of previous non-quantized Eagle models and cause...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: eagle3 default use quant model loader bug;stale ### Your current environment Currently, Eagle3 defaults to using the quantized model loader, which prevents the use of previous non-quantized Eagle models and cause...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: eagle3 default use quant model loader bug;stale ### Your current environment Currently, Eagle3 defaults to using the quantized model loader, which prevents the use of previous non-quantized Eagle models and cause...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: events the use of previous non-quantized Eagle models and causes a key mismatch error during loading. ### 🐛 Describe the bug (EngineCore_DP0 pid=2326) ERROR 11-18 15:34:49 [core.py:708] EngineCore failed to start. (Engi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: prevents the use of previous non-quantized Eagle models and causes a key mismatch error during loading. ### 🐛 Describe the bug (EngineCore_DP0 pid=2326) ERROR 11-18 15:34:49 [core.py:708] EngineCore failed to start. (En...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
