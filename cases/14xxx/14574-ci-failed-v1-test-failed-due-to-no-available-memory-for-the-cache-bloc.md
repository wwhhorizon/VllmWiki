# vllm-project/vllm#14574: [CI failed]: V1 Test Failed due to "No available memory for the cache blocks" in GitHub Actions

| 字段 | 值 |
| --- | --- |
| Issue | [#14574](https://github.com/vllm-project/vllm/issues/14574) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI failed]: V1 Test Failed due to "No available memory for the cache blocks" in GitHub Actions

### Issue 正文摘录

### Anything you want to discuss about vllm. I encountered c1 test failure when running CI while initiating the merge request code code link：https://github.com/vllm-project/vllm/pull/14377 The error is as follows： [2025-03-10T15:07:20Z] INFO 03-10 08:07:20 [gpu_model_runner.py:1067] Model loading took 0.2389 GB and 0.977005 seconds -- | [2025-03-10T15:07:20Z] ERROR 03-10 08:07:20 [core.py:302] EngineCore hit an exception: Traceback (most recent call last): | [2025-03-10T15:07:20Z] ERROR 03-10 08:07:20 [core.py:302] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 294, in run_engine_core | [2025-03-10T15:07:20Z] ERROR 03-10 08:07:20 [core.py:302] engine_core = EngineCoreProc(*args, **kwargs) | [2025-03-10T15:07:20Z] ERROR 03-10 08:07:20 [core.py:302] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ | [2025-03-10T15:07:20Z] ERROR 03-10 08:07:20 [core.py:302] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 249, in __init__ | [2025-03-10T15:07:20Z] ERROR 03-10 08:07:20 [core.py:302] super().__init__(vllm_config, executor_class, log_stats) | [2025-03-10T15:07:20Z] ERROR 03-10 08:07:20 [core.py:302] File "/usr/local/lib/python3.12/dist-packages/vllm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI failed]: V1 Test Failed due to "No available memory for the cache blocks" in GitHub Actions stale ### Anything you want to discuss about vllm. I encountered c1 test failure when running CI while initiating the merge
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: he error is as follows： [2025-03-10T15:07:20Z] INFO 03-10 08:07:20 [gpu_model_runner.py:1067] Model loading took 0.2389 GB and 0.977005 seconds -- | [2025-03-10T15:07:20Z] ERROR 03-10 08:07:20 [core.py:302] EngineCore h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: iled due to "No available memory for the cache blocks" in GitHub Actions stale ### Anything you want to discuss about vllm. I encountered c1 test failure when running CI while initiating the merge request code code link...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ine ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [CI failed]: V1 Test Failed due to "No available memory for the cache blocks" in GitHub Actions stale ### Anything you want to discuss about vllm. I encountered c1 test failure when running CI while initiating the merge...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
