# vllm-project/vllm#35547: [Bug]: Long weight loading results in server start failure

| 字段 | 值 |
| --- | --- |
| Issue | [#35547](https://github.com/vllm-project/vllm/issues/35547) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Long weight loading results in server start failure

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When loading weights take very long (e.g., first-time loading), the server fails to start with the following error: ``` Loading safetensors checkpoint shards: 64% Completed | 105/163 [09:30<04:59, 5.16s/it] Loading safetensors checkpoint shards: 65% Completed | 106/163 [09:36<05:20, 5.63s/it] (ApiServer_5 pid=463645) Process ApiServer_5: (ApiServer_5 pid=463645) Traceback (most recent call last): (ApiServer_5 pid=463645) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (ApiServer_5 pid=463645) self.run() (ApiServer_5 pid=463645) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (ApiServer_5 pid=463645) self._target(*self._args, **self._kwargs) (ApiServer_5 pid=463645) File "vllm/vllm/entrypoints/cli/serve.py", line 301, in run_api_server_worker_proc (ApiServer_5 pid=463645) uvloop.run( (ApiServer_5 pid=463645) File "vllm/.venv/lib/python3.12/site-packages/uvloop/__init__.py", line 96, in run (ApiServer_5 pid=463645) return __asyncio.run( (ApiServer_5 pid=463645) ^^^^^^^^^^^^^^ (ApiServer_5 pid=463645) File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run (ApiServer_5 p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: /__init__.py", line 96, in run (ApiServer_5 pid=463645) return __asyncio.run( (ApiServer_5 pid=463645) ^^^^^^^^^^^^^^ (ApiServer_5 pid=463645) File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run (ApiServer_5...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rk. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _engine_args (ApiServer_5 pid=463645) async_llm = AsyncLLM.from_vllm_config( (ApiServer_5 pid=463645) ^^^^^^^^^^^^^^^^^^^^^^^^^^ (ApiServer_5 pid=463645) File "vllm/vllm/v1/engine/async_llm.py", line 223, in from_vllm_c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: raise TimeoutError( (ApiServer_5 pid=463645) TimeoutError: Timed out waiting for engines to send initial message on input socket. ``` Weight will continue to load but will eventually fail to start. Running the server ag...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
