# vllm-project/vllm#17172: [Usage]: I want to create custom docker image by adding my code

| 字段 | 值 |
| --- | --- |
| Issue | [#17172](https://github.com/vllm-project/vllm/issues/17172) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: I want to create custom docker image by adding my code

### Issue 正文摘录

### Your current environment I would like to create a custom Docker image by writing a Dockerfile and copying my code inside it. ### How would you like to use vllm ```text I am using **vllm/vllm-openai** docker image from docker hub for running vLLM in docker by mounting locally downloaded model using docker volume. Now, I want to create custom docker image by copying my code inside this base image? How should I write custom Docker file by taking vllm/vllm-openai as a base docker image? Thank you! ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: I want to create custom docker image by adding my code usage ### Your current environment I would like to create a custom Docker image by writing a Dockerfile and copying my code inside it. ### How would you li...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rom docker hub for running vLLM in docker by mounting locally downloaded model using docker volume. Now, I want to create custom docker image by copying my code inside this base image? How should I write custom Docker f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
