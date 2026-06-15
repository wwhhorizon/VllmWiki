# vllm-project/vllm#2526: [RFC] Speedup vLLM inference with Intel@ Extension for PyTorch*

| 字段 | 值 |
| --- | --- |
| Issue | [#2526](https://github.com/vllm-project/vllm/issues/2526) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC] Speedup vLLM inference with Intel@ Extension for PyTorch*

### Issue 正文摘录

## Motivation In the current technological landscape, Generative AI (GenAI) workloads and models have gained widespread attention and popularity. Large Language Models (LLMs) have emerged as the dominant models driving these GenAI applications. Most of LLMs are GPT-like architectures that consist of multiple Decoder layers. The MultiHeadAttention and FeedForward layer are two key components of every Decoder layer. The generation task is memory bound because iterative decode and kv_cache require special management to reduce memory overheads. Intel® Extension for PyTorch* provides a lot of specific optimizations for these LLMs. On the operator level, the extension provides highly efficient GEMM kernel to speed up Linear layer and customized operators to reduce the memory footprint. To better trade-off the performance and accuracy, different low-precision solutions e.g., smoothQuant and weight-only-quantization are also enabled. Besides, tensor parallel can also adopt to get lower latency for LLMs and we also enable the shared memory based all-reduce to reduce the latency of all-reduce. We already integrated Intel@ Extension for PyTorch* into huggingface ([#RFC](https://github.com/hu...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: the current technological landscape, Generative AI (GenAI) workloads and models have gained widespread attention and popularity. Large Language Models (LLMs) have emerged as the dominant models driving these GenAI appli...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: to reduce the memory footprint. To better trade-off the performance and accuracy, different low-precision solutions e.g., smoothQuant and weight-only-quantization are also enabled. Besides, tensor parallel can also adop...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: performance and accuracy, different low-precision solutions e.g., smoothQuant and weight-only-quantization are also enabled. Besides, tensor parallel can also adopt to get lower latency for LLMs and we also enable the s...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ed linear kernels for weight only quantization. All of them use specific block format to utilize hardware resources in a highly efficient way. ### Low Precision Data Types While Generative AI (GenAI) workloads and model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: inant models driving these GenAI applications. Most of LLMs are GPT-like architectures that consist of multiple Decoder layers. The MultiHeadAttention and FeedForward layer are two key components of every Decoder layer....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
