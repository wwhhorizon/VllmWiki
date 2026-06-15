# vllm-project/vllm#15142: missing latest tag in vllm-cpu image

| 字段 | 值 |
| --- | --- |
| Issue | [#15142](https://github.com/vllm-project/vllm/issues/15142) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> missing latest tag in vllm-cpu image

### Issue 正文摘录

### Your current environment current CI/CD builds a new vllm-cpu image on new releases which is great. but ‘latest’ tag is missing which requires having to keep changing the image manually on every release. we expect the CI/CD not only to create a versioned tag, but also to tag latest once a new release is out. ### How would you like to use vllm I want to run inference ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: missing latest tag in vllm-cpu image installation ### Your current environment current CI/CD builds a new vllm-cpu image on new releases which is great. but ‘latest’ tag is missing which requires having to keep changing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nce ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: missing latest tag in vllm-cpu image installation ### Your current environment current CI/CD builds a new vllm-cpu image on new releases which is great. but ‘latest’ tag is missing which requires having to keep changing...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
