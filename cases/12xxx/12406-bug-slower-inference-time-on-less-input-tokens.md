# vllm-project/vllm#12406: [Bug]: Slower inference time on less input tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#12406](https://github.com/vllm-project/vllm/issues/12406) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Slower inference time on less input tokens

### Issue 正文摘录

### Your current environment Currently, we are getting the inference time of 1.45 seconds for 1068 tokens and 1.53 seconds for 3554 tokens. Any suggestions for improvement to get the inference time within a second? [00:01<00:00, 1.54s/it, est. speed input: 671.29 toks/s, output: 149.17 toks/s] for 1068 tokens [00:01<00:00, 1.59s/it, est. speed input: 2045.29 toks/s, output: 148.63 toks/s] for 3554 tokens ### Model Input Dumps Below is the inference time. ### 🐛 Describe the bug Slow inference time ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ime ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: speed input: 2045.29 toks/s, output: 148.63 toks/s] for 3554 tokens ### Model Input Dumps Below is the inference time. ### 🐛 Describe the bug Slow inference time ### Before submitting a new issue... - [x] Make sure you...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Slower inference time on less input tokens bug;stale ### Your current environment Currently, we are getting the inference time of 1.45 seconds for 1068 tokens and 1.53 seconds for 3554 tokens. Any suggestions for...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
