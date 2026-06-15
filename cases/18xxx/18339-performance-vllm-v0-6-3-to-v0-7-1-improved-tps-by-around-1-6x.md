# vllm-project/vllm#18339: [Performance]: vLLM v0.6.3 to v0.7.1, improved tps by around 1.6x

| 字段 | 值 |
| --- | --- |
| Issue | [#18339](https://github.com/vllm-project/vllm/issues/18339) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: vLLM v0.6.3 to v0.7.1, improved tps by around 1.6x

### Issue 正文摘录

### Proposal to improve performance Hi, I recently upgraded from vLLM v0.6.3 to v0.7.1, and I noticed that my RPS (requests per second) improved by around 1.6x — even though I’m still using the v0 engine, not v1. I saw in the [v0.7.1 release notes](https://github.com/vllm-project/vllm/releases/tag/v0.7.1) that it mentions “~3x the generation throughput, ~10x the memory capacity for tokens, and horizontal context scalability with pipeline parallelism.” Could you help me understand what specific optimizations or changes in v0.7.1 might have contributed to this performance gain, even without switching to the v1 engine? Thanks in advance! ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: m-project/vllm/releases/tag/v0.7.1) that it mentions “~3x the generation throughput, ~10x the memory capacity for tokens, and horizontal context scalability with pipeline parallelism.” Could you help me understand what...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ty for tokens, and horizontal context scalability with pipeline parallelism.” Could you help me understand what specific optimizations or changes in v0.7.1 might have contributed to this performance gain, even without s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ormance]: vLLM v0.6.3 to v0.7.1, improved tps by around 1.6x performance;stale ### Proposal to improve performance Hi, I recently upgraded from vLLM v0.6.3 to v0.7.1, and I noticed that my RPS (requests per second) impr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: .1) that it mentions “~3x the generation throughput, ~10x the memory capacity for tokens, and horizontal context scalability with pipeline parallelism.” Could you help me understand what specific optimizations or change...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
