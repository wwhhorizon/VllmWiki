# vllm-project/vllm#35267: [Feature]: Integrate RadixMLP into vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#35267](https://github.com/vllm-project/vllm/issues/35267) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integrate RadixMLP into vLLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm wondering whether vLLM would consider supporting RadixMLP-style intra-batch deduplication for the prefill path. The high-level idea of RadixMLP is that it deduplicates position-wise computations (e.g., norms / linear projections / MLP-related activations) for tokens that have identical prefix, while running attention on the original expanded layout. This shall be complimentary to vLLM’s existing prefix caching / KV-cache mechanisms. That said, as the paper notes, the integration effort appears non-trivial. Paper: https://arxiv.org/pdf/2601.15013 Code: https://github.com/michaelfeil/radix-mlp ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Integrate RadixMLP into vLLM feature request;stale ### 🚀 The feature, motivation and pitch I'm wondering whether vLLM would consider supporting RadixMLP-style intra-batch deduplication for the prefill path. T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: all be complimentary to vLLM’s existing prefix caching / KV-cache mechanisms. That said, as the paper notes, the integration effort appears non-trivial. Paper: https://arxiv.org/pdf/2601.15013 Code: https://github.com/m...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ayout. This shall be complimentary to vLLM’s existing prefix caching / KV-cache mechanisms. That said, as the paper notes, the integration effort appears non-trivial. Paper: https://arxiv.org/pdf/2601.15013 Code: https:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: have identical prefix, while running attention on the original expanded layout. This shall be complimentary to vLLM’s existing prefix caching / KV-cache mechanisms. That said, as the paper notes, the integration effort...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
