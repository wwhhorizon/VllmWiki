# vllm-project/vllm#33603: [Bug] [CI, Build, and Release] Lost vllm against PyTorch nightly signal since Jan 28, 2026

| 字段 | 值 |
| --- | --- |
| Issue | [#33603](https://github.com/vllm-project/vllm/issues/33603) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] [CI, Build, and Release] Lost vllm against PyTorch nightly signal since Jan 28, 2026

### Issue 正文摘录

### Your current environment Running in Nightly CI ### 🐛 Describe the bug Related PR: https://github.com/vllm-project/vllm/pull/30443 Last successful run: https://buildkite.com/vllm/ci/builds/48643#019bfe41-7f72-4e06-b437-9e08fb37c4d2 Current runs do not contain this signal any more: https://buildkite.com/vllm/ci/builds/49537#_ I believe we want to use this signal before PyTorch branch cut. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug] [CI, Build, and Release] Lost vllm against PyTorch nightly signal since Jan 28, 2026 bug;stale ### Your current environment Running in Nightly CI ### 🐛 Describe the bug Related PR: https://github.com/vllm-project/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ut. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Release] Lost vllm against PyTorch nightly signal since Jan 28, 2026 bug;stale ### Your current environment Running in Nightly CI ### 🐛 Describe the bug Related PR: https://github.com/vllm-project/vllm/pull/30443 Last s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
