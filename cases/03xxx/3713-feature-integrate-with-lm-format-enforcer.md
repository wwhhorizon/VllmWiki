# vllm-project/vllm#3713: [Feature]: Integrate with lm-format-enforcer

| 字段 | 值 |
| --- | --- |
| Issue | [#3713](https://github.com/vllm-project/vllm/issues/3713) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integrate with lm-format-enforcer

### Issue 正文摘录

### 🚀 The feature, motivation and pitch While existing Outline state machine provide great state of the art performance, it is trading off a one-off compile time when working with the schema. For endpoint products running model as a service with customers supplying many different schemas, the cost might not be acceptable. In that case, we should integrate with lm-format-enforcer from @noamgat. We already have an existing logits processor interface and guided decoding tested. It should be quite straightforward to add it integration for it. In the end it should be some flag choosing `--guided-decoding-backend=...`. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Integrate with lm-format-enforcer feature request ### 🚀 The feature, motivation and pitch While existing Outline state machine provide great state of the art performance, it is trading off a one-off compile t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: on for it. In the end it should be some flag choosing `--guided-decoding-backend=...`. ### Alternatives _No response_ ### Additional context _No response_
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: provide great state of the art performance, it is trading off a one-off compile time when working with the schema. For endpoint products running model as a service with customers supplying many different schemas, the co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Integrate with lm-format-enforcer feature request ### 🚀 The feature, motivation and pitch While existing Outline state machine provide great state of the art performance, it is trading off a one-off compile t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: already have an existing logits processor interface and guided decoding tested. It should be quite straightforward to add it integration for it. In the end it should be some flag choosing `--guided-decoding-backend=...`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
