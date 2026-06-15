# vllm-project/vllm#16009: [Bug]: TypeError: __init__() missing 1 required positional argument: 'inner_exception'

| 字段 | 值 |
| --- | --- |
| Issue | [#16009](https://github.com/vllm-project/vllm/issues/16009) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: __init__() missing 1 required positional argument: 'inner_exception'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` python export CUDA_VISIBLE_DEVICES=0,1 vllm serve "QwQ-32B" \ --host 0.0.0.0 \ --port 44390 \ --tensor-parallel-size 2 ``` ``` ERROR 04-03 18:30:13 [core.py:343] EngineCore hit an exception: Traceback (most recent call last): ERROR 04-03 18:30:13 [core.py:343] File "/envs/vllm/lib/python3.9/site-packages/vllm/v1/engine/core.py", line 335, in run_engine_core ERROR 04-03 18:30:13 [core.py:343] engine_core = EngineCoreProc(*args, **kwargs) ERROR 04-03 18:30:13 [core.py:343] File "/envs/vllm/lib/python3.9/site-packages/vllm/v1/engine/core.py", line 290, in __init__ ERROR 04-03 18:30:13 [core.py:343] super().__init__(vllm_config, executor_class, log_stats) ERROR 04-03 18:30:13 [core.py:343] File "/envs/vllm/lib/python3.9/site-packages/vllm/v1/engine/core.py", line 63, in __init__ ERROR 04-03 18:30:13 [core.py:343] num_gpu_blocks, num_cpu_blocks = self._initialize_kv_caches( ERROR 04-03 18:30:13 [core.py:343] File "/envs/vllm/lib/python3.9/site-packages/vllm/v1/engine/core.py", line 122, in _initialize_kv_caches ERROR 04-03 18:30:13 [core.py:343] available_gpu_memory = self.model_executor.determine_available_memory() ERROR 04-03 18...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: __() missing 1 required positional argument: 'inner_exception' bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug ``` python export CUDA_VISIBLE_DEVICES=0,1 vllm serve "QwQ-32B" \ --host 0.0.0.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: # Your current environment ### 🐛 Describe the bug ``` python export CUDA_VISIBLE_DEVICES=0,1 vllm serve "QwQ-32B" \ --host 0.0.0.0 \ --port 44390 \ --tensor-parallel-size 2 ``` ``` ERROR 04-03 18:30:13 [core.py:343] Eng...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: in __init__ ERROR 04-03 18:30:13 [core.py:343] super().__init__(vllm_config, executor_class, log_stats) ERROR 04-03 18:30:13 [core.py:343] File "/envs/vllm/lib/python3.9/site-packages/vllm/v1/engine/core.py", line 63, i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: sing 1 required positional argument: 'inner_exception' bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug ``` python export CUDA_VISIBLE_DEVICES=0,1 vllm serve "QwQ-32B" \ --host 0.0.0.0 \ --por...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
