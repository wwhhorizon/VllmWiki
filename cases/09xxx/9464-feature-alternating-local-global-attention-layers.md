# vllm-project/vllm#9464: [Feature]: Alternating local-global attention layers

| 字段 | 值 |
| --- | --- |
| Issue | [#9464](https://github.com/vllm-project/vllm/issues/9464) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Alternating local-global attention layers

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Gemma-2 and new Ministral models use alternating sliding window and full attention layers to reduce the size of the KV cache. The KV cache is a huge inference bottleneck and this technique could be fine-tuned into other models to make them much more memory efficient, especially for large batch sizes. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: on layers feature request;stale ### 🚀 The feature, motivation and pitch Gemma-2 and new Ministral models use alternating sliding window and full attention layers to reduce the size of the KV cache. The KV cache is a hug...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Alternating local-global attention layers feature request;stale ### 🚀 The feature, motivation and pitch Gemma-2 and new Ministral models use alternating sliding window and full attention layers to reduce the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: could be fine-tuned into other models to make them much more memory efficient, especially for large batch sizes. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ating sliding window and full attention layers to reduce the size of the KV cache. The KV cache is a huge inference bottleneck and this technique could be fine-tuned into other models to make them much more memory effic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
