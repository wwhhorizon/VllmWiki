# vllm-project/vllm#11042: [Performance]: How to properly measure performance between vLLM and SGLang?

| 字段 | 值 |
| --- | --- |
| Issue | [#11042](https://github.com/vllm-project/vllm/issues/11042) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: How to properly measure performance between vLLM and SGLang?

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Since vLLM does not handle batches like other frameworks, what is the recommended way to reach an apples/apples comparison at a specific batch size for TRT-LLM and SGLang? I believe that this needs to be clarified or people will compare apples/oranges between the frameworks and arrive at erroneous metrics. ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Since vLLM does not handle batches like other frameworks, what is the recommended way to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: what is the recommended way to reach an apples/apples comparison at a specific batch size for TRT-LLM and SGLang? I believe that this needs to be clarified or people will compare apples/oranges between the frameworks an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: How to properly measure performance between vLLM and SGLang? performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Sinc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
