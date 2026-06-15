# vllm-project/vllm#33951: [Feature]: Implement `get_kv_cache_stride_order` for all classes

| 字段 | 值 |
| --- | --- |
| Issue | [#33951](https://github.com/vllm-project/vllm/issues/33951) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Implement `get_kv_cache_stride_order` for all classes

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, `AttentionBackend.get_kv_cache_stride_order` raises a notImplementedError by default: https://github.com/vllm-project/vllm/blob/main/vllm/v1/attention/backend.py#L90 This causes this awkward usage in vLLM e.g. in https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu_model_runner.py#L5864: ``` try: kv_cache_stride_order = attn_backend.get_kv_cache_stride_order() except (AttributeError, NotImplementedError): kv_cache_stride_order = tuple(range(len(kv_cache_shape))) ``` We should instead make the default return the tuple(range(...)) object, then switch the usage across vLLM. https://github.com/vllm-project/vllm/pull/33948#discussion_r2771597517 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Implement `get_kv_cache_stride_order` for all classes feature request;stale ### 🚀 The feature, motivation and pitch Currently, `AttentionBackend.get_kv_cache_stride_order` raises a notImplementedError by defa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: uest;stale ### 🚀 The feature, motivation and pitch Currently, `AttentionBackend.get_kv_cache_stride_order` raises a notImplementedError by default: https://github.com/vllm-project/vllm/blob/main/vllm/v1/attention/backen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: Implement `get_kv_cache_stride_order` for all classes feature request;stale ### 🚀 The feature, motivation and pitch Currently, `AttentionBackend.get_kv_cache_stride_order` raises a notImplementedError by defa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .g. in https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu_model_runner.py#L5864: ``` try: kv_cache_stride_order = attn_backend.get_kv_cache_stride_order() except (AttributeError, NotImplementedError): kv_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
