# vllm-project/vllm#34465: [CI Failure]: Intel HPU Test

| 字段 | 值 |
| --- | --- |
| Issue | [#34465](https://github.com/vllm-project/vllm/issues/34465) |
| 状态 | open |
| 标签 | stale;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Intel HPU Test

### Issue 正文摘录

### Name of failing test `vllm/examples/offline_inference/basic/generate.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This is most likely a CI test infra issue. The test ends with: `AttributeError: module 'vllm.envs' has no attribute 'VLLM_TORCH_PROFILER_DIR'. ` ``` (EngineCore_DP0 pid=420) Process EngineCore_DP0: -- (EngineCore_DP0 pid=420) ERROR 02-12 07:04:54 [core.py:1006] EngineCore failed to start. (EngineCore_DP0 pid=420) ERROR 02-12 07:04:54 [core.py:1006] Traceback (most recent call last): (EngineCore_DP0 pid=420) ERROR 02-12 07:04:54 [core.py:1006] File "/workspace/vllm/vllm/v1/engine/core.py", line 996, in run_engine_core (EngineCore_DP0 pid=420) ERROR 02-12 07:04:54 [core.py:1006] engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) (EngineCore_DP0 pid=420) ERROR 02-12 07:04:54 [core.py:1006] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=420) ERROR 02-12 07:04:54 [core.py:1006] File "/workspace/vllm/vllm/v1/engine/core.py", line 740, in __init__ (EngineCore_DP0 pid=420) ERROR 02-12 07:04:54 [core.py:1006] s...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: g test `vllm/examples/offline_inference/basic/generate.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Intel HPU Test stale;ci-failure ### Name of failing test `vllm/examples/offline_inference/basic/generate.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external lib
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: Intel HPU Test stale;ci-failure ### Name of failing test `vllm/examples/offline_inference/basic/generate.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ce/basic/generate.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This is most likely a CI test infr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI Failure]: Intel HPU Test stale;ci-failure ### Name of failing test `vllm/examples/offline_inference/basic/generate.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
