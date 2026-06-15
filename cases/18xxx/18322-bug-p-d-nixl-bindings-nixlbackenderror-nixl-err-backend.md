# vllm-project/vllm#18322: [Bug][P/D]: nixl._bindings.nixlBackendError: NIXL_ERR_BACKEND

| 字段 | 值 |
| --- | --- |
| Issue | [#18322](https://github.com/vllm-project/vllm/issues/18322) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][P/D]: nixl._bindings.nixlBackendError: NIXL_ERR_BACKEND

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run the script `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`, I encountered this error. ``` INFO 05-18 12:25:43 [gpu_model_runner.py:1521] Model loading took 14.9889 GiB and 2.689499 seconds [mlp-dgx-01:45435:0:45788] Caught signal 11 (Segmentation fault: address not mapped to object at address 0x7f48000689dc) [mlp-dgx-01:45430:0:45786] Caught signal 11 (Segmentation fault: address not mapped to object at address 0x7fb6241a39dc) INFO 05-18 12:25:44 [kv_cache_utils.py:637] GPU KV cache size: 442,160 tokens INFO 05-18 12:25:44 [kv_cache_utils.py:640] Maximum concurrency for 131,072 tokens per request: 3.37x ERROR 05-18 12:25:44 [core.py:489] EngineCore failed to start. ERROR 05-18 12:25:44 [core.py:489] Traceback (most recent call last): ERROR 05-18 12:25:44 [core.py:489] File "/data1/lzw/venvs/nixl/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 480, in run_engine_core ERROR 05-18 12:25:44 [core.py:489] engine_core = EngineCoreProc(*args, **kwargs) ERROR 05-18 12:25:44 [core.py:489] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 05-18 12:25:44 [core.py:489] File "/data1/lzw/venvs/nixl/lib/python3.12/site-p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. development attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cache;cuda;operator;sampling;triton...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug][P/D]: nixl._bindings.nixlBackendError: NIXL_ERR_BACKEND bug ### Your current environment ### 🐛 Describe the bug When I run the script `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`, I encountered th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: curacy_test.sh`, I encountered this error. ``` INFO 05-18 12:25:43 [gpu_model_runner.py:1521] Model loading took 14.9889 GiB and 2.689499 seconds [mlp-dgx-01:45435:0:45788] Caught signal 11 (Segmentation fault: address...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 25:44 [kv_cache_utils.py:640] Maximum concurrency for 131,072 tokens per request: 3.37x ERROR 05-18 12:25:44 [core.py:489] EngineCore failed to start. ERROR 05-18 12:25:44 [core.py:489] Traceback (most recent call last)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
