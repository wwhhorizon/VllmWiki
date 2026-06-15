# vllm-project/vllm#40556: [Feature]: Support responses api in tokenize endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#40556](https://github.com/vllm-project/vllm/issues/40556) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support responses api in tokenize endpoint

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, I see here that the `/tokenize` api supports chat completions input: https://discuss.vllm.ai/t/tell-me-about-the-current-status-of-the-tokenize-endpoint-in-vllm/2089 . I would like to request that this endpoint also supports the responses api input as it would be great if for any supported input format you could pass the request to tokenize to determine the input tokens the model will receive. Thank you. Also side note, but the docs here do not make it clear that the `/tokenize` endpoint even works with chat completions here: https://docs.vllm.ai/en/latest/serving/openai_compatible_server/#tokenizer-api ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: the responses api input as it would be great if for any supported input format you could pass the request to tokenize to determine the input tokens the model will receive. Thank you. Also side note, but the docs here do...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support responses api in tokenize endpoint feature request ### 🚀 The feature, motivation and pitch Hi, I see here that the `/tokenize` api supports chat completions input: https://discuss.vllm.ai/t/tell-me-ab...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ndpoint even works with chat completions here: https://docs.vllm.ai/en/latest/serving/openai_compatible_server/#tokenizer-api ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
