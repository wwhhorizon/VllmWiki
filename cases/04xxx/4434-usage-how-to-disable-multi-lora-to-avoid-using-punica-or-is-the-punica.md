# vllm-project/vllm#4434: [Usage]: How to disable multi lora to avoid using punica ? Or is the punica being the only choice?

| 字段 | 值 |
| --- | --- |
| Issue | [#4434](https://github.com/vllm-project/vllm/issues/4434) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to disable multi lora to avoid using punica ? Or is the punica being the only choice?

### Issue 正文摘录

I searched the outdated issues, and everyone is saying that the version of multi lora's punica must be >=8.0. Therefore, I want to ask if there is an option that only uses a standalone lora but supports cuda=7.5? I have tried examples/offline_inference.py, which llm.generate with only 1 lora. But it still ran into punica, and then it prompted that cuda>=8 is required.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d using punica ? Or is the punica being the only choice? usage;stale I searched the outdated issues, and everyone is saying that the version of multi lora's punica must be >=8.0. Therefore, I want to ask if there is an...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ge;stale I searched the outdated issues, and everyone is saying that the version of multi lora's punica must be >=8.0. Therefore, I want to ask if there is an option that only uses a standalone lora but supports cuda=7....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ra to avoid using punica ? Or is the punica being the only choice? usage;stale I searched the outdated issues, and everyone is saying that the version of multi lora's punica must be >=8.0. Therefore, I want to ask if th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
