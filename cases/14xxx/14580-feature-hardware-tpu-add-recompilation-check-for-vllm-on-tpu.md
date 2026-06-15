# vllm-project/vllm#14580: [Feature][Hardware][TPU]: Add Recompilation Check for vLLM on TPU

| 字段 | 值 |
| --- | --- |
| Issue | [#14580](https://github.com/vllm-project/vllm/issues/14580) |
| 状态 | closed |
| 标签 | feature request;tpu |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Hardware][TPU]: Add Recompilation Check for vLLM on TPU

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Ideally, post-warmup, no further compilation should occur. However, PyTorch/XLA's implicit compilation can lead to excessive recompilation during LLM serving, impacting performance. We can add an option to detect recompilation after warmup, requiring a PyTorch/XLA method like xm.num_graph_hash() to track the number of captured graphs. This number should remain constant post-warmup if no recompilation occurs. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: warmup, no further compilation should occur. However, PyTorch/XLA's implicit compilation can lead to excessive recompilation during LLM serving, impacting performance. We can add an option to detect recompilation after...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Feature][Hardware][TPU]: Add Recompilation Check for vLLM on TPU feature request;tpu ### 🚀 The feature, motivation and pitch Ideally, post-warmup, no further compilation should occur. However, PyTorch/XLA's implicit com...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
