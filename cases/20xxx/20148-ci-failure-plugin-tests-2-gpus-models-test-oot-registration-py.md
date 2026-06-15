# vllm-project/vllm#20148: [CI Failure]: Plugin Tests (2 GPUs) - models/test_oot_registration.py

| 字段 | 值 |
| --- | --- |
| Issue | [#20148](https://github.com/vllm-project/vllm/issues/20148) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Plugin Tests (2 GPUs) - models/test_oot_registration.py

### Issue 正文摘录

### Name of failing test `models/test_oot_registration.py::test_oot_registration_embedding` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The `models/test_oot_registration.py::test_oot_registration_embedding` test seems to be failing in CI consistently with a context length OOM https://buildkite.com/vllm/ci/builds/22737/steps/canvas?sid=0197acae-970a-43ee-9fef-108d8a58da0c#0197acae-98db-423d-8af9-eb4eb401f1b4/212-1320 ``` [2025-06-26T16:27:15Z] ERROR 06-26 09:27:15 [core.py:519] ValueError: To serve at least one request with the models's max seq len (8192), (2.63 GiB KV cache is needed, which is larger than the available KV cache memory (1.64 GiB). Based on the available memory, the estimated maximum model length is 5088. Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. ``` ### 📝 History of failing test Not sure, maybe related to FP32 weights? I have a prospective fix https://github.com/vllm-project/vllm/pull/20144 ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Plugin Tests (2 GPUs) - models/test_oot_registration.py ci-failure ### Name of failing test `models/test_oot_registration.py::test_oot_registration_embedding` ### Basic information - [ ] Flaky test - [x]
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: dding` test seems to be failing in CI consistently with a context length OOM https://buildkite.com/vllm/ci/builds/22737/steps/canvas?sid=0197acae-970a-43ee-9fef-108d8a58da0c#0197acae-98db-423d-8af9-eb4eb401f1b4/212-1320...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: Plugin Tests (2 GPUs) - models/test_oot_registration.py ci-failure ### Name of failing test `models/test_oot_registration.py::test_oot_registration_embedding` ### Basic information - [ ] Flaky test - [x] C...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: gistration_embedding` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The `models/test_oot_registration....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 5Z] ERROR 06-26 09:27:15 [core.py:519] ValueError: To serve at least one request with the models's max seq len (8192), (2.63 GiB KV cache is needed, which is larger than the available KV cache memory (1.64 GiB). Based o...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
