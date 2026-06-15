# vllm-project/vllm#18815: [Feature]: vllm/v1/attention/backends/blocksparse_attn.py

| 字段 | 值 |
| --- | --- |
| Issue | [#18815](https://github.com/vllm-project/vllm/issues/18815) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: vllm/v1/attention/backends/blocksparse_attn.py

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Right now, `get_attn_backend` selects v0 vllm/attention/backends/blocksparse_attn.py, regardless of whether we are in v1. https://github.com/vllm-project/vllm/blob/b78f844a6743732b58022f2f84858d61b40b5913/vllm/attention/selector.py#L118-L122 This will cause all models using blocksparse attention to crash. The feature request is to implement a vllm/v1/attention/backends/blocksparse_attn.py, which does not exist currently. ### Alternatives It may also make sense to: - In `get_attn_backend`, detect if the selected attention backend is v0 but `use_v1=True`. In this case, a more helpful warning/error message can be provided. ### Additional context This is discovered from an opaque error message in serving Phi3Small: https://github.com/vllm-project/vllm/pull/16493#issuecomment-2915137285 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: context This is discovered from an opaque error message in serving Phi3Small: https://github.com/vllm-project/vllm/pull/16493#issuecomment-2915137285 ### Before submitting a new issue... - [x] Make sure you already sear...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: vllm/v1/attention/backends/blocksparse_attn.py feature request;stale ### 🚀 The feature, motivation and pitch Right now, `get_attn_backend` selects v0 vllm/attention/backends/blocksparse_attn.py, regardless of...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: vllm/v1/attention/backends/blocksparse_attn.py feature request;stale ### 🚀 The feature, motivation and pitch Right now, `get_attn_backend` selects v0 vllm/attention/backends/blocksparse_attn.py, regardless of...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: vllm/v1/attention/backends/blocksparse_attn.py feature request;stale ### 🚀 The feature, motivation and pitch Right now, `get_attn_backend` selects v0 vllm/attention/backends/blocksparse_attn.py, regardless of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 858d61b40b5913/vllm/attention/selector.py#L118-L122 This will cause all models using blocksparse attention to crash. The feature request is to implement a vllm/v1/attention/backends/blocksparse_attn.py, which does not e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
