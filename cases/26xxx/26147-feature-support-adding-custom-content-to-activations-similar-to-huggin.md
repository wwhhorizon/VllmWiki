# vllm-project/vllm#26147: [Feature]: Support adding custom content to activations similar to HuggingFace

| 字段 | 值 |
| --- | --- |
| Issue | [#26147](https://github.com/vllm-project/vllm/issues/26147) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support adding custom content to activations similar to HuggingFace

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I hope vllm can support an API similar to HuggingFace that allows directly adding custom content to activations. For example, HuggingFace enables: def set_add_activations(self, layer, activations): self.model.model.layers[layer].add(activations) This would make it more flexible to insert or modify intermediate activations, which is useful for research and customization. ### Alternatives Currently, this can only be achieved by modifying the underlying source code or using hooks, which lack a unified interface and are not flexible enough. ### Additional context Refer to HuggingFace's implementation. If vllm could support a similar API, it would be much easier to perform customized operations at the activation stage. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support adding custom content to activations similar to HuggingFace feature request;stale ### 🚀 The feature, motivation and pitch I hope vllm can support an API similar to HuggingFace that allows directly add...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: port adding custom content to activations similar to HuggingFace feature request;stale ### 🚀 The feature, motivation and pitch I hope vllm can support an API similar to HuggingFace that allows directly adding custom con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: le to insert or modify intermediate activations, which is useful for research and customization. ### Alternatives Currently, this can only be achieved by modifying the underlying source code or using hooks, which lack a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
