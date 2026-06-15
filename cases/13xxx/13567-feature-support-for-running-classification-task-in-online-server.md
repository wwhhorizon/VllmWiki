# vllm-project/vllm#13567: [Feature]: Support for Running Classification Task in Online Server

| 字段 | 值 |
| --- | --- |
| Issue | [#13567](https://github.com/vllm-project/vllm/issues/13567) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for Running Classification Task in Online Server

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I would like it to be easy to stand up models for sequence classification using the vllm online inference pattern. Currently this is available for offline inference but it would be nice to expose this server in kubernetes similar to how we host OpenAI compatible servers. ### Alternatives We could train a causal lm where we treat special tokens as the classification labels. We could then take the softmaxed logprobs for those 2 tokens to threshold. However this is going to require slightly more code on the client side. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: servers. ### Alternatives We could train a causal lm where we treat special tokens as the classification labels. We could then take the softmaxed logprobs for those 2 tokens to threshold. However this is going to requir...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: he feature, motivation and pitch I would like it to be easy to stand up models for sequence classification using the vllm online inference pattern. Currently this is available for offline inference but it would be nice...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lassification Task in Online Server help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch I would like it to be easy to stand up models for sequence classification using the vllm online in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
