# vllm-project/vllm#6272: [Doc]: Latency vs Throughput Configurations

| 字段 | 值 |
| --- | --- |
| Issue | [#6272](https://github.com/vllm-project/vllm/issues/6272) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Latency vs Throughput Configurations

### Issue 正文摘录

### 📚 The doc issue **Context:** During July 9, 2024, vLLM open office hours (FP8), there were several questions regarding how to **optimize** model deployment inference configurations targeting the two major regimes: **latency** and **throughput** (batch processing). Relevant articles around the same discussion, [Efficiently Scaling Transformer Inference](https://arxiv.org/pdf/2211.05102). Whereas there is an exploration of batch size, chip count and context length. Additionally we should explore the whole set of features (e.g optimized kernels, quantization strategies, pipeline/tensor/sequence parallelism) ### Suggest a potential alternative/fix **Targets:** Create documentation making explicit what configurations are suitable for each regime, and listing some of its constraints and tradeoffs. The creation of this documentation should add new benchmarking and experimental scripts for reproducing such results. Simultaneously this issue will list the set of compatible flags, thus helping understanding invalid deployment configurations.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Doc]: Latency vs Throughput Configurations documentation;stale ### 📚 The doc issue **Context:** During July 9, 2024, vLLM open office hours (FP8), there were several questions regarding how to **optimize** model deploy...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: The doc issue **Context:** During July 9, 2024, vLLM open office hours (FP8), there were several questions regarding how to **optimize** model deployment inference configurations targeting the two major regimes: **laten...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: xiv.org/pdf/2211.05102). Whereas there is an exploration of batch size, chip count and context length. Additionally we should explore the whole set of features (e.g optimized kernels, quantization strategies, pipeline/t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Doc]: Latency vs Throughput Configurations documentation;stale ### 📚 The doc issue **Context:** During July 9, 2024, vLLM open office hours (FP8), there were several questions regarding how to **optimize** model deploy...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: * (batch processing). Relevant articles around the same discussion, [Efficiently Scaling Transformer Inference](https://arxiv.org/pdf/2211.05102). Whereas there is an exploration of batch size, chip count and context le...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
