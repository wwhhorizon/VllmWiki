# vllm-project/vllm#13601: [Usage] [V1] Refactor speculative decoding configuration

| 字段 | 值 |
| --- | --- |
| Issue | [#13601](https://github.com/vllm-project/vllm/issues/13601) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage] [V1] Refactor speculative decoding configuration

### Issue 正文摘录

Make it hierarchical like the compilation config.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage] [V1] Refactor speculative decoding configuration Make it hierarchical like the compilation config.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage] [V1] Refactor speculative decoding configuration Make it hierarchical like the compilation config.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage] [V1] Refactor speculative decoding configuration Make it hierarchical like the compilation config.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
