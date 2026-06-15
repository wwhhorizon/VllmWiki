# vllm-project/vllm#23374: [Bug]: Genai-perf tests for run-nightly-benchmark.sh script are not using the dynamic backend for serving engine

| 字段 | 值 |
| --- | --- |
| Issue | [#23374](https://github.com/vllm-project/vllm/issues/23374) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Genai-perf tests for run-nightly-benchmark.sh script are not using the dynamic backend for serving engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Issue Description When running `genai-perf-tests` with the `run-nightly-benchmark.sh` script for the `sglang` framework, we noticed via server logs that, even after specifying `backend=sglang`, the tests were still using the `vllm` backend. Further investigation revealed that the `backend` variable is currently hardcoded to `vllm` in the run command. To ensure flexibility and correct execution, `backend` should be set dynamically—similar to how it is handled in the `serving_tests` portion of the script. ## References - **Hardcoded backend in genai-perf-tests:** [run-nightly-benchmarks.sh#L385](https://github.com/vllm-project/vllm/blob/main/.buildkite/nightly-benchmarks/scripts/run-nightly-benchmarks.sh#L385) - **Correct dynamic backend implementation in serving_tests:** [run-nightly-benchmarks.sh#L231](https://github.com/vllm-project/vllm/blob/main/.buildkite/nightly-benchmarks/scripts/run-nightly-benchmarks.sh#L231) ## Additional Information Please see the attached screenshot for relevant server log output. --- ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: r the `sglang` framework, we noticed via server logs that, even after specifying `backend=sglang`, the tests were still using the `vllm` backend. Further investigation revealed that the `backend` variable is currently h...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Genai-perf tests for run-nightly-benchmark.sh script are not using the dynamic backend for serving engine bug ### Your current environment ### 🐛 Describe the bug ## Issue Description When running `genai-perf-test...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: perf tests for run-nightly-benchmark.sh script are not using the dynamic backend for serving engine bug ### Your current environment ### 🐛 Describe the bug ## Issue Description When running `genai-perf-tests` with the `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: --- ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: htly-benchmarks/scripts/run-nightly-benchmarks.sh#L231) ## Additional Information Please see the attached screenshot for relevant server log output. --- ### Before submitting a new issue... - [x] Make sure you already s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
