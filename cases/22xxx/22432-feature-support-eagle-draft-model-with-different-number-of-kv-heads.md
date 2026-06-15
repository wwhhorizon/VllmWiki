# vllm-project/vllm#22432: [Feature]: Support Eagle Draft Model with different number of KV heads

| 字段 | 值 |
| --- | --- |
| Issue | [#22432](https://github.com/vllm-project/vllm/issues/22432) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Eagle Draft Model with different number of KV heads

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The current EAGLE implementation raises `NotImplementedError` (https://github.com/vllm-project/vllm/blob/8e8e0b6af189d262bcfdaef6c0cfb94772e86b0b/vllm/v1/core/kv_cache_utils.py#L1098), because of different `page_size_bytes` calculation ( https://github.com/vllm-project/vllm/blob/main/vllm/v1/kv_cache_interface.py#L68 ) when using a draft model with different `num_kv_heads` compared to the target model. However in practice, we can have draft models trained with different `num_kv_heads` than the target model. Would that be possible to implement this change? Or it would require a lot of architectural changes? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support Eagle Draft Model with different number of KV heads feature request ### 🚀 The feature, motivation and pitch The current EAGLE implementation raises `NotImplementedError` (https://github.com/vllm-proje...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: that be possible to implement this change? Or it would require a lot of architectural changes? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 4772e86b0b/vllm/v1/core/kv_cache_utils.py#L1098), because of different `page_size_bytes` calculation ( https://github.com/vllm-project/vllm/blob/main/vllm/v1/kv_cache_interface.py#L68 ) when using a draft model with dif...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support Eagle Draft Model with different number of KV heads feature request ### 🚀 The feature, motivation and pitch The current EAGLE implementation raises `NotImplementedError` (https://github.com/vllm-proje...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
