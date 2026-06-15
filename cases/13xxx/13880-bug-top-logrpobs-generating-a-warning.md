# vllm-project/vllm#13880: [Bug]: top_logrpobs generating a WARNING

| 字段 | 值 |
| --- | --- |
| Issue | [#13880](https://github.com/vllm-project/vllm/issues/13880) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: top_logrpobs generating a WARNING

### Issue 正文摘录

### Your current environment Using vllm v0.7.3 ### 🐛 Describe the bug When making a request via the OpenAI API using the top_logprobs atgument, the logging of the request shows a warning that says: ``` The following fields were present in the request but ignore: {'top_logprobs'} ``` This behaviour should be reserved to the args in the request that are not expected by the ```ChatCompletionRequest()``` class, but ```top_logprobs``` is actually part of its args. This warning is raised by the function ```__log_extra_fields__()``` in ```vllm/entrypoints/openai/protocol.py```. The warning started to appear in version v0.7.1 and I think was introduced in the PR #12420 (I would like to tag @maxdebayser for more some help :)) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vllm/entrypoints/openai/protocol.py```. The warning started to appear in version v0.7.1 and I think was introduced in the PR #12420 (I would like to tag @maxdebayser for more some help :)) ### Before submitting a new is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: :)) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nt environment Using vllm v0.7.3 ### 🐛 Describe the bug When making a request via the OpenAI API using the top_logprobs atgument, the logging of the request shows a warning that says: ``` The following fields were prese...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
