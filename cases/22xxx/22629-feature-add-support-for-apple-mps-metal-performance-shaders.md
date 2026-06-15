# vllm-project/vllm#22629: [Feature]: Add support for Apple MPS(Metal Performance Shaders)

| 字段 | 值 |
| --- | --- |
| Issue | [#22629](https://github.com/vllm-project/vllm/issues/22629) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add support for Apple MPS(Metal Performance Shaders)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I have been trying to install vLLM on MacOS M3 but installation fails most of the time. I have used both pip and uv approaches to install dependencies. Apart from issues with my machine specific installation, vLLM only has CPU enabled for MacOS. This issue is for adding GPU support for MacOS via Apple MPS(Metal Performance Shaders) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e request ### 🚀 The feature, motivation and pitch I have been trying to install vLLM on MacOS M3 but installation fails most of the time. I have used both pip and uv approaches to install dependencies. Apart from issues...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add support for Apple MPS(Metal Performance Shaders) feature request ### 🚀 The feature, motivation and pitch I have been trying to install vLLM on MacOS M3 but installation fails most of the time. I have used...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
