# vllm-project/vllm#20150: [CI Failure]: Distributed Tests (2 GPUs) - v1/test_async_llm_dp.py::test_load

| 字段 | 值 |
| --- | --- |
| Issue | [#20150](https://github.com/vllm-project/vllm/issues/20150) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Distributed Tests (2 GPUs) - v1/test_async_llm_dp.py::test_load

### Issue 正文摘录

### Name of failing test `v1/test_async_llm_dp.py::test_load` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/builds/22751/steps/canvas?sid=0197ada3-fac8-4883-be17-6763399d2937 ``` [2025-06-26T19:18:54Z] (DPEngineCoreActor pid=1153) Exception raised in creation task: The actor died because of an error raised in its creation task, ray::DPEngineCoreActor.__init__() (pid=1153, ip=172.16.0.2, actor_id=999e66988abea09590bcd81301000000, repr= ) [2025-06-26T19:18:54Z] (DPEngineCoreActor pid=1153) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-06-26T19:18:54Z] (DPEngineCoreActor pid=1153) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-06-26T19:18:54Z] (DPEngineCoreActor pid=1153) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 930, in __init__ [2025-06-26T19:18:54Z] (DPEngineCoreActor pid=1153) super().__init__(vllm_config, on_head_node, "", executor_class, [2025-06-26T19:18:54Z] (DPEngineCoreActor pid=1153) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 768, in __init__ [2025-06-26T19:18:54Z] (DPEngine...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Distributed Tests (2 GPUs) - v1/test_async_llm_dp.py::test_load ci-failure ### Name of failing test `v1/test_async_llm_dp.py::test_load` ### Basic information - [x] Flaky test - [ ] Can reproduce locally
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Name of failing test `v1/test_async_llm_dp.py::test_load` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing tes...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: llm_dp.py::test_load` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/buil...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s failed to listen on any local network address. port: 42369, useIpv6: false, code: -98, name: EADDRINUSE, message: address already in use [2025-06-26T19:18:54Z] (DPEngineCoreActor pid=1151) RuntimeError: nonce == retur...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Distributed Tests (2 GPUs) - v1/test_async_llm_dp.py::test_load ci-failure ### Name of failing test `v1/test_async_llm_dp.py::test_load` ### Basic information - [x] Flaky test - [ ] Can reproduce locally -...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
