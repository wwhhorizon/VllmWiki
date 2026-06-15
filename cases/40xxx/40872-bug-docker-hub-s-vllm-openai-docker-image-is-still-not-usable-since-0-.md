# vllm-project/vllm#40872: [Bug]: Docker Hub's vllm-openai Docker image is *still* not usable since 0.14.

| 字段 | 值 |
| --- | --- |
| Issue | [#40872](https://github.com/vllm-project/vllm/issues/40872) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Docker Hub's vllm-openai Docker image is *still* not usable since 0.14.

### Issue 正文摘录

### Your current environment This is the original issue. I fear it's lost in the depths: https://github.com/vllm-project/vllm/issues/32755 This is the fix: https://github.com/vllm-project/vllm/pull/32809 I really hope this fix gets included into 0.20.0 or 0.20.1. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Docker Hub's vllm-openai Docker image is *still* not usable since 0.14. bug ### Your current environment This is the original issue. I fear it's lost in the depths: https://github.com/vllm-project/vllm/issues/327...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .1. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
