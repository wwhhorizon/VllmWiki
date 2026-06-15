# vllm-project/vllm#7124: [RFC]: Model architecture plugins

| 字段 | 值 |
| --- | --- |
| Issue | [#7124](https://github.com/vllm-project/vllm/issues/7124) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Model architecture plugins

### Issue 正文摘录

### Motivation. As a continuation to #5367 - as this merge request was rejected and I have to maintain my own fork to support this scenario, I suggest we should add support in vLLM for model architecture plugins. This will allow vLLM to easily add new model architectures without changing vLLM's core logic, and support scenarios such as uneven GPU tensor parallelism. We could build an ecosystem of model architecture plugins - which could accelerate new model support by a lot without risking existing functionality. ### Proposed Change. Supporting this in it's basic form is simple as we just have to add loaded plugins to the `ModelRegistry`. To support more complex model architectures (Such in the #5367 case), we should decouple the `Config` class which provides the amount of attention heads from vLLM's core logic, and allow each model architecture to override these values. ### Feedback Period. _No response_ ### CC List. @youkaichao ### Any Other Things. Just to make it clear, I'll be happy to implement this, but I want hear some feedback before I go ahead and implement this.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Model architecture plugins RFC;stale ### Motivation. As a continuation to #5367 - as this merge request was rejected and I have to maintain my own fork to support this scenario, I suggest we should add support in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: Model architecture plugins RFC;stale ### Motivation. As a continuation to #5367 - as this merge request was rejected and I have to maintain my own fork to support this scenario, I suggest we should add support in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Model architecture plugins RFC;stale ### Motivation. As a continuation to #5367 - as this merge request was rejected and I have to maintain my own fork to support this scenario, I suggest we should add support in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: , and support scenarios such as uneven GPU tensor parallelism. We could build an ecosystem of model architecture plugins - which could accelerate new model support by a lot without risking existing functionality. ### Pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
