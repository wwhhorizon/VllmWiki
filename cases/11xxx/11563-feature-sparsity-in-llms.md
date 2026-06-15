# vllm-project/vllm#11563: [Feature]: Sparsity in LLMs

| 字段 | 值 |
| --- | --- |
| Issue | [#11563](https://github.com/vllm-project/vllm/issues/11563) |
| 状态 | closed |
| 标签 | feature request;rocm;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Sparsity in LLMs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Great action for support 2:4 sparsity (with quantization) in vllm for nvidia Ampere+ architectures! I wonder 2:4 sparsity support in AMD MI300/MI300X+ Accelerators, Will this be the roadmap of the future? Will you provide unstructured sparsity support in the future? Flash-LLM (https://github.com/AlibabaResearch/flash-llm) currently provides 1.3x end-to-end acceleration of 70% unstructured sparse LLM on NVIDIA GPUs. Thanks~ ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Feature]: Sparsity in LLMs feature request;rocm;stale ### 🚀 The feature, motivation and pitch Great action for support 2:4 sparsity (with quantization) in vllm for nvidia Ampere+ architectures! I wonder 2:4 sparsity su...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Sparsity in LLMs feature request;rocm;stale ### 🚀 The feature, motivation and pitch Great action for support 2:4 sparsity (with quantization) in vllm for nvidia Ampere+ architectures! I wonder 2:4 sparsity su...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ature, motivation and pitch Great action for support 2:4 sparsity (with quantization) in vllm for nvidia Ampere+ architectures! I wonder 2:4 sparsity support in AMD MI300/MI300X+ Accelerators, Will this be the roadmap o...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
