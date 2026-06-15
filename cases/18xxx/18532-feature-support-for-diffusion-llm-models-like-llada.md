# vllm-project/vllm#18532: [Feature]: Support for diffusion LLM models like LLADA

| 字段 | 值 |
| --- | --- |
| Issue | [#18532](https://github.com/vllm-project/vllm/issues/18532) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for diffusion LLM models like LLADA

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, I was wondering if support for diffusion models is possible with VLLM. With the launch of [gemini diffusion models](https://deepmind.google/models/gemini-diffusion/), I think the future would involve llm diffusion models especially for fast inference use cases. With that in mind i wonder if models like [LLADA](https://github.com/ML-GSAI/LLaDA) are supported. I would like to know if there is a plan and what would involve in integrating such models. I would like to contribute in any way to make this possible. Thanks for a great project. Thanks Arun ### Alternatives LLADA works with transformers, but havent tried if it is supported out of the box with VLLM. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: i-diffusion/), I think the future would involve llm diffusion models especially for fast inference use cases. With that in mind i wonder if models like [LLADA](https://github.com/ML-GSAI/LLaDA) are supported. I would li...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support for diffusion LLM models like LLADA feature request ### 🚀 The feature, motivation and pitch Hi, I was wondering if support for diffusion models is possible with VLLM. With the launch of [gemini diffus...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support for diffusion LLM models like LLADA feature request ### 🚀 The feature, motivation and pitch Hi, I was wondering if support for diffusion models is possible with VLLM. With the launch of [gemini diffus...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
