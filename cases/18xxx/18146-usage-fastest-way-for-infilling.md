# vllm-project/vllm#18146: [Usage]: Fastest Way For Infilling?

| 字段 | 值 |
| --- | --- |
| Issue | [#18146](https://github.com/vllm-project/vllm/issues/18146) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Fastest Way For Infilling?

### Issue 正文摘录

### Your current environment N/A ### How would you like to use vllm Greetings, I am wondering how do I do infilling with VLLM. Is this supported? For example, I have this `sentence_1, [token], sentence_2, [token]` I want to predict these to tokens. My current implementation is doing such things iteratively, like ``` 1. prompt = sentence_1, predicted_token_1 = llm.generate(prompt) 2. prompt += predicted_token_1 + sentence_2 3. token_2 = llm.generate(prompt) ``` This is slow as I have to reload the sentence 1 into the generation. Does anyone have any suggestions? Thanks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Fastest Way For Infilling? usage;stale ### Your current environment N/A ### How would you like to use vllm Greetings, I am wondering how do I do infilling with VLLM. Is this supported? For example, I have this...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Usage]: Fastest Way For Infilling? usage;stale ### Your current environment N/A ### How would you like to use vllm Greetings, I am wondering how do I do infilling with VLLM. Is this supported? For example, I have this...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
