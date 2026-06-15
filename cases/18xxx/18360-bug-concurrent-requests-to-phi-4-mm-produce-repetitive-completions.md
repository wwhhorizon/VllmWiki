# vllm-project/vllm#18360: [Bug]: Concurrent requests to Phi-4-MM produce repetitive completions

| 字段 | 值 |
| --- | --- |
| Issue | [#18360](https://github.com/vllm-project/vllm/issues/18360) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Concurrent requests to Phi-4-MM produce repetitive completions

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi 👋🏼 When sending concurrent requests to Phi-4-multimodal-instruct with image inputs, I’ve noticed that the responses tend to degrade partway through. While the initial sentences are generally well-structured, the remainder often includes repeated words or excessive punctuation. This behavior seems to emerge specifically under parallel load, and doesn't occur when requests are made sequentially. Example output: `This image presents two key insights about student learning habits. The first section shows how much time students spend on homework each week, divided into four ranges. Most students report spending between 6 and 10 hours weekly - -----2-------2-1-2---------1----1-------------o---2-2-1-1-1---1-i-1-t--2-1-2-100-100-1-1-a-100-100-1-a-2-a-100-100-l--100-100--1-100-100-2-2-a-2-2-2--2-100-100- and---100--- and-b----1-2-b-1-100-1-b-b- and- and-b-- and- and-2-2-b-2-b--a-a-b-l-a-2-a-2-b-a-2-2-2-2-1-b-b-b-a-b-b---b-a-b-2-2-b-b-b-b-b-2-2-2-b-2-1-1-2-a-1-1- and-1-1-2-a-a-a-1-a-1-a-1-b-*-----2-b-b-a-a-b-2-1-2-b-2-2-2-a-1-1-1-i-b-e-a-b-a-b-b-a-a-b-a-1-b-b-1-a- and-ea-2-a-b-b-a-a-a-b-a-*-a-a-a-a-a-2-a-2-a-b-1-e-2-` vLLM image: v0.8.5...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ### 🐛 Describe the bug Hi 👋🏼 When sending concurrent requests to Phi-4-multimodal-instruct with image inputs, I’ve noticed that the responses tend to degrade partway through. While the initial sentences are generally we...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: epeated words or excessive punctuation. This behavior seems to emerge specifically under parallel load, and doesn't occur when requests are made sequentially. Example output: `This image presents two key insights about...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Concurrent requests to Phi-4-MM produce repetitive completions bug ### Your current environment ### 🐛 Describe the bug Hi 👋🏼 When sending concurrent requests to Phi-4-multimodal-instruct with image inputs, I’ve n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: u 🤗 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
