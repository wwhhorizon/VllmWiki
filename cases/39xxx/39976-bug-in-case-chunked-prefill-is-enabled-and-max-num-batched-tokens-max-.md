# vllm-project/vllm#39976: [Bug]: In case chunked prefill is enabled and max-num-batched-tokens > max-model-length the server does not start up and fails

| 字段 | 值 |
| --- | --- |
| Issue | [#39976](https://github.com/vllm-project/vllm/issues/39976) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: In case chunked prefill is enabled and max-num-batched-tokens > max-model-length the server does not start up and fails

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This is the official definition that I got. Therefore, my understanding is max-num-batched tokens could be more than max-model-length (number of tokens in a request. Because batched tokens could include tokens from both prefill and decode phase and also across requests but whenever max-num-batched tokens > max-model-length, the server did not start up ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: In case chunked prefill is enabled and max-num-batched-tokens > max-model-length the server does not start up and fails bug ### Your current environment ### 🐛 Describe the bug This is the official definition that...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: current environment ### 🐛 Describe the bug This is the official definition that I got. Therefore, my understanding is max-num-batched tokens could be more than max-model-length (number of tokens in a request. Because ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: up ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ug]: In case chunked prefill is enabled and max-num-batched-tokens > max-model-length the server does not start up and fails bug ### Your current environment ### 🐛 Describe the bug This is the official definition that I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
