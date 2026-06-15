# vllm-project/vllm#8033: [Misc]:  Question about Serving with Server API

| 字段 | 值 |
| --- | --- |
| Issue | [#8033](https://github.com/vllm-project/vllm/issues/8033) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]:  Question about Serving with Server API

### Issue 正文摘录

### API Server I have been digging around VLLM. and I have observed that the API server actually holds a client to an RPC server. I guess this is needed because of the multi model potential nature. But if I were to serve a single model instance, would it be recommended to use directly an `AsyncLLMEngine` behind my FastAPI app or any web server? Thanks for the clarification. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: a client to an RPC server. I guess this is needed because of the multi model potential nature. But if I were to serve a single model instance, would it be recommended to use directly an `AsyncLLMEngine` behind my FastAP...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
