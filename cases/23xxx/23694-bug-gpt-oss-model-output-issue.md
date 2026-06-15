# vllm-project/vllm#23694: [Bug]: gpt-oss model output issue

| 字段 | 值 |
| --- | --- |
| Issue | [#23694](https://github.com/vllm-project/vllm/issues/23694) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: gpt-oss model output issue

### Issue 正文摘录

### Your current environment vLLM 1.0.1 python 3.12 ### 🐛 Describe the bug I fine-tuned the model without using any reasoning data. When generating, the model produces output like: ` final {"issues":[]} ` However, the `parse_chat_output` function doesn’t check the channel. It mistakenly interprets the content as belonging to the `reasoning` field. As a result, the final output ends up empty, while the reasoning field incorrectly contains the actual data. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: gpt-oss model output issue bug;stale;gpt-oss ### Your current environment vLLM 1.0.1 python 3.12 ### 🐛 Describe the bug I fine-tuned the model without using any reasoning data. When generating, the model produces...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ta. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: gpt-oss model output issue bug;stale;gpt-oss ### Your current environment vLLM 1.0.1 python 3.12 ### 🐛 Describe the bug I fine-tuned the model without using any reasoning data. When generating, the model produces...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
