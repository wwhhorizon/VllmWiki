# vllm-project/vllm#8535: [Installation]: Assets v0.6 for cuda 12+

| 字段 | 值 |
| --- | --- |
| Issue | [#8535](https://github.com/vllm-project/vllm/issues/8535) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Assets v0.6 for cuda 12+

### Issue 正文摘录

### Your current environment ```text my environment: cuda:12.1 ``` ### How you are installing vllm ```sh I'm using vllm release url：https://github.com/vllm-project/vllm/releases I was using vllm-0.5.4-cp39-cp39-manylinux1_x86_64.whl (https://github.com/vllmproject/vllm/releases/download/v0.5.4/vllm-0.5.4-cp39-cp39-manylinux1_x86_64.whl) From 0.5.5 I see only assets with cuda11.8, but I need with cuda12 or higher. Why are these assets missing? Thanks ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: Assets v0.6 for cuda 12+ installation ### Your current environment ```text my environment: cuda:12.1 ``` ### How you are installing vllm ```sh I'm using vllm release url：https://github.com/vllm-project/v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Installation]: Assets v0.6 for cuda 12+ installation ### Your current environment ```text my environment: cuda:12.1 ``` ### How you are installing vllm ```sh I'm using vllm release url：https://github.com/vllm-project/
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
