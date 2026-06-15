# vllm-project/vllm#17362: [Bug]: swap_blocks and copy_blocks functions are wrong in flashinfer.py

| 字段 | 值 |
| --- | --- |
| Issue | [#17362](https://github.com/vllm-project/vllm/issues/17362) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: swap_blocks and copy_blocks functions are wrong in flashinfer.py

### Issue 正文摘录

### Your current environment Code Exceptions. ### 🐛 Describe the bug Because the kv cache shape of FlashInfer is different with PageAttention/FlashAttention, the original swap/copy function path is not usable for FlashInfer. However, Flashinfer still uses the old swap/copy method, which will cause exceptions in some situations (like using swap space/beam search). Positions: get kv cache shape with [[num_blocks, 2, ...]](https://github.com/vllm-project/vllm/blob/main/vllm/attention/backends/flashinfer.py#L85), however treat shape as [[2, num_blocks ...]](https://github.com/vllm-project/vllm/blob/main/vllm/attention/backends/flashinfer.py#L101) in PagedAttention. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: swap_blocks and copy_blocks functions are wrong in flashinfer.py bug;stale ### Your current environment Code Exceptions. ### 🐛 Describe the bug Because the kv cache shape of FlashInfer is different with PageAtten...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: h will cause exceptions in some situations (like using swap space/beam search). Positions: get kv cache shape with [[num_blocks, 2, ...]](https://github.com/vllm-project/vllm/blob/main/vllm/attention/backends/flashinfer...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: rrent environment Code Exceptions. ### 🐛 Describe the bug Because the kv cache shape of FlashInfer is different with PageAttention/FlashAttention, the original swap/copy function path is not usable for FlashInfer. Howev...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: swap_blocks and copy_blocks functions are wrong in flashinfer.py bug;stale ### Your current environment Code Exceptions. ### 🐛 Describe the bug Because the kv cache shape of FlashInfer is different with PageAtten...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g]: swap_blocks and copy_blocks functions are wrong in flashinfer.py bug;stale ### Your current environment Code Exceptions. ### 🐛 Describe the bug Because the kv cache shape of FlashInfer is different with PageAttentio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
