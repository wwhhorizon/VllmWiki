# vllm-project/vllm#14004: [Usage]: Do vllm support the prefix caching in multi node?

| 字段 | 值 |
| --- | --- |
| Issue | [#14004](https://github.com/vllm-project/vllm/issues/14004) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Do vllm support the prefix caching in multi node?

### Issue 正文摘录

### Your current environment ```text the latest version ``` ### How would you like to use vllm For example, when encountering the situation that multil node to infer DeepSeek-R1-671B, how to share the kv cache between the nodes? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ng in multi node? usage ### Your current environment ```text the latest version ``` ### How would you like to use vllm For example, when encountering the situation that multil node to infer DeepSeek-R1-671B, how to shar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: e situation that multil node to infer DeepSeek-R1-671B, how to share the kv cache between the nodes? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot l...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: caching in multi node? usage ### Your current environment ```text the latest version ``` ### How would you like to use vllm For example, when encountering the situation that multil node to infer DeepSeek-R1-671B, how to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
