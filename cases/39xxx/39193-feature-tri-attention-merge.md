# vllm-project/vllm#39193: [Feature]: Tri-attention merge?

| 字段 | 值 |
| --- | --- |
| Issue | [#39193](https://github.com/vllm-project/vllm/issues/39193) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Tri-attention merge?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Superheroes just open sourced a new kv-cache compression method, called Triattention! It seems really promising and they say it's vLLM compatible already. Can/will this be merged to be installed by default with vLLM? The github repo is Apache 2.0, thank you so much @WeianMao https://github.com/WeianMao/triattention ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and they say it's vLLM compatible already. Can/will this be merged to be installed by default with vLLM? The github repo is Apache 2.0, thank you so much @WeianMao https://github.com/WeianMao/triattention ### Alternativ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 🚀 The feature, motivation and pitch Superheroes just open sourced a new kv-cache compression method, called Triattention! It seems really promising and they say it's vLLM compatible already. Can/will this be merged to b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Tri-attention merge? feature request ### 🚀 The feature, motivation and pitch Superheroes just open sourced a new kv-cache compression method, called Triattention! It seems really promising and they say it's v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
