# vllm-project/vllm#10754: [Feature]: Beam search: top_p, min_p and logit processors

| 字段 | 值 |
| --- | --- |
| Issue | [#10754](https://github.com/vllm-project/vllm/issues/10754) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Beam search: top_p, min_p and logit processors

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Dear vllm community, we recently deprecated beam search from the core library, in favour of a new method called `beam_search`. However, this new method is far less powerful than before and it restrict the possibilities of applying beam search to many use cases. For example, by controlling the generation (top_p etc) or doing constrained beam search (e.g. https://huggingface.co/blog/constrained-beam-search). We, at Spotify, use 0.6.1 for this reason. I am sure that many more are doing the same. However, we would like to move to pytorch 2.5 to fully use our h100s, FSDP2 etc. Moreover, we would like to stay up-to-date with vllm Could we consider moving these parameters in the new method as well? Thaaaaank you! ref https://github.com/vllm-project/vllm/issues/6226 ### Alternatives Huggingface ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Beam search: top_p, min_p and logit processors feature request;stale ### 🚀 The feature, motivation and pitch Dear vllm community, we recently deprecated beam search from the core library, in favour of a new m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Beam search: top_p, min_p and logit processors feature request;stale ### 🚀 The feature, motivation and pitch Dear vllm community, we recently deprecated beam search from the core library, in favour of a new m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: he generation (top_p etc) or doing constrained beam search (e.g. https://huggingface.co/blog/constrained-beam-search). We, at Spotify, use 0.6.1 for this reason. I am sure that many more are doing the same. However, we...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
