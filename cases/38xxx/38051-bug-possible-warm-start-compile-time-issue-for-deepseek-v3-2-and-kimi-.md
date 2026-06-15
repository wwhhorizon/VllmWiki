# vllm-project/vllm#38051: [Bug]: Possible warm start compile time issue for Deepseek V3.2 and Kimi K2.5

| 字段 | 值 |
| --- | --- |
| Issue | [#38051](https://github.com/vllm-project/vllm/issues/38051) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Possible warm start compile time issue for Deepseek V3.2 and Kimi K2.5

### Issue 正文摘录

### Your current environment main ### 🐛 Describe the bug see https://github.com/vllm-project/vllm/pull/38046 I'm not sure if the issue is that the test is wrong or if it actually manifests in real life. Need to go benchmarking later ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: b.com/vllm-project/vllm/pull/38046 I'm not sure if the issue is that the test is wrong or if it actually manifests in real life. Need to go benchmarking later ### Before submitting a new issue... - [x] Make sure you alr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Possible warm start compile time issue for Deepseek V3.2 and Kimi K2.5 bug;torch.compile ### Your current environment main ### 🐛 Describe the bug see https://github.com/vllm-project/vllm/pull/38046 I'm not sure i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ter ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
