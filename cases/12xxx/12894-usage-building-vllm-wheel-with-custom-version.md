# vllm-project/vllm#12894: [Usage]: Building vLLM wheel with custom version.

| 字段 | 值 |
| --- | --- |
| Issue | [#12894](https://github.com/vllm-project/vllm/issues/12894) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Building vLLM wheel with custom version.

### Issue 正文摘录

### Your current environment Hi Team, I'm trying to build vLLM wheel in my local GPU device and I want to specify custom version instead of default 0.1.devxxxxx. I have made some changes on top of 0.6.3.post1 version and want the final wheel created should have 0.6.3.post1 in the version instead of 0.1.devxxx Suggestion would be helpful ### How would you like to use vllm Build wheel file. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Usage]: Building vLLM wheel with custom version. usage ### Your current environment Hi Team, I'm trying to build vLLM wheel in my local GPU device and I want to specify custom version instead of default 0.1.devxxxxx. I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: le. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
