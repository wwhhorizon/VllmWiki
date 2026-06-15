# vllm-project/vllm#20181: [Feature]: Batch inference for Multi-Modal Online Serving

| 字段 | 值 |
| --- | --- |
| Issue | [#20181](https://github.com/vllm-project/vllm/issues/20181) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Batch inference for Multi-Modal Online Serving

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It would be great if we could have support for batch inference for online serving. It seems only supported for offline inference. Also, it seems that the OpenAI interface supports only a single request at a time (Not batched). This feature is not about the OpenAI interface specifically; instead, it requests a generic way, which could be using OpenAI or any other method. ### Alternatives The straightforward alternative to submit multiple parallel requests is threading, but it is not efficient, as the model on the server will handle each request separately, so it is not batched inference. ### Additional context These issues (#11859, #9575) are related, but they don't propose any reliable solution, and they were closed for being stale. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Batch inference for Multi-Modal Online Serving feature request;stale ### 🚀 The feature, motivation and pitch It would be great if we could have support for batch inference for online serving. It seems only su...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: a time (Not batched). This feature is not about the OpenAI interface specifically; instead, it requests a generic way, which could be using OpenAI or any other method. ### Alternatives The straightforward alternative to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: le. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: multiple parallel requests is threading, but it is not efficient, as the model on the server will handle each request separately, so it is not batched inference. ### Additional context These issues (#11859, #9575) are r...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
