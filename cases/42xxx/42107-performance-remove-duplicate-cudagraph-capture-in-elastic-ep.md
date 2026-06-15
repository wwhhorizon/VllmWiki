# vllm-project/vllm#42107: [Performance]: Remove duplicate cudagraph capture in elastic EP

| 字段 | 值 |
| --- | --- |
| Issue | [#42107](https://github.com/vllm-project/vllm/issues/42107) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Remove duplicate cudagraph capture in elastic EP

### Issue 正文摘录

Remove double cudgraph capture introduced in: https://github.com/vllm-project/vllm/pull/41792 per https://github.com/vllm-project/vllm/pull/41792#pullrequestreview-4253860752

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Performance]: Remove duplicate cudagraph capture in elastic EP performance Remove double cudgraph capture introduced in: https://github.com/vllm-project/vllm/pull/41792 per https://github.com/vllm-project/vllm/pull/417...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: /vllm/pull/41792 per https://github.com/vllm-project/vllm/pull/41792#pullrequestreview-4253860752

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
