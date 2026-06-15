# vllm-project/vllm#5682: [Usage]: Recommended setting for running vLLM for CPU 

| 字段 | 值 |
| --- | --- |
| Issue | [#5682](https://github.com/vllm-project/vllm/issues/5682) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Recommended setting for running vLLM for CPU 

### Issue 正文摘录

### How would you like to use vllm What are the recommended settings for running vLLM on a CPU to achieve high performance? For instance, if I have a dual-socket server with 96 cores per socket, how many cores (--cpuset-cpus) should be allocated to run multiple replicas of vLLM?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Recommended setting for running vLLM for CPU usage;stale ### How would you like to use vllm What are the recommended settings for running vLLM on a CPU to achieve high performance? For instance, if I have a dua...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
