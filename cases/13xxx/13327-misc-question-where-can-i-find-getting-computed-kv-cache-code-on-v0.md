# vllm-project/vllm#13327: [Misc]: Question: Where can I find getting computed kv cache code on v0.

| 字段 | 值 |
| --- | --- |
| Issue | [#13327](https://github.com/vllm-project/vllm/issues/13327) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Question: Where can I find getting computed kv cache code on v0.

### Issue 正文摘录

Hi, I'm trying understanding the work flow of vLLM and I'm intersting in Prefix Caching. So, I want to know the conditions of prefix caching and who (Scheduler, Executor, Worker, Runner etc. ) get kv cache. In v1 code, I found it. https://github.com/vllm-project/vllm/blob/067fa2255b6687ccaa79391dc9d1a08c7632f605/vllm/v1/core/scheduler.py#L215-L217 But, v0, I failed to find it. Does any one help me? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: Question: Where can I find getting computed kv cache code on v0. stale Hi, I'm trying understanding the work flow of vLLM and I'm intersting in Prefix Caching. So, I want to know the conditions of prefix caching...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Misc]: Question: Where can I find getting computed kv cache code on v0. stale Hi, I'm trying understanding the work flow of vLLM and I'm intersting in Prefix Caching. So, I want to know the conditions of prefix caching...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
