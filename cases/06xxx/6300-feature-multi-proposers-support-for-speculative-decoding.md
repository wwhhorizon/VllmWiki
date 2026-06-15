# vllm-project/vllm#6300: [Feature]: Multi-Proposers support for speculative decoding.

| 字段 | 值 |
| --- | --- |
| Issue | [#6300](https://github.com/vllm-project/vllm/issues/6300) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Multi-Proposers support for speculative decoding.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Speculative decoding has demonstrated significant potential in efficiently generating proposals and utilizing idle computing power to expedite the auto-regression decoding process, particularly under lightweight workloads. Thanks to the remarkable work by @cadedaniel, we have verified the latency benefits brought by speculative decoding on the latest version of vllm. We have observed the following points that we believe could further enhance the utility of speculative decoding: * **Ngram Proposer:** While the 'Ngram' proposer can offer a 2x to 3x performance improvement in Retrieval-Augmented Generation (RAG) scenarios, its performance diminishes when the RAG module retrieves no relevant data for a query. * **Draft-Model-Based Proposers:** In contrast, draft-model-based proposers have exhibited higher acceptance rates when the RAG module retrieves no relevant data or faces a more creative task. Yet the performance of this type of implementation is not fully optimized (#4630 #5561). So the current performance gains are limited. We sincerely thank the open-source community for their efforts and hope all this progress will be smooth. * **Creati...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Feature]: Multi-Proposers support for speculative decoding. feature request;stale ### 🚀 The feature, motivation and pitch Speculative decoding has demonstrated significant potential in efficiently generating proposals...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: rating proposals and utilizing idle computing power to expedite the auto-regression decoding process, particularly under lightweight workloads. Thanks to the remarkable work by @cadedaniel, we have verified the latency...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: itch Speculative decoding has demonstrated significant potential in efficiently generating proposals and utilizing idle computing power to expedite the auto-regression decoding process, particularly under lightweight wo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: en-source community for their efforts and hope all this progress will be smooth. * **Creative Tasks with High Temperature:** We have noticed that both proposer methods exhibit lower performance compared to non-spec impl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s when the RAG module retrieves no relevant data for a query. * **Draft-Model-Based Proposers:** In contrast, draft-model-based proposers have exhibited higher acceptance rates when the RAG module retrieves no relevant...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
