# vllm-project/vllm#8639: [Performance]:  The accept rate of typical acceptance sampling

| 字段 | 值 |
| --- | --- |
| Issue | [#8639](https://github.com/vllm-project/vllm/issues/8639) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]:  The accept rate of typical acceptance sampling

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression I tested the `accept length` ( number of tokens per step) with`typical acceptance sampling`. The accept length is even smaller than default reject sampling method. Here is my experimental details: 1. The dataset I used was mt_bench. 2. Speculative decoding model's setup: llama3.1 8b as target model and Qwama-0.5B-Instruct as a draft model (num of speculative tokens is 2) llama3.1 8b as target model with MLP-speculator. 3 Temperature was set as 0.9 4 `posterior_threshold` and `posterior_alpha` were set as default values. Do you have some experimental results on this? Or do I need to tune some parameters for `typical acceptance sampling`? Thanks a lot! ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s per step) with`typical acceptance sampling`. The accept length is even smaller than default reject sampling method. Here is my experimental details: 1. The dataset I used was mt_bench. 2. Speculative decoding model's...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: al details: 1. The dataset I used was mt_bench. 2. Speculative decoding model's setup: llama3.1 8b as target model and Qwama-0.5B-Instruct as a draft model (num of speculative tokens is 2) llama3.1 8b as target model wi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Here is my experimental details: 1. The dataset I used was mt_bench. 2. Speculative decoding model's setup: llama3.1 8b as target model and Qwama-0.5B-Instruct as a draft model (num of speculative tokens is 2) llama3.1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression I tested the `accept length` ( number of tokens per step) with`typical acceptance sampling`. The accept length is even smaller than defau...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
