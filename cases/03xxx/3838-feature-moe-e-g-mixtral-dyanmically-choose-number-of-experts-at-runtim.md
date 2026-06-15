# vllm-project/vllm#3838: [Feature]: MoE (e.g. Mixtral) dyanmically choose number of experts at runtime

| 字段 | 值 |
| --- | --- |
| Issue | [#3838](https://github.com/vllm-project/vllm/issues/3838) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: MoE (e.g. Mixtral) dyanmically choose number of experts at runtime

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Often times we want to balance performance and speed. One could use Mixtral + Mistral 7B in a setup and use separate GPUs etc. However, this is wasteful. It would be more efficient if Mixtral could be triggered to use a single 7B expert and somehow be as efficient as a single 7B if possible. If the attention layers still make it computationally less efficient than just a single 7B, then probably not best idea. ### Alternatives 2 models: Mixtral + Mistral 7B ### Additional context _No response_

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: MoE (e.g. Mixtral) dyanmically choose number of experts at runtime feature request ### 🚀 The feature, motivation and pitch Often times we want to balance performance and speed. One could use Mixtral + Mistral...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: use separate GPUs etc. However, this is wasteful. It would be more efficient if Mixtral could be triggered to use a single 7B expert and somehow be as efficient as a single 7B if possible. If the attention layers still...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: than just a single 7B, then probably not best idea. ### Alternatives 2 models: Mixtral + Mistral 7B ### Additional context _No response_
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: E (e.g. Mixtral) dyanmically choose number of experts at runtime feature request ### 🚀 The feature, motivation and pitch Often times we want to balance performance and speed. One could use Mixtral + Mistral 7B in a setu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
