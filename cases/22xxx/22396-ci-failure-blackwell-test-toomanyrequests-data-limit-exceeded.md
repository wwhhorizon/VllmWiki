# vllm-project/vllm#22396: [CI Failure]: Blackwell Test - toomanyrequests: Data limit exceeded

| 字段 | 值 |
| --- | --- |
| Issue | [#22396](https://github.com/vllm-project/vllm/issues/22396) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Blackwell Test - toomanyrequests: Data limit exceeded

### Issue 正文摘录

### Name of failing test fails before tests run ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This is an infrastructure setup issue. `docker login` is needed on the host. Discussed on slack here: https://vllm-dev.slack.com/archives/C07R5PAL2L9/p1754403287892619 ### 📝 History of failing test Failing consistently ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Blackwell Test - toomanyrequests: Data limit exceeded ci-failure ### Name of failing test fails before tests run ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: Blackwell Test - toomanyrequests: Data limit exceeded ci-failure ### Name of failing test fails before tests run ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ails before tests run ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This is an infrastructure setup is...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [CI Failure]: Blackwell Test - toomanyrequests: Data limit exceeded ci-failure ### Name of failing test fails before tests run ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ci-failure ### Name of failing test fails before tests run ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
