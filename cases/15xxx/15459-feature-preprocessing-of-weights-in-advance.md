# vllm-project/vllm#15459: [Feature]: preprocessing of weights in advance

| 字段 | 值 |
| --- | --- |
| Issue | [#15459](https://github.com/vllm-project/vllm/issues/15459) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: preprocessing of weights in advance

### Issue 正文摘录

### 🚀 The feature, motivation and pitch If hardware inherently requires decompression of pre-compressed weight data, feeding weights into the hardware would necessitate on-the-fly compression before each operator execution, thereby introducing significant performance overhead. Currently, vLLM performs weight partitioning and compression during weight loading (e.g., SliceGPT's matrix slicing strategy1). However, this approach faces critical limitations: - High Latency: Sequential partitioning and compression prolong loading time; - Redundant Computation: Dynamic compression consumes CPU resources and prevents preprocessing optimization; - Inflexibility: User-defined compression algorithms struggle to integrate into real-time workflows. **Proposed Solution:** Integrate weight partitioning (e.g., DP/EP/PP slicing2) and user-defined compression into a standalone preprocessing tool to generate pre-compressed, partitioned weight files. This would: - Reduce Loading Overhead: Directly load preprocessed weights, eliminating runtime computational costs; - Enable Hardware-Specific Optimization: Tailor compression strategies to hardware characteristics (e.g., GPU memory bandwidth1); - Enhance...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: preprocessing of weights in advance feature request;stale ### 🚀 The feature, motivation and pitch If hardware inherently requires decompression of pre-compressed weight data, feeding weights into the hardware...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: g strategy1). However, this approach faces critical limitations: - High Latency: Sequential partitioning and compression prolong loading time; - Redundant Computation: Dynamic compression consumes CPU resources and prev...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: te on-the-fly compression before each operator execution, thereby introducing significant performance overhead. Currently, vLLM performs weight partitioning and compression during weight loading (e.g., SliceGPT's matrix...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ty: Standardize interfaces for diverse compression algorithms (e.g., NF4 quantization2). ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you alrea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
