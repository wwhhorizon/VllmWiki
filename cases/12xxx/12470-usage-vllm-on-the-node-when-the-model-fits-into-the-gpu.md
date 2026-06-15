# vllm-project/vllm#12470: [Usage]: VLLM on the node when the model fits into the GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#12470](https://github.com/vllm-project/vllm/issues/12470) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: VLLM on the node when the model fits into the GPU

### Issue 正文摘录

### Your current environment Hey everyone! ### How would you like to use vllm I have a GPU node with 4 GPU, each one individually can serve the model with max-model-lens What is the most efficient way to configure vllm for this node to get (one of): 1. min latency 2. max throughput Thank you ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: st efficient way to configure vllm for this node to get (one of): 1. min latency 2. max throughput Thank you ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: VLLM on the node when the model fits into the GPU usage ### Your current environment Hey everyone! ### How would you like to use vllm I have a GPU node with 4 GPU, each one individually can serve the model with...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ndividually can serve the model with max-model-lens What is the most efficient way to configure vllm for this node to get (one of): 1. min latency 2. max throughput Thank you ### Before submitting a new issue... - [x] M...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: you ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
