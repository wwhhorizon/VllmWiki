# vllm-project/vllm#4470: [Feature]: Sliding window attention in a fraction of layers

| 字段 | 值 |
| --- | --- |
| Issue | [#4470](https://github.com/vllm-project/vllm/issues/4470) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Sliding window attention in a fraction of layers

### Issue 正文摘录

### 🚀 The feature, motivation and pitch With the context length of models becoming longer and longer, the kvcache generated during inference will take trememdous amount of memory. A quite straight forward way to mitigate this problem is to let a fraction of layers in the model use sliding window attention (e.g. with a window size of 8k), so that the model can remain it's full capability in short context length and still have some long ICL ability (with the remaining full attention layers), making the memory vs long-context performance an adjustable trade-off. I wonder if the vllm community is interested in implementing such approach. And we'd love to help! Thank you :) ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Sliding window attention in a fraction of layers feature request;stale ### 🚀 The feature, motivation and pitch With the context length of models becoming longer and longer, the kvcache generated during infere...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: (e.g. with a window size of 8k), so that the model can remain it's full capability in short context length and still have some long ICL ability (with the remaining full attention layers), making the memory vs long-conte...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tale ### 🚀 The feature, motivation and pitch With the context length of models becoming longer and longer, the kvcache generated during inference will take trememdous amount of memory. A quite straight forward way to mi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
