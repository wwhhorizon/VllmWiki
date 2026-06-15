# vllm-project/vllm#16142: [Bug]: H20*TP16，can't start service, get error: Cannot allocate memory

| 字段 | 值 |
| --- | --- |
| Issue | [#16142](https://github.com/vllm-project/vllm/issues/16142) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: H20*TP16，can't start service, get error: Cannot allocate memory

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when l use H20*TP16 with DeepSeek-R1, l get some terrible error: 2025-04-07 01:43:36,226 INFO worker.py:1654 -- Connecting to existing Ray cluster at address: 7.216.55.143:6379... 2025-04-07 01:43:36,236 INFO worker.py:1832 -- Connected to Ray cluster. View the dashboard at 127.0.0.1:8265 ERROR 04-07 01:43:36 [core.py:390] EngineCore hit an exception: Traceback (most recent call last): ERROR 04-07 01:43:36 [core.py:390] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 378, in run_engine_core ERROR 04-07 01:43:36 [core.py:390] engine_core = EngineCoreProc(*args, **kwargs) ERROR 04-07 01:43:36 [core.py:390] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 319, in __init__ ERROR 04-07 01:43:36 [core.py:390] super().__init__(vllm_config, executor_class, log_stats) ERROR 04-07 01:43:36 [core.py:390] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 67, in __init__ ERROR 04-07 01:43:36 [core.py:390] self.model_executor = executor_class(vllm_config) ERROR 04-07 01:43:36 [core.py:390] File "/usr/local/lib/python3.10/dist-packages/vllm/executor/executor_base.p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: led ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: in __init__ ERROR 04-07 01:43:36 [core.py:390] super().__init__(vllm_config, executor_class, log_stats) ERROR 04-07 01:43:36 [core.py:390] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 67,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: H20*TP16，can't start service, get error: Cannot allocate memory bug;stale ### Your current environment ### 🐛 Describe the bug when l use H20*TP16 with DeepSeek-R1, l get some terrible error: 2025-04-07 01:43:36,226...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
