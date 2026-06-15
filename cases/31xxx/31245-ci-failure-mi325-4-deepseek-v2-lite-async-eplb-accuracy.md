# vllm-project/vllm#31245: [CI Failure]:  mi325_4: DeepSeek V2-Lite Async EPLB Accuracy

| 字段 | 值 |
| --- | --- |
| Issue | [#31245](https://github.com/vllm-project/vllm/issues/31245) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_4: DeepSeek V2-Lite Async EPLB Accuracy

### Issue 正文摘录

### Name of failing test `bash .buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh 0.25 1319 8030` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test is flaky on both NVIDIA and ROCm. We are not planning on fixing this yet. We are going to remove this eventually from our CI. This ticket is for tracking purposes. ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/2024 ### CC List. _No response_

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [CI Failure]: mi325_4: DeepSeek V2-Lite Async EPLB Accuracy ci-failure ### Name of failing test `bash .buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh 0.25 1319 8030` ### Basic information...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_4: DeepSeek V2-Lite Async EPLB Accuracy ci-failure ### Name of failing test `bash .buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh 0.25 1319 8030` ### Basic informatio
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi325_4: DeepSeek V2-Lite Async EPLB Accuracy ci-failure ### Name of failing test `bash .buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_async_eplb.sh 0.25 1319 8030` ### Basic information...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### 🧪 Describe the failing test This test is flaky on both NVIDIA and ROCm. We are not planning on fixing this yet. We are going to remove this eventually from our CI. This ticket is for tracking purposes. ### 📝 History...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tion_test/deepseek_v2_lite_ep_async_eplb.sh 0.25 1319 8030` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
