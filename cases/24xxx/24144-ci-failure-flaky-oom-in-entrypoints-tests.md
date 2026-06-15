# vllm-project/vllm#24144: [CI Failure]: Flaky OOM in Entrypoints Tests

| 字段 | 值 |
| --- | --- |
| Issue | [#24144](https://github.com/vllm-project/vllm/issues/24144) |
| 状态 | closed |
| 标签 | stale;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Flaky OOM in Entrypoints Tests

### Issue 正文摘录

### Name of failing test entrypoints tests ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Random OOMs in the CI. This happens after a successful test. VLLM does not clean itself up properly An example case is here: - https://buildkite.com/vllm/fastcheck/builds/39064#0199090f-5115-4814-b60a-941df8fb3f9b/7-2101 This is very frustrating to our contributors. It would be great to understand why this happens and see if there is any mitigation against showdown in the CI. ### 📝 History of failing test x ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Flaky OOM in Entrypoints Tests stale;ci-failure ### Name of failing test entrypoints tests ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug i
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: st entrypoints tests ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Random OOMs in the CI. This happens...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [CI Failure]: Flaky OOM in Entrypoints Tests stale;ci-failure ### Name of failing test entrypoints tests ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tale;ci-failure ### Name of failing test entrypoints tests ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI Failure]: Flaky OOM in Entrypoints Tests stale;ci-failure ### Name of failing test entrypoints tests ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
