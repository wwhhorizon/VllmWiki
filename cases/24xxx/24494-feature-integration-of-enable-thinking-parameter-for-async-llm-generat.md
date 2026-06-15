# vllm-project/vllm#24494: [Feature]: Integration of enable_thinking parameter for Async LLM Generation for dynamic generaiton

| 字段 | 值 |
| --- | --- |
| Issue | [#24494](https://github.com/vllm-project/vllm/issues/24494) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integration of enable_thinking parameter for Async LLM Generation for dynamic generaiton

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi guys, I found the possible use of the extra_body arg "enable_thinking" into V1 with the llm.chat() method. However this feature doesn't seems do be supported for the generate() method of the async generation API (according to the bot). For now it needs to be passed through tokenizer parameter at engine initialization. It could be a great improvement to support dynamic thinking based on request parameter instead of initial initialization. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: inking parameter for Async LLM Generation for dynamic generaiton feature request;stale ### 🚀 The feature, motivation and pitch Hi guys, I found the possible use of the extra_body arg "enable_thinking" into V1 with the l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
