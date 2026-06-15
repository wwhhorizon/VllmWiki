# vllm-project/vllm#3957: [Bug]: initialization hang if define an environment variable HOST_IP

| 字段 | 值 |
| --- | --- |
| Issue | [#3957](https://github.com/vllm-project/vllm/issues/3957) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: initialization hang if define an environment variable HOST_IP

### Issue 正文摘录

### Your current environment ```text vllm will hang when we define an environment variable HOST_IP, is it expected? ``` ![image](https://github.com/vllm-project/vllm/assets/5827720/fb08abc8-1962-4db2-9709-780a125f8bd6) ### 🐛 Describe the bug It should start normally.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: initialization hang if define an environment variable HOST_IP bug;stale ### Your current environment ```text vllm will hang when we define an environment variable HOST_IP, is it expected? ``` ![image](https://git...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
