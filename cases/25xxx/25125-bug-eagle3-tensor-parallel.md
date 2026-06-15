# vllm-project/vllm#25125: [Bug]: eagle3  tensor-parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#25125](https://github.com/vllm-project/vllm/issues/25125) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: eagle3  tensor-parallel

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug eage3 not support base model's tensor parallel ? ```code vllm serve /home/models/Qwen3-32B --tensor-parallel-size 4 --speculative_config '{"method": "eagle3","model": "/home/models/Qwen3-32B_eagle3","num_speculative_tokens": 2}' --enforce-eager ``` ```code EngineCore_DP0 pid=2039425) ERROR 09-18 10:17:06 [core.py:712] EngineCore failed to start. (EngineCore_DP0 pid=2039425) ERROR 09-18 10:17:06 [core.py:712] Traceback (most recent call last): (EngineCore_DP0 pid=2039425) ERROR 09-18 10:17:06 [core.py:712] File "/home/wangyxbh/vllm/vllm/v1/engine/core.py", line 703, in run_engine_core (EngineCore_DP0 pid=2039425) ERROR 09-18 10:17:06 [core.py:712] engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=2039425) ERROR 09-18 10:17:06 [core.py:712] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=2039425) ERROR 09-18 10:17:06 [core.py:712] File "/home/wangyxbh/vllm/vllm/v1/engine/core.py", line 502, in __init__ (EngineCore_DP0 pid=2039425) ERROR 09-18 10:17:06 [core.py:712] super().__init__(vllm_config, executor_class, log_stats, (EngineCore_DP0 pid=2039425) ERROR 09-18 10:17:06 [core.py:712] File "/home/wangyxbh/vllm/vl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: current environment ### 🐛 Describe the bug eage3 not support base model's tensor parallel ? ```code vllm serve /home/models/Qwen3-32B --tensor-parallel-size 4 --speculative_config '{"method": "eagle3","model": "/home/mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: /__init__.py", line 109, in run (APIServer pid=2038852) return __asyncio.run( (APIServer pid=2038852) ^^^^^^^^^^^^^^ (APIServer pid=2038852) File "/home/wangyxbh/miniconda3/envs/v0.10.1/lib/python3.12/asyncio/runners.py...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: eagle3 tensor-parallel bug;stale ### Your current environment ### 🐛 Describe the bug eage3 not support base model's tensor parallel ? ```code vllm serve /home/models/Qwen3-32B --tensor-parallel-size 4 --speculati...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rypoints/cli/main.py", line 54, in main (APIServer pid=2038852) args.dispatch_function(args) (APIServer pid=2038852) File "/home/wangyxbh/vllm/vllm/entrypoints/cli/serve.py", line 50, in cmd (APIServer pid=2038852) uvlo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
