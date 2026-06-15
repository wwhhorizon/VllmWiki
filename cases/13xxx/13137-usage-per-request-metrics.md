# vllm-project/vllm#13137: [Usage]: Per request metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#13137](https://github.com/vllm-project/vllm/issues/13137) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Per request metrics

### Issue 正文摘录

### Your current environment I'm looking to access the incoming request, outgoing response, and total number of tokens. I've looked through the docs extensively and I couldn't find anything on this. I tried adding my own FastAPI middleware for this, but also hit a dead end. Is there any way to access this data so I can store it? I'm looking to access this data server side, along with incoming request and output ` usage: { prompt_tokens: 507, total_tokens: 929, completion_tokens: 422 }` ### How would you like to use vllm I'm hosting a model with the OpenAI compatible API. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: I. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: letion_tokens: 422 }` ### How would you like to use vllm I'm hosting a model with the OpenAI compatible API. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Per request metrics usage ### Your current environment I'm looking to access the incoming request, outgoing response, and total number of tokens. I've looked through the docs extensively and I couldn't find any...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
