# vllm-project/vllm#35419: [Feature]: Publish macOS wheels

| 字段 | 值 |
| --- | --- |
| Issue | [#35419](https://github.com/vllm-project/vllm/issues/35419) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Publish macOS wheels

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Using and developing vLLM on macOS would be much easier if the project would publish official binary wheels. Example: https://pypi.org/project/torch/2.10.0/#files > torch-2.10.0-cp314-cp314-macosx_14_0_arm64.whl ### Alternatives Every potential macOS user has to try to build manually in order to install vLLM. ### Additional context The standard project to build wheels is [cibuildwheel](https://github.com/pypa/cibuildwheel). Migrating the build would make it much easier to support all platforms and Python versions in the future. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Feature]: Publish macOS wheels feature request;stale ### 🚀 The feature, motivation and pitch Using and developing vLLM on macOS would be much easier if the project would publish official binary wheels. Example: https:/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Publish macOS wheels feature request;stale ### 🚀 The feature, motivation and pitch Using and developing vLLM on macOS would be much easier if the project would publish official binary wheels. Example: https:/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: re. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
