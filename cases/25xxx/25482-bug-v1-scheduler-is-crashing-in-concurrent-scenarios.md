# vllm-project/vllm#25482: [Bug]: V1 scheduler is crashing in concurrent scenarios

| 字段 | 值 |
| --- | --- |
| Issue | [#25482](https://github.com/vllm-project/vllm/issues/25482) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 scheduler is crashing in concurrent scenarios

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are running vllm on Triton, and since we upgraded to the new V1, we are finding that vllm is randomly dying when we are stressing the GPU. The error is this: ``` (EngineCore_0 pid=195) ERROR 09-23 10:29:55 [core.py:702] EngineCore encountered a fatal error. (EngineCore_0 pid=195) ERROR 09-23 10:29:55 [core.py:702] Traceback (most recent call last): (EngineCore_0 pid=195) ERROR 09-23 10:29:55 [core.py:702] File "/opt/tritonserver/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 693, in run_engine_core (EngineCore_0 pid=195) ERROR 09-23 10:29:55 [core.py:702] engine_core.run_busy_loop() (EngineCore_0 pid=195) ERROR 09-23 10:29:55 [core.py:702] File "/opt/tritonserver/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 720, in run_busy_loop (EngineCore_0 pid=195) ERROR 09-23 10:29:55 [core.py:702] self._process_engine_step() (EngineCore_0 pid=195) ERROR 09-23 10:29:55 [core.py:702] File "/opt/tritonserver/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 745, in _process_engine_step (EngineCore_0 pid=195) ERROR 09-23 10:29:55 [core.py:702] outputs, model_executed = self.step_fn() (Engin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;samp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: V1 scheduler is crashing in concurrent scenarios bug;stale ### Your current environment ### 🐛 Describe the bug We are running vllm on Triton, and since we upgraded to the new V1, we are finding that vllm is rando...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: le. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: r current environment ### 🐛 Describe the bug We are running vllm on Triton, and since we upgraded to the new V1, we are finding that vllm is randomly dying when we are stressing the GPU. The error is this: ``` (EngineCo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: p (EngineCore_0 pid=195) ERROR 09-23 10:29:55 [core.py:702] outputs, model_executed = self.step_fn() (EngineCore_0 pid=195) ERROR 09-23 10:29:55 [core.py:702] ^^^^^^^^^^^^^^ (EngineCore_0 pid=195) ERROR 09-23 10:29:55 [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
