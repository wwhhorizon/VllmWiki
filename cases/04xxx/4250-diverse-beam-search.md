# vllm-project/vllm#4250: Diverse Beam Search

| 字段 | 值 |
| --- | --- |
| Issue | [#4250](https://github.com/vllm-project/vllm/issues/4250) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Diverse Beam Search

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Now vllm cannot support diverse beam search which transformers already supports(https://huggingface.co/docs/transformers/generation_strategies#diverse-beam-search-decoding), will you implement diverse beam search in vllm? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Diverse Beam Search feature request;stale ### 🚀 The feature, motivation and pitch Now vllm cannot support diverse beam search which transformers already supports(https://huggingface.co/docs/transformers/generation_strat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Diverse Beam Search feature request;stale ### 🚀 The feature, motivation and pitch Now vllm cannot support diverse beam search which transformers already supports(https://huggingface.co/docs/transformers/generation_strat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: support diverse beam search which transformers already supports(https://huggingface.co/docs/transformers/generation_strategies#diverse-beam-search-decoding), will you implement diverse beam search in vllm? ### Alternati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
