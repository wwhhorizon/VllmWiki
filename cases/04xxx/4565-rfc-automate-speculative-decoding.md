# vllm-project/vllm#4565: [RFC]: Automate Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#4565](https://github.com/vllm-project/vllm/issues/4565) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Automate Speculative Decoding

### Issue 正文摘录

### Motivation. Speculative Decoding is a crucial feature for reducing latency, currently supported by vLLM (credit to @cadedaniel !). However, when deploying Speculative Decoding in real online LLM serving systems that use continuous batching, improvements are not always observed. Paradoxically, under conditions of high request rates or low speculation accuracy, latency may actually increase. We propose to address these issues. We want to intelligently determines the optimal speculation length for each request, ranging from zero (no speculation) to multiple tokens. This determination is based on the concept of goodput, which reflects the current observed load across the entire system, thus allowing for most effective speculative execution. The method is designed for versatility, compatible with various speculative decoding styles, from traditional, model-based approaches to model-free methods such as prompt lookup and tree-style decoding. This innovation builds on recent research by the vLLM team. We plan to release the detailed paper shortly. ### Proposed Change. **Milestone 1:** Implement a mechanism to disable speculative decoding (proposed length = verified length = 0), allow...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [RFC]: Automate Speculative Decoding RFC;stale ### Motivation. Speculative Decoding is a crucial feature for reducing latency, currently supported by vLLM (credit to @cadedaniel !). However, when deploying Speculative D...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: , compatible with various speculative decoding styles, from traditional, model-based approaches to model-free methods such as prompt lookup and tree-style decoding. This innovation builds on recent research by the vLLM...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ### Motivation. Speculative Decoding is a crucial feature for reducing latency, currently supported by vLLM (credit to @cadedaniel !). However, when deploying Speculative Decoding in real online LLM serving systems that...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ulative Decoding RFC;stale ### Motivation. Speculative Decoding is a crucial feature for reducing latency, currently supported by vLLM (credit to @cadedaniel !). However, when deploying Speculative Decoding in real onli...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: mpt lookup and tree-style decoding. This innovation builds on recent research by the vLLM team. We plan to release the detailed paper shortly. ### Proposed Change. **Milestone 1:** Implement a mechanism to disable specu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
