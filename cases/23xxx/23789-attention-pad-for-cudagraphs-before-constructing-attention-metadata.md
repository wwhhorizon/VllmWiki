# vllm-project/vllm#23789: [Attention]: Pad for cudagraphs before constructing attention metadata

| 字段 | 值 |
| --- | --- |
| Issue | [#23789](https://github.com/vllm-project/vllm/issues/23789) |
| 状态 | closed |
| 标签 | help wanted;feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Attention]: Pad for cudagraphs before constructing attention metadata

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently we pad for cudagraphs: https://github.com/vllm-project/vllm/blob/853c371fc33e7c99aa2ab9f6e2cd7cbd1cadcf99/vllm/v1/worker/gpu_model_runner.py#L1497 after constructing the metadata: https://github.com/vllm-project/vllm/blob/853c371fc33e7c99aa2ab9f6e2cd7cbd1cadcf99/vllm/v1/worker/gpu_model_runner.py#L820-L909 This creates headaches for making attention backends with ahead-of-time schedulers cudagraph compatible e.g. FlashMLA and FlashAttn. This is because the scheduler might be called with a batch size smaller then what the graph is running with; e.g. we recently had to work around this in FlashMLA (https://github.com/vllm-project/FlashMLA/pull/3). Moving the padding calculation before metadata construction and passing padded `CommonAttentionMetadata` is much better long term solution though since the we won't have to work around this in future attention kernels. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/lates...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Attention]: Pad for cudagraphs before constructing attention metadata help wanted;feature request ### 🚀 The feature, motivation and pitch Currently we pad for cudagraphs: https://github.com/vllm-project/vllm/blob/853c3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: or cudagraphs before constructing attention metadata help wanted;feature request ### 🚀 The feature, motivation and pitch Currently we pad for cudagraphs: https://github.com/vllm-project/vllm/blob/853c371fc33e7c99aa2ab9f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: u_model_runner.py#L820-L909 This creates headaches for making attention backends with ahead-of-time schedulers cudagraph compatible e.g. FlashMLA and FlashAttn. This is because the scheduler might be called with a batch...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Attention]: Pad for cudagraphs before constructing attention metadata help wanted;feature request ### 🚀 The feature, motivation and pitch Currently we pad for cudagraphs: https://github.com/vllm-project/vllm/blob/853c3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ct/vllm/blob/853c371fc33e7c99aa2ab9f6e2cd7cbd1cadcf99/vllm/v1/worker/gpu_model_runner.py#L1497 after constructing the metadata: https://github.com/vllm-project/vllm/blob/853c371fc33e7c99aa2ab9f6e2cd7cbd1cadcf99/vllm/v1/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
