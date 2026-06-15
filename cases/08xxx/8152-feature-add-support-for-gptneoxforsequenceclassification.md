# vllm-project/vllm#8152: [Feature]: Add support for `GPTNeoXForSequenceClassification`

| 字段 | 值 |
| --- | --- |
| Issue | [#8152](https://github.com/vllm-project/vllm/issues/8152) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add support for `GPTNeoXForSequenceClassification`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently vLLM does not support `GPTNeoXForSequenceClassification` architecture. Many reward models that are used in RLHF training have similar architecture (causalLM + linear projection on top). Supporting this architecture can make training and evaluation of RLHF methods way faster. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: not support `GPTNeoXForSequenceClassification` architecture. Many reward models that are used in RLHF training have similar architecture (causalLM + linear projection on top). Supporting this architecture can make train...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add support for `GPTNeoXForSequenceClassification` feature request;stale ### 🚀 The feature, motivation and pitch Currently vLLM does not support `GPTNeoXForSequenceClassification` architecture. Many reward mo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: r projection on top). Supporting this architecture can make training and evaluation of RLHF methods way faster. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: itch Currently vLLM does not support `GPTNeoXForSequenceClassification` architecture. Many reward models that are used in RLHF training have similar architecture (causalLM + linear projection on top). Supporting this ar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
