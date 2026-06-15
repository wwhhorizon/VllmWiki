# vllm-project/vllm#13442: [Usage]: Given sufficient GPU memory, which is better: starting a single vLLM instance or starting multiple instances for load balancing?

| 字段 | 值 |
| --- | --- |
| Issue | [#13442](https://github.com/vllm-project/vllm/issues/13442) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Given sufficient GPU memory, which is better: starting a single vLLM instance or starting multiple instances for load balancing?

### Issue 正文摘录

### Your current environment ```txt A100-80G×8 ``` ### How would you like to use vllm Given sufficient GPU memory, which is better: starting a single vLLM instance or starting multiple instances for load balancing? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: instances for load balancing? usage ### Your current environment ```txt A100-80G×8 ``` ### How would you like to use vllm Given sufficient GPU memory, which is better: starting a single vLLM instance or starting multipl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: Given sufficient GPU memory, which is better: starting a single vLLM instance or starting multiple instances for load balancing? usage ### Your current environment ```txt A100-80G×8 ``` ### How would you like t...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: Given sufficient GPU memory, which is better: starting a single vLLM instance or starting multiple instances for load balancing? usage ### Your current environment ```txt A100-80G×8 ``` ### How would you like t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
