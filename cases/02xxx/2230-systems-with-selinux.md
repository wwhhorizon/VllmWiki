# vllm-project/vllm#2230: systems with SELinux

| 字段 | 值 |
| --- | --- |
| Issue | [#2230](https://github.com/vllm-project/vllm/issues/2230) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> systems with SELinux

### Issue 正文摘录

Hi. Whenever I start my api_serverr.py on a selinux enabled system, the server gets stuck at "Started a local Ray instance" and nothing else happens. Does selinux prohibit spawning multi-processes or workers? Is it not compatible with Ray?

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: em, the server gets stuck at "Started a local Ray instance" and nothing else happens. Does selinux prohibit spawning multi-processes or workers? Is it not compatible with Ray?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: systems with SELinux stale Hi. Whenever I start my api_serverr.py on a selinux enabled system, the server gets stuck at "Started a local Ray instance" and nothing else happens. Does selinux prohibit spawning multi-proce...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
