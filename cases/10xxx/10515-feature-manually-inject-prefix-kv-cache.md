# vllm-project/vllm#10515: [Feature]: Manually inject Prefix KV Cache

| 字段 | 值 |
| --- | --- |
| Issue | [#10515](https://github.com/vllm-project/vllm/issues/10515) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Manually inject Prefix KV Cache

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We're having a good KV-cache compressor base on the paper: https://arxiv.org/abs/2401.03462 Example we can compress the KV-cache of 2048 tokens into the KV-cache of 512 special tokens, so we need a manual way to feed it into the generate function. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Feature]: Manually inject Prefix KV Cache feature request;stale ### 🚀 The feature, motivation and pitch We're having a good KV-cache compressor base on the paper: https://arxiv.org/abs/2401.03462 Example we can compres...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Manually inject Prefix KV Cache feature request;stale ### 🚀 The feature, motivation and pitch We're having a good KV-cache compressor base on the paper: https://arxiv.org/abs/2401.03462 Example we can compres...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: we can compress the KV-cache of 2048 tokens into the KV-cache of 512 special tokens, so we need a manual way to feed it into the generate function. ### Alternatives _No response_ ### Additional context _No response_ ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
