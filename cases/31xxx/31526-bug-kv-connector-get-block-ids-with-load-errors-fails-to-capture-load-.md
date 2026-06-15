# vllm-project/vllm#31526: [Bug]: kv_connector.get_block_ids_with_load_errors fails to capture load errors in PD separation scenario when P-side uses layer_wise KV cache loading

| 字段 | 值 |
| --- | --- |
| Issue | [#31526](https://github.com/vllm-project/vllm/issues/31526) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: kv_connector.get_block_ids_with_load_errors fails to capture load errors in PD separation scenario when P-side uses layer_wise KV cache loading

### Issue 正文摘录

### Your current environment - ### 🐛 Describe the bug In a Prefill-Decode (PD) separation architecture, the get_block_ids_with_load_errors method in the KV connector is unable to properly handle and report errors when the Prefill (P) worker loads the KV cache in a layer_wise manner. The method currently only captures load failures in non-layer_wise cache loading scenarios, leaving layer_wise loading errors on the P-side undetected. This can lead to silent failures and incorrect execution. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: oading bug ### Your current environment - ### 🐛 Describe the bug In a Prefill-Decode (PD) separation architecture, the get_block_ids_with_load_errors method in the KV connector is unable to properly handle and report er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ironment - ### 🐛 Describe the bug In a Prefill-Decode (PD) separation architecture, the get_block_ids_with_load_errors method in the KV connector is unable to properly handle and report errors when the Prefill (P) worke...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: apture load errors in PD separation scenario when P-side uses layer_wise KV cache loading bug ### Your current environment - ### 🐛 Describe the bug In a Prefill-Decode (PD) separation architecture, the get_block_ids_wit...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: kv_connector.get_block_ids_with_load_errors fails to capture load errors in PD separation scenario when P-side uses layer_wise KV cache loading bug ### Your current environment - ### 🐛 Describe the bug In a Prefi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
