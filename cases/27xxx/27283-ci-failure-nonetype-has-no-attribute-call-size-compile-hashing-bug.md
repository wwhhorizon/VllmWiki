# vllm-project/vllm#27283: [CI Failure]: 'NoneType' has no attribute 'call_size'. (compile hashing bug)

| 字段 | 值 |
| --- | --- |
| Issue | [#27283](https://github.com/vllm-project/vllm/issues/27283) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: 'NoneType' has no attribute 'call_size'. (compile hashing bug)

### Issue 正文摘录

### Name of failing test tests/basic_correctness/test_basic_correctness.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This is reproducible by running tests/basic_correctness/test_basic_correctness.py with pytorch nightly (2.10+). ``` (EngineCore_DP0 pid=4029586) (EngineCore_DP0 pid=4029586) Process EngineCore_DP0: (EngineCore_DP0 pid=4029586) Traceback (most recent call last): (EngineCore_DP0 pid=4029586) File "/home/zhxchen17/.conda/envs/pytorch-3.12/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=4029586) self.run() (EngineCore_DP0 pid=4029586) File "/home/zhxchen17/.conda/envs/pytorch-3.12/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=4029586) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=4029586) File "/data/users/zhxchen17/vllm/vllm/v1/engine/core.py", line 797, in run_engine_core (EngineCore_DP0 pid=4029586) raise e (EngineCore_DP0 pid=4029586) File "/data/users/zhxchen17/vllm/vllm/v1/engine/core.py", line 784, in run_engine_core (EngineCore_DP0 pid=4029586) engine_co...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ing test tests/basic_correctness/test_basic_correctness.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: _basic_correctness.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This is reproducible by running te...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: 'NoneType' has no attribute 'call_size'. (compile hashing bug) ci-failure ### Name of failing test tests/basic_correctness/test_basic_correctness.py ### Basic information - [ ] Flaky test - [x] Can reprod
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ribute 'call_size'. (compile hashing bug) ci-failure ### Name of failing test tests/basic_correctness/test_basic_correctness.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: core.py", line 113, in __init__ (EngineCore_DP0 pid=4029586) num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( (EngineCore_DP0 pid=4029586) ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=402...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
