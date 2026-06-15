# vllm-project/vllm#17697: [Feature]: Addition of pre-built AMD wheel packages

| 字段 | 值 |
| --- | --- |
| Issue | [#17697](https://github.com/vllm-project/vllm/issues/17697) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Addition of pre-built AMD wheel packages

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, The installation on AMD GPU currently requires either to use heavy docker images, or to build from source. While docker is great for some things, it is a pretty heavy thing that does not fit well in some infrastructures. It would be great if prebuilt wheel files were provided for AMD, similarly to what PyTorch does. It would lower the barrier to entry for some types of users that want to use AMD machines. Thank you for considering this, Best regards, Epliz ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Feature]: Addition of pre-built AMD wheel packages feature request;stale ### 🚀 The feature, motivation and pitch Hi, The installation on AMD GPU currently requires either to use heavy docker images, or to build from so...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Addition of pre-built AMD wheel packages feature request;stale ### 🚀 The feature, motivation and pitch Hi, The installation on AMD GPU currently requires either to use heavy docker images, or to build from so...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
