# vllm-project/vllm#26537: [Bug]: V1 attention tests are broken

| 字段 | 值 |
| --- | --- |
| Issue | [#26537](https://github.com/vllm-project/vllm/issues/26537) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: V1 attention tests are broken

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Many of the tests in `tests/v1/attention` are broken due to changes in the attention backends and their interfaces. Furthermore, they are not run in CI at all (which is why these issues haven't been caught). These need to be fixed and added to CI. cc @LucasWilkinson ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tests in `tests/v1/attention` are broken due to changes in the attention backends and their interfaces. Furthermore, they are not run in CI at all (which is why these issues haven't been caught). These need to be fixed...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ttention backends and their interfaces. Furthermore, they are not run in CI at all (which is why these issues haven't been caught). These need to be fixed and added to CI. cc @LucasWilkinson ### Before submitting a new...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: V1 attention tests are broken bug;good first issue ### Your current environment ### 🐛 Describe the bug Many of the tests in `tests/v1/attention` are broken due to changes in the attention backends and their inter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
