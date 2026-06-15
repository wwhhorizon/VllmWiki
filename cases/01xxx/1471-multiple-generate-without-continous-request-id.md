# vllm-project/vllm#1471: multiple generate, without continous request_id

| 字段 | 值 |
| --- | --- |
| Issue | [#1471](https://github.com/vllm-project/vllm/issues/1471) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> multiple generate, without continous request_id

### Issue 正文摘录

Hi Due to some data logics I need run `llm.generate` several times, and I need some id to know if any request is success or not. I tried using`request_id`, but found that the `request_id`s are successive. I.E: ``` # 1st time llm.generate return a list of output with `request_id` 0, 1, 2, 3 # 2nd time llm.generate return a list of output with `request_id` 4, 5, 6 ``` What I need is such kind of ids: ``` # 1st time llm.generate return a list of output with `request_id` 0, 1, 2, 3 # 2nd time llm.generate return a list of output with `request_id` 0, 1, 2 ``` Any approach to get this? Thanks.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: multiple generate, without continous request_id Hi Due to some data logics I need run `llm.generate` several times, and I need some id to know if any request is success or not. I tried using`request_id`, but found that...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
