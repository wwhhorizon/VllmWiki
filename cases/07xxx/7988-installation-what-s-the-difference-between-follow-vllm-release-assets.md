# vllm-project/vllm#7988: [Installation]: What's the difference between follow vllm release assets?

| 字段 | 值 |
| --- | --- |
| Issue | [#7988](https://github.com/vllm-project/vllm/issues/7988) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: What's the difference between follow vllm release assets?

### Issue 正文摘录

### Your current environment gpu: T4 cuda:12.1 ### How you are installing vllm vllm release url：https://github.com/vllm-project/vllm/releases **What's the difference between vllm-0.5.4+cu118-cp310-cp310-manylinux1_x86_64.whl and vllm-0.5.4-cp310-cp310-manylinux1_x86_64.whl？** In my environment: cuda:12.1 does vllm-0.5.4-cp310-cp310-manylinux1_x86_64.whl means vllm-0.5.4+cu121？ How can i get vllm-0.5.4+cu121-cp310-cp310-manylinux1_x86_64.whl ? only way is compiling whl by source cde? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: vllm release assets? installation ### Your current environment gpu: T4 cuda:12.1 ### How you are installing vllm vllm release url：https://github.com/vllm-project/vllm/releases **What's the difference between vllm-0.5.4+...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Installation]: What's the difference between follow vllm release assets? installation ### Your current environment gpu: T4 cuda:12.1 ### How you are installing vllm vllm release url：https://github.com/vllm-project/vll
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
