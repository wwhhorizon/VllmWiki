# vllm-project/vllm#25096: [Feature]: Prefix Caching support when Prompt Embeds is enabled.

| 字段 | 值 |
| --- | --- |
| Issue | [#25096](https://github.com/vllm-project/vllm/issues/25096) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Prefix Caching support when Prompt Embeds is enabled.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Prompt Embeds + prefix caching is broken in both v0 and v1 (#24278). #24278 explicitly disables prefix caching whenever prompt embeds is enabled, in fact. Fixing this in the v0 engine is not worth any effort, since v0 is actively being removed. After #24278 lands, it should be straightforward to enable it in v1 by adding some canonical representation of prompt embeds tensors to the input of the hash function for each block. I plan on doing this follow-up work, but I didn't want to complicate #24278, so I'm creating this issue to track it. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: mbeds + prefix caching is broken in both v0 and v1 (#24278). #24278 explicitly disables prefix caching whenever prompt embeds is enabled, in fact. Fixing this in the v0 engine is not worth any effort, since v0 is active...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tion of prompt embeds tensors to the input of the hash function for each block. I plan on doing this follow-up work, but I didn't want to complicate #24278, so I'm creating this issue to track it. ### Alternatives _No r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Prefix Caching support when Prompt Embeds is enabled. feature request ### 🚀 The feature, motivation and pitch Prompt Embeds + prefix caching is broken in both v0 and v1 (#24278). #24278 explicitly disables pr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
