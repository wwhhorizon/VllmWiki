# vllm-project/vllm#25068: [Bug]: Docker latest tag is not being updated

| 字段 | 值 |
| --- | --- |
| Issue | [#25068](https://github.com/vllm-project/vllm/issues/25068) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Docker latest tag is not being updated

### Issue 正文摘录

### Your current environment Docker ### 🐛 Describe the bug With the introduction of the CPU arch based Docker images, the `latest` tag is not being updated. See here: https://hub.docker.com/r/vllm/vllm-openai/tags?name=latest ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Docker latest tag is not being updated bug ### Your current environment Docker ### 🐛 Describe the bug With the introduction of the CPU arch based Docker images, the `latest` tag is not being updated. See here: ht...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: onment Docker ### 🐛 Describe the bug With the introduction of the CPU arch based Docker images, the `latest` tag is not being updated. See here: https://hub.docker.com/r/vllm/vllm-openai/tags?name=latest ### Before subm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: Docker latest tag is not being updated bug ### Your current environment Docker ### 🐛 Describe the bug With the introduction of the CPU arch based Docker images, the `latest` tag is not being updated. See here: ht...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
