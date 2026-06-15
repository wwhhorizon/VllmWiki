# vllm-project/vllm#41974: "[Bugfix] release KV blocks for skipped P-ranks ..." accidentally reverted during rebase

| 字段 | 值 |
| --- | --- |
| Issue | [#41974](https://github.com/vllm-project/vllm/issues/41974) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> "[Bugfix] release KV blocks for skipped P-ranks ..." accidentally reverted during rebase

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Reverted PR: https://github.com/vllm-project/vllm/pull/40449 Will fix soon. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: "[Bugfix] release KV blocks for skipped P-ranks ..." accidentally reverted during rebase bug ### Your current environment ### 🐛 Describe the bug Reverted PR: https://github.com/vllm-project/vllm/pull/40449 Will fix soon...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "[Bugfix] release KV blocks for skipped P-ranks ..." accidentally reverted during rebase bug ### Your current environment ### 🐛 Describe the bug Reverted PR: https://github.com/vllm-project/vllm/pull/40449 Will fix soon...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
