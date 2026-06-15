# vllm-project/vllm#31678: [Performance]: embedding

| 字段 | 值 |
| --- | --- |
| Issue | [#31678](https://github.com/vllm-project/vllm/issues/31678) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: embedding

### Issue 正文摘录

### Proposal to improve performance Hi using vllm 0.13.0 with jina embeddings v3. why i use 1x vllm get around 600/s embeddings but 4x vllm on one gpu get around 2800? is it problem of tokenizer on one process? it seems skip tokenizer and prompt_token_ids dont work for embedding. what about adding it to embedding and also optional multiprocesspool on tokenization? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: so optional multiprocesspool on tokenization? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: embedding performance;stale ### Proposal to improve performance Hi using vllm 0.13.0 with jina embeddings v3. why i use 1x vllm get around 600/s embeddings but 4x vllm on one gpu get around 2800? is it pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
