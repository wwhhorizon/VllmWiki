# vllm-project/vllm#11728: [Feature]: Publish an Arm image for GH200

| 字段 | 值 |
| --- | --- |
| Issue | [#11728](https://github.com/vllm-project/vllm/issues/11728) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Publish an Arm image for GH200

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently all users need to build and publish their own images. This isn't great for user experience. It would be nice if vLLM publishes an official arm image that works on GH200. ### Alternatives Build yourself using steps here: https://docs.vllm.ai/en/stable/serving/deploying_with_docker.html#building-for-arm64-aarch64 ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ale ### 🚀 The feature, motivation and pitch Currently all users need to build and publish their own images. This isn't great for user experience. It would be nice if vLLM publishes an official arm image that works on GH...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Publish an Arm image for GH200 feature request;stale ### 🚀 The feature, motivation and pitch Currently all users need to build and publish their own images. This isn't great for user experience. It would be n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: vllm.ai/en/stable/serving/deploying_with_docker.html#building-for-arm64-aarch64 ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and ask...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
