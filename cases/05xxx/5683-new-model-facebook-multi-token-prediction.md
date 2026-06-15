# vllm-project/vllm#5683: [New Model]: facebook/multi-token-prediction 

| 字段 | 值 |
| --- | --- |
| Issue | [#5683](https://github.com/vllm-project/vllm/issues/5683) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: facebook/multi-token-prediction 

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Multi token prediction may be a promising way to accelerate the inference of the model. The community is also interested in this model. [Multi token prediction huggingface link ](https://huggingface.co/facebook/multi-token-prediction) [Multi token prediction paper link ](https://arxiv.org/abs/2404.19737) ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: facebook/multi-token-prediction feature request;stale ### 🚀 The feature, motivation and pitch Multi token prediction may be a promising way to accelerate the inference of the model. The community is also in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [New Model]: facebook/multi-token-prediction feature request;stale ### 🚀 The feature, motivation and pitch Multi token prediction may be a promising way to accelerate the inference of the model. The community is also in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ty is also interested in this model. [Multi token prediction huggingface link ](https://huggingface.co/facebook/multi-token-prediction) [Multi token prediction paper link ](https://arxiv.org/abs/2404.19737) ### Alternat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
