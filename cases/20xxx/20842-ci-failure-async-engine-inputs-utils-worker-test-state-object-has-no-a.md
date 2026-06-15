# vllm-project/vllm#20842: [CI Failure]: Async Engine, Inputs, Utils, Worker Test: 'State' object has no attribute 'enable_server_load_tracking'

| 字段 | 值 |
| --- | --- |
| Issue | [#20842](https://github.com/vllm-project/vllm/issues/20842) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Async Engine, Inputs, Utils, Worker Test: 'State' object has no attribute 'enable_server_load_tracking'

### Issue 正文摘录

### Name of failing test Async Engine, Inputs, Utils, Worker Test ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```bash [2025-07-11T20:13:34Z] INFO 07-11 13:13:34 [async_llm_engine.py:222] Aborted request 85bac0a6a206462aadb2f9d86b92b5f6. -- | [2025-07-11T20:13:34Z] Task exception was never retrieved | [2025-07-11T20:13:34Z] future: exception=AttributeError("'State' object has no attribute 'enable_server_load_tracking'")> | [2025-07-11T20:13:34Z] Traceback (most recent call last): | [2025-07-11T20:13:34Z] File "/usr/local/lib/python3.12/dist-packages/starlette/datastructures.py", line 668, in __getattr__ | [2025-07-11T20:13:34Z] return self._state[key] | [2025-07-11T20:13:34Z] ~~~~~~~~~~~^^^^^ | [2025-07-11T20:13:34Z] KeyError: 'enable_server_load_tracking' | [2025-07-11T20:13:34Z] | [2025-07-11T20:13:34Z] During handling of the above exception, another exception occurred: | [2025-07-11T20:13:34Z] | [2025-07-11T20:13:34Z] Traceback (most recent call last): | [2025-07-11T20:13:34Z] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/utils.py", line 36, in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Async Engine, Inputs, Utils, Worker Test: 'State' object has no attribute 'enable_server_load_tracking' ci-failure ### Name of failing test Async Engine, Inputs, Utils, Worker Test ### Basic information -
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s, Utils, Worker Test ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```bash [2025-07-11T20:13:34Z] INF...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e of failing test Async Engine, Inputs, Utils, Worker Test ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 5-07-11T20:13:34Z] INFO 07-11 13:13:34 [async_llm_engine.py:222] Aborted request 85bac0a6a206462aadb2f9d86b92b5f6. -- | [2025-07-11T20:13:34Z] Task exception was never retrieved | [2025-07-11T20:13:34Z] future: exceptio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Async Engine, Inputs, Utils, Worker Test: 'State' object has no attribute 'enable_server_load_tracking' ci-failure ### Name of failing test Async Engine, Inputs, Utils, Worker Test ### Basic information -...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
