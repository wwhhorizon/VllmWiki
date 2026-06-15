# vllm-project/vllm#28976: [Bug]: kimi-k2-thinking running 500 error

| 字段 | 值 |
| --- | --- |
| Issue | [#28976](https://github.com/vllm-project/vllm/issues/28976) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: kimi-k2-thinking running 500 error

### Issue 正文摘录

### Your current environment vllm docker nightly vllm=0.11.1rc7.dev109+gca00b1bfc.cu129 ### 🐛 Describe the bug When I deployed k2-thinking on multiple machines using vllm and ray, the evaluation showed after running for a period of time: attribute error _torchtensoracclerator channel object has no attribute "_accelerator_group" did you mean:"_accelerator_group_id"? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: When I deployed k2-thinking on multiple machines using vllm and ray, the evaluation showed after running for a period of time: attribute error _torchtensoracclerator channel object has no attribute "_accelerator_group"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: hinking running 500 error bug;unstale ### Your current environment vllm docker nightly vllm=0.11.1rc7.dev109+gca00b1bfc.cu129 ### 🐛 Describe the bug When I deployed k2-thinking on multiple machines using vllm and ray, t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d"? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: kimi-k2-thinking running 500 error bug;unstale ### Your current environment vllm docker nightly vllm=0.11.1rc7.dev109+gca00b1bfc.cu129 ### 🐛 Describe the bug When I deployed k2-thinking on multiple machines using...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
