# vllm-project/vllm#31631: [CI Failure]:  mi325_1: V1 Test others

| 字段 | 值 |
| --- | --- |
| Issue | [#31631](https://github.com/vllm-project/vllm/issues/31631) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_1: V1 Test others

### Issue 正文摘录

### Name of failing test `pytest -s -v -m 'not cpu_test' v1/kv_connector/unit` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test `test_abort_timeout_on_prefiller[ray]` because: ```log 2026-01-02 13:32:35 CST E File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py", line 809, in __init__ 2026-01-02 13:32:35 CST E raise RuntimeError("NIXL is not available") 2026-01-02 13:32:35 CST E RuntimeError: NIXL is not available ``` We expect this to be fixed once the new base ROCm Docker image is released after https://github.com/vllm-project/vllm/pull/31460. ### 📝 History of failing test Last success: https://buildkite.com/vllm/amd-ci/builds/2223 First fail: https://buildkite.com/vllm/amd-ci/builds/2253

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_1: V1 Test others ci-failure ### Name of failing test `pytest -s -v -m 'not cpu_test' v1/kv_connector/unit` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by extern
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: v1/kv_connector/unit` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test `test_abort_timeout_on_prefil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: NIXL is not available ``` We expect this to be fixed once the new base ROCm Docker image is released after https://github.com/vllm-project/vllm/pull/31460. ### 📝 History of failing test Last success: https://buildkite.c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: test `pytest -s -v -m 'not cpu_test' v1/kv_connector/unit` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: sformers`) ### 🧪 Describe the failing test Test `test_abort_timeout_on_prefiller[ray]` because: ```log 2026-01-02 13:32:35 CST E File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/kv_transfer/kv_connector/v1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
