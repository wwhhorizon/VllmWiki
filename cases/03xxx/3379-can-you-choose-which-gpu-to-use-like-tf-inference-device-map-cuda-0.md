# vllm-project/vllm#3379: Can you choose which GPU to use. like  tf inference  device_map="cuda:0"

| 字段 | 值 |
| --- | --- |
| Issue | [#3379](https://github.com/vllm-project/vllm/issues/3379) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can you choose which GPU to use. like  tf inference  device_map="cuda:0"

### Issue 正文摘录

As the title suggests

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Can you choose which GPU to use. like tf inference device_map="cuda:0" stale As the title suggests
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Can you choose which GPU to use. like tf inference device_map="cuda:0" stale As the title suggests

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
