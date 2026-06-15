# vllm-project/vllm#13875: [Usage]: `max_num_batched_tokens` and `max_model_len`

| 字段 | 值 |
| --- | --- |
| Issue | [#13875](https://github.com/vllm-project/vllm/issues/13875) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: `max_num_batched_tokens` and `max_model_len`

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm when i use vllm to run deepseek r1, i find there are two parameters which named `max_num_batched_tokens` and `max_model_len`. my questions are: 1. what's the relationship between `max_num_batched_tokens` and `max_model_len`. 2. `max_model_len` is related to the context length, limiting the total number of tokens for both input and output? Does `max_num_batched_tokens` only restrict the input tokens? Does `max_num_batched_tokens` also restrict the output tokens? 3. when i run deepseek_r1 with `max_model_len` = 64k, i find that the serving model only support input with 2k tokens. from the source code of vllm, i find that `max_num_batched_tokens` is forcibly set as 2k. what is the purpose of doing this? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _tokens` and `max_model_len`. my questions are: 1. what's the relationship between `max_num_batched_tokens` and `max_model_len`. 2. `max_model_len` is related to the context length, limiting the total number of tokens f...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rom the source code of vllm, i find that `max_num_batched_tokens` is forcibly set as 2k. what is the purpose of doing this? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: `max_num_batched_tokens` and `max_model_len` usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm when i use vllm to run deepseek r1, i f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: `max_num_batched_tokens` and `max_model_len` usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm when i use vllm to run deepseek r1, i f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
