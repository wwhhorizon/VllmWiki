# vllm-project/vllm#3714: [Feature]: Integrate with AICI

| 字段 | 值 |
| --- | --- |
| Issue | [#3714](https://github.com/vllm-project/vllm/issues/3714) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integrate with AICI

### Issue 正文摘录

### 🚀 The feature, motivation and pitch #2888 added a prototype for AI Controller Interface, which is a WASM based runtime for guided generation. We would like to integrate this into our existing guided decoding stack properly. Related is lm-format-enforcer #3713. We should tell the users strength of each framework and let the user choose. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Integrate with AICI feature request;stale ### 🚀 The feature, motivation and pitch #2888 added a prototype for AI Controller Interface, which is a WASM based runtime for guided generation. We would like to int...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Integrate with AICI feature request;stale ### 🚀 The feature, motivation and pitch #2888 added a prototype for AI Controller Interface, which is a WASM based runtime for guided generation. We would like to int...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pitch #2888 added a prototype for AI Controller Interface, which is a WASM based runtime for guided generation. We would like to integrate this into our existing guided decoding stack properly. Related is lm-format-enfo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e this into our existing guided decoding stack properly. Related is lm-format-enforcer #3713. We should tell the users strength of each framework and let the user choose. ### Alternatives _No response_ ### Additional co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
