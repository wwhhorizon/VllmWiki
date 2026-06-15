# vllm-project/vllm#7289: [Feature]: Beam Search also requires diversity

| 字段 | 值 |
| --- | --- |
| Issue | [#7289](https://github.com/vllm-project/vllm/issues/7289) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Beam Search also requires diversity

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Basically in decoding stage, we use sampling strategy with parameters like top_p/top_k/temp/xx_penalty to control the diversity of the generated content. However beam_search is still very important at the moment, but lacks relevant parameters to control its diversity, which is already supported in HF as follows: HammingDiversityLogitsProcessor：https://huggingface.co/docs/transformers/zh/internal/generation_utils#transformers.HammingDiversityLogitsProcessor ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: evant parameters to control its diversity, which is already supported in HF as follows: HammingDiversityLogitsProcessor：https://huggingface.co/docs/transformers/zh/internal/generation_utils#transformers.HammingDiversity...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Beam Search also requires diversity feature request;stale ### 🚀 The feature, motivation and pitch Basically in decoding stage, we use sampling strategy with parameters like top_p/top_k/temp/xx_penalty to cont...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he diversity of the generated content. However beam_search is still very important at the moment, but lacks relevant parameters to control its diversity, which is already supported in HF as follows: HammingDiversityLogi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Beam Search also requires diversity feature request;stale ### 🚀 The feature, motivation and pitch Basically in decoding stage, we use sampling strategy with parameters like top_p/top_k/temp/xx_penalty to cont...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
