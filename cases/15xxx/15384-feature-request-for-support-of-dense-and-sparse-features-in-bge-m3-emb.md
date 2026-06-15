# vllm-project/vllm#15384: [Feature]: Request for Support of Dense and Sparse Features in bge-m3 Embedding Model

| 字段 | 值 |
| --- | --- |
| Issue | [#15384](https://github.com/vllm-project/vllm/issues/15384) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Request for Support of Dense and Sparse Features in bge-m3 Embedding Model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Dear VLLM Team, I hope this message finds you well. I am writing to request support for the bge-m3 embedding model, specifically regarding the implementation of dense and sparse features. The bge-m3 model, available at https://modelscope.cn/models/BAAI/bge-m3, is a promising embedding model that I believe could significantly enhance our capabilities in various NLP tasks. However, to fully leverage its potential, it is crucial to support both dense and sparse feature representations. Dense embeddings are essential for capturing the nuanced relationships within the data, while sparse embeddings can be highly beneficial for handling large vocabularies and reducing computational overhead. Supporting both dense and sparse features would make the bge-m3 model more versatile and applicable to a wider range of use cases. I kindly ask if you could consider adding support for dense and sparse features in the bge-m3 model. It would be greatly appreciated if you could also share the roadmap or timeline for this feature implementation, if available. Thank you very much for your attention to this request. I look forward to your response and the possibilit...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tions. Dense embeddings are essential for capturing the nuanced relationships within the data, while sparse embeddings can be highly beneficial for handling large vocabularies and reducing computational overhead. Suppor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Request for Support of Dense and Sparse Features in bge-m3 Embedding Model feature request;stale ### 🚀 The feature, motivation and pitch Dear VLLM Team, I hope this message finds you well. I am writing to req...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: well. I am writing to request support for the bge-m3 embedding model, specifically regarding the implementation of dense and sparse features. The bge-m3 model, available at https://modelscope.cn/models/BAAI/bge-m3, is a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e]: Request for Support of Dense and Sparse Features in bge-m3 Embedding Model feature request;stale ### 🚀 The feature, motivation and pitch Dear VLLM Team, I hope this message finds you well. I am writing to request su...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
