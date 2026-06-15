# vllm-project/vllm#24292: [Usage]: Adjusting reasoning efforts for GPT-OSS in direct sampling

| 字段 | 值 |
| --- | --- |
| Issue | [#24292](https://github.com/vllm-project/vllm/issues/24292) |
| 状态 | closed |
| 标签 | usage;stale;gpt-oss |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Adjusting reasoning efforts for GPT-OSS in direct sampling

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi team, I understand that currently we could adjust the "reasoning_effort" for GPT-OSS if we serve the model via VLLM using "Chat Completions-compatible API" approach. However, it seems there is no appropriate parameter for this if we want to initialise the model using "LLM" and do direct sampling (via llm.generate). May I know are we planning to integrate this into SamplingParams or we have already done so? Thanks for your kind answer in advance. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Adjusting reasoning efforts for GPT-OSS in direct sampling usage;stale;gpt-oss ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi team, I unders...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Usage]: Adjusting reasoning efforts for GPT-OSS in direct sampling usage;stale;gpt-oss ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi team, I underst...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
