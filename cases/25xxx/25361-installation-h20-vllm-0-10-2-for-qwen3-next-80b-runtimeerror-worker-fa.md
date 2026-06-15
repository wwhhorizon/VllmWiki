# vllm-project/vllm#25361: [Installation]: H20 vllm==0.10.2  for Qwen3-Next-80B，RuntimeError: Worker failed with error ''staticmethod' object is not callable', please check the stack trace above for the root cause

| 字段 | 值 |
| --- | --- |
| Issue | [#25361](https://github.com/vllm-project/vllm/issues/25361) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: H20 vllm==0.10.2  for Qwen3-Next-80B，RuntimeError: Worker failed with error ''staticmethod' object is not callable', please check the stack trace above for the root cause

### Issue 正文摘录

### Your current environment (EngineCore_DP0 pid=297) ERROR 09-17 15:58:14 [multiproc_executor.py:149] Worker proc VllmWorker-3 died unexpectedly, shutting down executor. (EngineCore_DP0 pid=297) Process EngineCore_DP0: (EngineCore_DP0 pid=297) Traceback (most recent call last): (EngineCore_DP0 pid=297) File "/usr/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap (EngineCore_DP0 pid=297) self.run() (EngineCore_DP0 pid=297) File "/usr/lib/python3.9/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=297) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=297) File "/usr/local/lib/python3.9/dist-packages/vllm/v1/engine/core.py", line 722, in run_engine_core (EngineCore_DP0 pid=297) raise e (EngineCore_DP0 pid=297) File "/usr/local/lib/python3.9/dist-packages/vllm/v1/engine/core.py", line 709, in run_engine_core (EngineCore_DP0 pid=297) engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=297) File "/usr/local/lib/python3.9/dist-packages/vllm/v1/engine/core.py", line 505, in __init__ (EngineCore_DP0 pid=297) super().__init__(vllm_config, executor_class, log_stats, (EngineCore_DP0 pid=297) File "/usr/local/lib/python3.9/dist-packa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Installation]: H20 vllm==0.10.2 for Qwen3-Next-80B，RuntimeError: Worker failed with error ''staticmethod' object is not callable', please check the stack trace above for the root cause installation;stale ### Your curre...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: H20 vllm==0.10.2 for Qwen3-Next-80B，RuntimeError: Worker failed with error ''staticmethod' object is not callable', please check the stack trace above for the root cause installation;stale ### Your curren
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ble', please check the stack trace above for the root cause installation;stale ### Your current environment (EngineCore_DP0 pid=297) ERROR 09-17 15:58:14 [multiproc_executor.py:149] Worker proc VllmWorker-3 died unexpec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
