# vllm-project/vllm#18115: [Usage]: --preemption-mode is not supported by the V1 Engine. Falling back to V0.

| 字段 | 值 |
| --- | --- |
| Issue | [#18115](https://github.com/vllm-project/vllm/issues/18115) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: --preemption-mode is not supported by the V1 Engine. Falling back to V0.

### Issue 正文摘录

May I ask if the v1 engine does not provide an interface for setting the preemption strategy? If so, where is the preemption mechanism implemented in the v1 engine, and what strategy does it use by default?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: r setting the preemption strategy? If so, where is the preemption mechanism implemented in the v1 engine, and what strategy does it use by default?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: mption-mode is not supported by the V1 Engine. Falling back to V0. usage;stale May I ask if the v1 engine does not provide an interface for setting the preemption strategy? If so, where is the preemption mechanism imple...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
