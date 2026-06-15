# vllm-project/vllm#5433: [Feature]: Add guided-* Parameters to Sampling Parameters

| 字段 | 值 |
| --- | --- |
| Issue | [#5433](https://github.com/vllm-project/vllm/issues/5433) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add guided-* Parameters to Sampling Parameters

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The openai endpoint of vllm now supports passing guided grammar in the request body. However, the current sampling parameters do not include corresponding parameters for guided grammar. This limitation prevents me from using guided grammar while utilizing the LLM Engine. Please add support for guided-* parameters in the sampling parameters to enable the use of guided grammar with the LLM Engine. With the addition of guided-* parameters in the sampling parameters, users will be able to leverage guided grammar in conjunction with the LLM Engine, enhancing the flexibility and functionality of the model. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: able to leverage guided grammar in conjunction with the LLM Engine, enhancing the flexibility and functionality of the model. ### Alternatives _No response_ ### Additional context _No response_
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: with the LLM Engine, enhancing the flexibility and functionality of the model. ### Alternatives _No response_ ### Additional context _No response_
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add guided-* Parameters to Sampling Parameters feature request ### 🚀 The feature, motivation and pitch The openai endpoint of vllm now supports passing guided grammar in the request body. However, the current...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
