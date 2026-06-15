# vllm-project/vllm#17681: [Feature]: Support for streaming N tokens at a time in AsyncLLMEngine

| 字段 | 值 |
| --- | --- |
| Issue | [#17681](https://github.com/vllm-project/vllm/issues/17681) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for streaming N tokens at a time in AsyncLLMEngine

### Issue 正文摘录

### 🚀 The feature, motivation and pitch To reduce network overhead, we propose a mechanism to stream N tokens at a time instead of just 1 in AsyncLLMEngine. To do this, we propose introducing a parameter `stream_n` that controls how many tokens are emitted at a time during streaming. As a design decision (and to support future features regarding streaming), this feature could be introduced in a separate StreamingParams class (as opposed to modifying SamplingParams which historically has only related to sampling). ### Alternatives _No response_ ### Additional context A working version is already live in our internal fork and has been validated, so I can make a PR if this is agreed to be useful. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: time instead of just 1 in AsyncLLMEngine. To do this, we propose introducing a parameter `stream_n` that controls how many tokens are emitted at a time during streaming. As a design decision (and to support future featu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e, motivation and pitch To reduce network overhead, we propose a mechanism to stream N tokens at a time instead of just 1 in AsyncLLMEngine. To do this, we propose introducing a parameter `stream_n` that controls how ma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ure]: Support for streaming N tokens at a time in AsyncLLMEngine feature request;stale ### 🚀 The feature, motivation and pitch To reduce network overhead, we propose a mechanism to stream N tokens at a time instead of j...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
