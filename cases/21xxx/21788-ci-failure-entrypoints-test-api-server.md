# vllm-project/vllm#21788: [CI Failure]: Entrypoints Test (API Server)

| 字段 | 值 |
| --- | --- |
| Issue | [#21788](https://github.com/vllm-project/vllm/issues/21788) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Entrypoints Test (API Server)

### Issue 正文摘录

### Name of failing test Entrypoints Test (API Server) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/fastcheck/builds/32625#019852a9-ac8e-4a40-aaa2-739d656d892f https://buildkite.com/vllm/fastcheck/builds/32645#01985269-4284-4938-8a37-8979580246f6 ### 📝 History of failing test Seems today ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Entrypoints Test (API Server) ci-failure ### Name of failing test Entrypoints Test (API Server) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g.
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nts Test (API Server) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/fastche...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ure ### Name of failing test Entrypoints Test (API Server) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Entrypoints Test (API Server) ci-failure ### Name of failing test Entrypoints Test (API Server) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
