# vllm-project/vllm#30261: [Bug]: The new Version of VLLM cannot detect the 2 GPUs versions.

| 字段 | 值 |
| --- | --- |
| Issue | [#30261](https://github.com/vllm-project/vllm/issues/30261) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The new Version of VLLM cannot detect the 2 GPUs versions.

### Issue 正文摘录

### Your current environment [Bug] vLLM: ValueError 'Tensor parallel size (2) cannot be larger than the number of available GPUs (1)' on 2-GPU node ### 🐛 Describe the bug What I expected: 2 GPUs visible. What actually happened: vLLM sees 1 GPU and raises that specific ValueError ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: The new Version of VLLM cannot detect the 2 GPUs versions. bug ### Your current environment [Bug] vLLM: ValueError 'Tensor parallel size (2) cannot be larger than the number of available GPUs (1)' on 2-GPU node #...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ror ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
