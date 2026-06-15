# vllm-project/vllm#7752: [Feature]: Integrate with `Formatron`

| 字段 | 值 |
| --- | --- |
| Issue | [#7752](https://github.com/vllm-project/vllm/issues/7752) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integrate with `Formatron`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch While we already have `Outlines` and `lm-format-enforcer` integration, they are implemented purely in Python and may suffer from Python interpreter overhead like reports from several users in this [issue](https://github.com/vllm-project/vllm/issues/3567). Maybe we can integrate with [Formatron](https://github.com/Dan-wanna-M/formatron) which uses a Rust backend and supports efficient regex/json/context free grammar-constrained generation? If we are willing to integrate, the actual integration should be quite straightforward since we already have `logits_processors` interface and another option in the flag --guided-decoding-backend=... should not be too difficult to add? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Integrate with `Formatron` feature request;stale ### 🚀 The feature, motivation and pitch While we already have `Outlines` and `lm-format-enforcer` integration, they are implemented purely in Python and may su...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Formatron](https://github.com/Dan-wanna-M/formatron) which uses a Rust backend and supports efficient regex/json/context free grammar-constrained generation? If we are willing to integrate, the actual integration shoul...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ub.com/Dan-wanna-M/formatron) which uses a Rust backend and supports efficient regex/json/context free grammar-constrained generation? If we are willing to integrate, the actual integration should be quite straightforwa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Integrate with `Formatron` feature request;stale ### 🚀 The feature, motivation and pitch While we already have `Outlines` and `lm-format-enforcer` integration, they are implemented purely in Python and may su...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
