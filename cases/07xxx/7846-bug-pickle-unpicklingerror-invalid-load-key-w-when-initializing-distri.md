# vllm-project/vllm#7846: [Bug]: _pickle.UnpicklingError: invalid load key, 'W' when initializing distributed environment with vllm 0.5.5

| 字段 | 值 |
| --- | --- |
| Issue | [#7846](https://github.com/vllm-project/vllm/issues/7846) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: _pickle.UnpicklingError: invalid load key, 'W' when initializing distributed environment with vllm 0.5.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I attempted to use vllm==0.5.5 and ran the following script: ```bash python -m vllm.entrypoints.openai.api_server \ --model $MODEL_PATH \ --tensor-parallel-size 2 \ --seed 0 \ --gpu-memory-utilization 0.7 ``` However, I encountered the following error while loading the model: ``` ERROR 08-25 16:17:39 multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 1049 died, exit code: -15 INFO 08-25 16:17:39 multiproc_worker_utils.py:123] Killing local vLLM worker processes Traceback (most recent call last): File "/root/miniconda3/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/root/miniconda3/lib/python3.11/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/root/miniconda3/lib/python3.11/site-packages/vllm/entrypoints/openai/rpc/server.py", line 230, in run_rpc_server server = AsyncEngineRPCServer(async_engine_args, usage_context, rpc_path) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/miniconda3/lib/python3.11/site-packages/vllm/entrypoints/openai/rpc/server.py", line 31, in __init__ self.engine = AsyncLLMEngine.from_eng...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;triton build_error;crash env_dependency Your c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ng script: ```bash python -m vllm.entrypoints.openai.api_server \ --model $MODEL_PATH \ --tensor-parallel-size 2 \ --seed 0 \ --gpu-memory-utilization 0.7 ``` However, I encountered the following error while loading the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: el;frontend_api;hardware_porting;model_support;speculative_decoding cuda;triton build_error;crash env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
