# vllm-project/vllm#3406: How to run multiple mixtral in one machine

| 字段 | 值 |
| --- | --- |
| Issue | [#3406](https://github.com/vllm-project/vllm/issues/3406) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to run multiple mixtral in one machine

### Issue 正文摘录

I have an 8xA100 GPU machine. I noticed that one Mixtral instance requires at least 2 GPUs. However, when I attempt to run two Mixtral instances on the machine, each allocated 2 GPUs, the second one hangs at `Started a local Ray instance.` Additionally, the terminal reports `fork: retry: Resource temporarily unavailable`. It appears that the two Ray instances are causing a conflict. Is there any solution to resolve this issue?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: How to run multiple mixtral in one machine I have an 8xA100 GPU machine. I noticed that one Mixtral instance requires at least 2 GPUs. However, when I attempt to run two Mixtral instances on the machine, each allocated...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
