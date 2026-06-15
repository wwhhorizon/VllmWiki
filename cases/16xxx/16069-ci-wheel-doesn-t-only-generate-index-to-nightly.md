# vllm-project/vllm#16069: [CI]: wheel doesn't only generate index to nightly

| 字段 | 值 |
| --- | --- |
| Issue | [#16069](https://github.com/vllm-project/vllm/issues/16069) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: wheel doesn't only generate index to nightly

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It seems wheel building pipeling didn’t produce a wheel server formatted index.html so install from wheels.vllm.ai/v0.8.0rc1 doesn’t work vs /nightly. Clues in https://github.com/vllm-project/vllm/blob/dccf535f8edb861e95cf2f0b3512e1fd737265c2/.buildkite/upload-wheels.sh#L44 and we should generate index properly for other version too. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [CI]: wheel doesn't only generate index to nightly feature request;stale ### 🚀 The feature, motivation and pitch It seems wheel building pipeling didn’t produce a wheel server formatted index.html so install from wheels.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [CI]: wheel doesn't only generate index to nightly feature request;stale ### 🚀 The feature, motivation and pitch It seems wheel building pipeling didn’t produce a wheel server formatted index.html so install from wheels...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nd pitch It seems wheel building pipeling didn’t produce a wheel server formatted index.html so install from wheels.vllm.ai/v0.8.0rc1 doesn’t work vs /nightly. Clues in https://github.com/vllm-project/vllm/blob/dccf535f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
