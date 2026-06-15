# vllm-project/vllm#17431: [Bug]: A800 GPU set VLLM_USE_V1=1 ValueError: No available memory for the cache blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#17431](https://github.com/vllm-project/vllm/issues/17431) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: A800 GPU set VLLM_USE_V1=1 ValueError: No available memory for the cache blocks

### Issue 正文摘录

### Your current environment if I set VLLM_USE_V1=0 ,vllm server can start success. otherwise fail. ### 🐛 Describe the bug ### success case ``` VLLM_USE_V1=0 /home/python_vllm_env_085/bin/python -m vllm.entrypoints.openai.api_server --model /root/yjpzmodel/basemodel/Qwen3-8B --served-model-name Qwen3-8B --gpu-memory-utilization 0.4 --port 8001 ``` ### error case ``` /home/python_vllm_env_085/bin/python -m vllm.entrypoints.openai.api_server --model /root/yjpzmodel/basemodel/Qwen3-8B --served-model-name Qwen3-8B --gpu-memory-utilization 0.4 --port 8001 ``` ### error log ``` INFO 04-30 10:20:35 [monitor.py:33] torch.compile takes 13.93 s in total ERROR 04-30 10:20:36 [core.py:396] EngineCore failed to start. ERROR 04-30 10:20:36 [core.py:396] Traceback (most recent call last): ERROR 04-30 10:20:36 [core.py:396] File "/home/python_vllm_env_085/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 387, in run_engine_core ERROR 04-30 10:20:36 [core.py:396] engine_core = EngineCoreProc(*args, **kwargs) ERROR 04-30 10:20:36 [core.py:396] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-30 10:20:36 [core.py:396] File "/home/python_vllm_env_085/lib/python3.11/site-packages/vllm/v1/engine/core....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ort 8001 ``` ### error log ``` INFO 04-30 10:20:35 [monitor.py:33] torch.compile takes 13.93 s in total ERROR 04-30 10:20:36 [core.py:396] EngineCore failed to start. ERROR 04-30 10:20:36 [core.py:396] Traceback (most r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: thon_vllm_env_085/bin/python -m vllm.entrypoints.openai.api_server --model /root/yjpzmodel/basemodel/Qwen3-8B --served-model-name Qwen3-8B --gpu-memory-utilization 0.4 --port 8001 ``` ### error case ``` /home/python_vll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: t VLLM_USE_V1=1 ValueError: No available memory for the cache blocks bug;stale ### Your current environment if I set VLLM_USE_V1=0 ,vllm server can start success. otherwise fail. ### 🐛 Describe the bug ### success case...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: el;frontend_api;hardware_porting;model_support;speculative_decoding cuda;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
