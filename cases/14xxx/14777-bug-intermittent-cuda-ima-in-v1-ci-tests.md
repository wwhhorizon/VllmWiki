# vllm-project/vllm#14777: [Bug]: Intermittent CUDA IMA in V1 CI tests

| 字段 | 值 |
| --- | --- |
| Issue | [#14777](https://github.com/vllm-project/vllm/issues/14777) |
| 状态 | closed |
| 标签 | bug;v1 |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Intermittent CUDA IMA in V1 CI tests

### Issue 正文摘录

### Your current environment CI ### 🐛 Describe the bug ``` Processed prompts: 0% 0/100 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s]ERROR 03-13 08:00:58 [core.py:337] EngineCore hit an exception: Traceback (most recent call last): [2025-03-13T08:00:58Z] ERROR 03-13 08:00:58 [core.py:337] File "/opt/venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 330, in run_engine_core [2025-03-13T08:00:58Z] ERROR 03-13 08:00:58 [core.py:337] engine_core.run_busy_loop() [2025-03-13T08:00:58Z] ERROR 03-13 08:00:58 [core.py:337] File "/opt/venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 364, in run_busy_loop [2025-03-13T08:00:58Z] ERROR 03-13 08:00:58 [core.py:337] outputs = step_fn() [2025-03-13T08:00:58Z] ERROR 03-13 08:00:58 [core.py:337] ^^^^^^^^^ [2025-03-13T08:00:58Z] ERROR 03-13 08:00:58 [core.py:337] File "/opt/venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 192, in step [2025-03-13T08:00:58Z] ERROR 03-13 08:00:58 [core.py:337] output = self.model_executor.execute_model(scheduler_output) [2025-03-13T08:00:58Z] ERROR 03-13 08:00:58 [core.py:337] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-03-13T08:00:58Z] ERR...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Intermittent CUDA IMA in V1 CI tests bug;v1 ### Your current environment CI ### 🐛 Describe the bug ``` Processed prompts: 0% 0/100 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s]ERROR 03-13 0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Intermittent CUDA IMA in V1 CI tests bug;v1 ### Your current environment CI ### 🐛 Describe the bug ``` Processed prompts: 0% 0/100 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s]ERROR 03-13 0...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: a30668bf correctness ci_build;frontend_api cuda;kernel build_error;crash;mismatch env_dependency;shape Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 03-13 08:00:58 [core.py:337] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 [2025-03-13T08:00:58Z] ERROR 03-13 08:00:58 [core.py:337] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. [2025-03-1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 25-03-13T08:00:58Z] ERROR 03-13 08:00:58 [core.py:337] output = self.model_executor.execute_model(scheduler_output) [2025-03-13T08:00:58Z] ERROR 03-13 08:00:58 [core.py:337] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
