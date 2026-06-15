# vllm-project/vllm#7339: [Feature]: Small Model Large Latency Compared to SGLang and TensorRT-LLM

| 字段 | 值 |
| --- | --- |
| Issue | [#7339](https://github.com/vllm-project/vllm/issues/7339) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Small Model Large Latency Compared to SGLang and TensorRT-LLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In this post, https://lmsys.org/blog/2024-07-25-sglang-llama3/, it looks like vllm is not efficient in small model size in both online and offline benchmark. What is the bottleneck for vllm for small model inference and whether this will be addressed to catch SGLang and TensorRT performance. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Small Model Large Latency Compared to SGLang and TensorRT-LLM feature request ### 🚀 The feature, motivation and pitch In this post, https://lmsys.org/blog/2024-07-25-sglang-llama3/, it looks like vllm is not...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Small Model Large Latency Compared to SGLang and TensorRT-LLM feature request ### 🚀 The feature, motivation and pitch In this post, https://lmsys.org/blog/2024-07-25-sglang-llama3/, it looks like vllm is not...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /lmsys.org/blog/2024-07-25-sglang-llama3/, it looks like vllm is not efficient in small model size in both online and offline benchmark. What is the bottleneck for vllm for small model inference and whether this will be...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Small Model Large Latency Compared to SGLang and TensorRT-LLM feature request ### 🚀 The feature, motivation and pitch In this post, https://lmsys.org/blog/2024-07-25-sglang-llama3/, it looks like vllm is not...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: Small Model Large Latency Compared to SGLang and TensorRT-LLM feature request ### 🚀 The feature, motivation and pitch In this post, https://lmsys.org/blog/2024-07-25-sglang-llama3/, it looks like vllm is not efficien...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
