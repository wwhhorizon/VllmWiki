# vllm-project/vllm#4669: [Feature]: Support for a draft model that takes inputs from base model (to support Medusa/EAGLE/Hydra)

| 字段 | 值 |
| --- | --- |
| Issue | [#4669](https://github.com/vllm-project/vllm/issues/4669) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for a draft model that takes inputs from base model (to support Medusa/EAGLE/Hydra)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In approaches like Medusa/EAGLE/Hydra, the speculative model uses the last hidden states from the base model to propose candidates. This feature will allow any such approaches to be implemented with ease. One idea is to store the required base model's outputs along with the sequence and then use that while generating candidates for the next iteration. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Support for a draft model that takes inputs from base model (to support Medusa/EAGLE/Hydra) feature request ### 🚀 The feature, motivation and pitch In approaches like Medusa/EAGLE/Hydra, the speculative model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support for a draft model that takes inputs from base model (to support Medusa/EAGLE/Hydra) feature request ### 🚀 The feature, motivation and pitch In approaches like Medusa/EAGLE/Hydra, the speculative model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
