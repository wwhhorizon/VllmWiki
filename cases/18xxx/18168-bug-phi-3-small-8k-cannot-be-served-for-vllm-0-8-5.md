# vllm-project/vllm#18168: [Bug]: Phi-3-small-8k cannot be served for vllm >= 0.8.5

| 字段 | 值 |
| --- | --- |
| Issue | [#18168](https://github.com/vllm-project/vllm/issues/18168) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Phi-3-small-8k cannot be served for vllm >= 0.8.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running the following code encounters an exception during model build: `TypeError: cannot pickle '_thread.RLock' object` ```python python -m vllm.entrypoints.openai.api_server \ --tensor-parallel-size 1 \ --host 0.0.0.0 --port 8080 \ --model microsoft/Phi-3-small-8k-instruct \ --gpu-memory-utilization 0.90 \ --trust-remote-code \ --guided-decoding-backend guidance ``` Traceback: ``` Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File ".../.venv/vllm/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 1130, in uvloop.run(run_server(args)) File ".../.venv/vllm/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run return runner.run(wrapper()) ^^^^^^^^^^^^^^^^^^^^^ File ".../.venv/vllm/lib/python3.11/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File ".../.venv/vllm/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper return await main ^^^^^^^^^^ File ".../.venv/vllm/lib/python3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: the bug Running the following code encounters an exception during model build: `TypeError: cannot pickle '_thread.RLock' object` ```python python -m vllm.entrypoints.openai.api_server \ --tensor-parallel-size 1 \ --host...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Phi-3-small-8k cannot be served for vllm >= 0.8.5 bug;stale ### Your current environment ### 🐛 Describe the bug Running the following code encounters an exception during model build: `TypeError: cannot pickle '_t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: emory-utilization 0.90 \ --trust-remote-code \ --guided-decoding-backend guidance ``` Traceback: ``` Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File ".....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cribe the bug Running the following code encounters an exception during model build: `TypeError: cannot pickle '_thread.RLock' object` ```python python -m vllm.entrypoints.openai.api_server \ --tensor-parallel-size 1 \...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Phi-3-small-8k cannot be served for vllm >= 0.8.5 bug;stale ### Your current environment ### 🐛 Describe the bug Running the following code encounters an exception during model build: `TypeError: cannot pickle '_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
