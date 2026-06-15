# vllm-project/vllm#11500: [Performance]: The speedup for Pipeline Parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#11500](https://github.com/vllm-project/vllm/issues/11500) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: The speedup for Pipeline Parallel

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression When I run llama-3.1-8B-Instruct with -pp 8 or not, there is nearly no speedup, even with large batch of data. I also watched the utilization of GPU. When running with pipeline parallel 8, the gpu utilization of the 8 cards are from 20% to 50%. Is this situation normal? The testing data is shown below: Model | Total Prompt Tokens | Total Decode Tokens | Total Runtime (s) | Decode Speed (Tokens / s) llama-3.1-8B-instruct-pp_1 |113,632 | 17,004 | 30.11 | 564.79 llama-3.1-8B-instruct-pp_8 |114,532 |17,517 | 29.89 | 586.03 ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ormance _No response_ ### Report of performance regression When I run llama-3.1-8B-Instruct with -pp 8 or not, there is nearly no speedup, even with large batch of data. I also watched the utilization of GPU. When runni...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression When I run llama-3.1-8B-Instruct with -pp 8 or not, there is nearly no speedup, even with large batch of data. I also watched the utiliza...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ? The testing data is shown below: Model | Total Prompt Tokens | Total Decode Tokens | Total Runtime (s) | Decode Speed (Tokens / s) llama-3.1-8B-instruct-pp_1 |113,632 | 17,004 | 30.11 | 564.79 llama-3.1-8B-instruct-pp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
