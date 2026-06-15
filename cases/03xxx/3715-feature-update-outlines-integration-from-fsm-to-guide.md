# vllm-project/vllm#3715: [Feature]: Update Outlines Integration from `FSM` to `Guide`

| 字段 | 值 |
| --- | --- |
| Issue | [#3715](https://github.com/vllm-project/vllm/issues/3715) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Update Outlines Integration from `FSM` to `Guide`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Recently outlines updated their interface from FSM to Guide to support "acceleration"/"fast-forward" which will output next sets of tokens if they are directly available. For JSON schema, the cases are the keys, the `"`, and `}` etc. This is non-trivial but very useful to improve vLLM for. It should also help other framework like AICI #3714. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: y useful to improve vLLM for. It should also help other framework like AICI #3714. ### Alternatives _No response_ ### Additional context _No response_
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Update Outlines Integration from `FSM` to `Guide` feature request ### 🚀 The feature, motivation and pitch Recently outlines updated their interface from FSM to Guide to support "acceleration"/"fast-forward" w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Update Outlines Integration from `FSM` to `Guide` feature request ### 🚀 The feature, motivation and pitch Recently outlines updated their interface from FSM to Guide to support "acceleration"/"fast-forward" w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
