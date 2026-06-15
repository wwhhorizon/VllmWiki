# vllm-project/vllm#3278: Does vLLM have a plan to support multi-node connection with cupy in cuda graph mode?

| 字段 | 值 |
| --- | --- |
| Issue | [#3278](https://github.com/vllm-project/vllm/issues/3278) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Does vLLM have a plan to support multi-node connection with cupy in cuda graph mode?

### Issue 正文摘录

Does vLLM have a plan to support multi-node connection with cupy in cuda graph mode?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n to support multi-node connection with cupy in cuda graph mode? feature request;stale Does vLLM have a plan to support multi-node connection with cupy in cuda graph mode?
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Does vLLM have a plan to support multi-node connection with cupy in cuda graph mode? feature request;stale Does vLLM have a plan to support multi-node connection with cupy in cuda graph mode?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
