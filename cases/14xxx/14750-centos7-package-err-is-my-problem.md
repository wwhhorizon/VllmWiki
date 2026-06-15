# vllm-project/vllm#14750: centos7 package err, is my problem?

| 字段 | 值 |
| --- | --- |
| Issue | [#14750](https://github.com/vllm-project/vllm/issues/14750) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> centos7 package err, is my problem?

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/382403921f18c22f6c4b6c8391fd19b9d21a84ee/csrc/cpu/utils.cpp#L84 ![Image](https://github.com/user-attachments/assets/58922a03-ccb9-424f-a660-1e2b81dce068) os: centos7 python: 3.10.16

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: centos7 package err, is my problem? stale https://github.com/vllm-project/vllm/blob/382403921f18c22f6c4b6c8391fd19b9d21a84ee/csrc/cpu/utils.cpp#L84 ![Image](https://github.com/user-attachments/assets/58922a03-ccb9-424f-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
