# vllm-project/vllm#30929: [CI Failure]:  mi325_4: DeepSeek V2-Lite Async EPLB Accuracy

| 字段 | 值 |
| --- | --- |
| Issue | [#30929](https://github.com/vllm-project/vllm/issues/30929) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_4: DeepSeek V2-Lite Async EPLB Accuracy

### Issue 正文摘录

### Name of failing test `bash .buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh 0.25 1319 8030` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test evaluates DeepSeek on EPLB. ### 📝 History of failing test Test started failing 12/11/2025 with buildkite run 1575 ### CC List. _No response_

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure]: mi325_4: DeepSeek V2-Lite Async EPLB Accuracy ci-failure ### Name of failing test `bash .buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh 0.25 1319 8030` ### Basic information...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [CI Failure]: mi325_4: DeepSeek V2-Lite Async EPLB Accuracy ci-failure ### Name of failing test `bash .buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh 0.25 1319 8030` ### Basic information...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_4: DeepSeek V2-Lite Async EPLB Accuracy ci-failure ### Name of failing test `bash .buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh 0.25 1319 8030` ### Basic informatio
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tion_test/deepseek_v2_lite_ep_async_eplb.sh 0.25 1319 8030` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
