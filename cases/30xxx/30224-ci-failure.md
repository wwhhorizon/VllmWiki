# vllm-project/vllm#30224: [CI Failure]:

| 字段 | 值 |
| --- | --- |
| Issue | [#30224](https://github.com/vllm-project/vllm/issues/30224) |
| 状态 | closed |
| 标签 | stale;needs reproduction |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:

### Issue 正文摘录

### Name of failing test t, h, w = image_grid_thw[image_index] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test (EngineCore_DP0 pid=268) Traceback (most recent call last): (EngineCore_DP0 pid=268) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=268) self.run() (EngineCore_DP0 pid=268) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=268) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=268) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 847, in run_engine_core (EngineCore_DP0 pid=268) raise e (EngineCore_DP0 pid=268) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 836, in run_engine_core (EngineCore_DP0 pid=268) engine_core.run_busy_loop() (EngineCore_DP0 pid=268) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 863, in run_busy_loop (EngineCore_DP0 pid=268) self._process_engine_step() (EngineCore_DP0 pid=268) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", l...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ame of failing test t, h, w = image_grid_thw[image_index] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing tes...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [CI Failure]: stale;needs reproduction ### Name of failing test t, h, w = image_grid_thw[image_index] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: grid_thw[image_index] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test (EngineCore_DP0 pid=268) Traceback...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: stale;needs reproduction ### Name of failing test t, h, w = image_grid_thw[image_index] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: stale;needs reproduction ### Name of failing test t, h, w = image_grid_thw[image_index] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
