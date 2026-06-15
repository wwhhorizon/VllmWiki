# vllm-project/vllm#1171: [Discussion] Will vLLM consider using Speculative Sampling to accelerating LLM decoding?

| 字段 | 值 |
| --- | --- |
| Issue | [#1171](https://github.com/vllm-project/vllm/issues/1171) |
| 状态 | closed |
| 标签 |  |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Discussion] Will vLLM consider using Speculative Sampling to accelerating LLM decoding?

### Issue 正文摘录

Sampling is an already known bottleneck of vLLM(see #421 and #670 ). Last weekend I saw a project named [Medusa](https://github.com/FasterDecoding/Medusa), in it's [blog](https://sites.google.com/view/medusa-llm), it introduce a new simple decoding way to accelerate LLM generation and reach a good performance. As far as I known, [lepton.ai](https://www.lepton.ai/docs) is alreay use this method. Adopting Medusa Heads is not difficult, since there is no seperate model. But tree attention and typical acceptance scheme is not a standard process for most LLM inference framework and should take a huge effort. Any advice or comments?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: thod. Adopting Medusa Heads is not difficult, since there is no seperate model. But tree attention and typical acceptance scheme is not a standard process for most LLM inference framework and should take a huge effort....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Discussion] Will vLLM consider using Speculative Sampling to accelerating LLM decoding? Sampling is an already known bottleneck of vLLM(see #421 and #670 ). Last weekend I saw a project named [Medusa](https://github.co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
