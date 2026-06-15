# vllm-project/vllm#27348: [CI Failure]: AssertionError on graph pickler while serializing symint nodes.

| 字段 | 值 |
| --- | --- |
| Issue | [#27348](https://github.com/vllm-project/vllm/issues/27348) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: AssertionError on graph pickler while serializing symint nodes.

### Issue 正文摘录

### Name of failing test tests/lora/test_quant_model.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test reproducible with torch 2.10 ``` (EngineCore_DP0 pid=4544) ERROR 10-15 10:01:02 [core.py:790] AssertionError (EngineCore_DP0 pid=4544) Process EngineCore_DP0: (EngineCore_DP0 pid=4544) Traceback (most recent call last): (EngineCore_DP0 pid=4544) File "/opt/conda/envs/py_3.12/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=4544) self.run() (EngineCore_DP0 pid=4544) File "/opt/conda/envs/py_3.12/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=4544) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=4544) File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 794, in run_engine_core (EngineCore_DP0 pid=4544) raise e (EngineCore_DP0 pid=4544) File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 781, in run_engine_core (EngineCore_DP0 pid=4544) engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=4544) ^^^^...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: symint nodes. ci-failure ### Name of failing test tests/lora/test_quant_model.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 D...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: a/test_quant_model.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test reproducible with torch 2.10 ``` (...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: AssertionError on graph pickler while serializing symint nodes. ci-failure ### Name of failing test tests/lora/test_quant_model.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ]
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/compilation/cuda_graph.py", line 125, in __call__ (EngineCore_DP0 pid=4544) return self.runnable(*args, **kwargs) (EngineCore_DP0 pid=4544) ^^^^^^^^^^^^^^^^^^...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: h pickler while serializing symint nodes. ci-failure ### Name of failing test tests/lora/test_quant_model.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bu...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
