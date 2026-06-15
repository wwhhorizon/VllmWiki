# vllm-project/vllm#33458: [Feature][Speculative Decoding]: Multi Modal Draft Model Support

| 字段 | 值 |
| --- | --- |
| Issue | [#33458](https://github.com/vllm-project/vllm/issues/33458) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Speculative Decoding]: Multi Modal Draft Model Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, multimodal EAGLE drafters are supported, but only for EAGLE drafters and only when not using parallel drafting. This is due to some complexity in managing the MRoPe position embeddings and multimodal state that has not been explored for external drafters. It may turn out to be quite simple to update the draft model / parallel drafting support to handle multimodal inputs. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature][Speculative Decoding]: Multi Modal Draft Model Support feature request;stale ### 🚀 The feature, motivation and pitch Currently, multimodal EAGLE drafters are supported, but only for EAGLE drafters and only whe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature][Speculative Decoding]: Multi Modal Draft Model Support feature request;stale ### 🚀 The feature, motivation and pitch Currently, multimodal EAGLE drafters are supported, but only for EAGLE drafters and only whe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
