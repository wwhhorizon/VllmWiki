# vllm-project/vllm#14513: [Usage]: How to improve concurrent processing capacity

| 字段 | 值 |
| --- | --- |
| Issue | [#14513](https://github.com/vllm-project/vllm/issues/14513) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to improve concurrent processing capacity

### Issue 正文摘录

### Your current environment vllm version: 0.6.1.post2 When I was testing the performance at 200 concurrent users, I found that vLLM can handle up to 100 requests at most. ![Image](https://github.com/user-attachments/assets/941c2fcf-30fd-4e67-a74f-46a43cdfa571) After each request is processed, a new request will be added, but the maximum number of requests is 100. Below is my startup script. ![Image](https://github.com/user-attachments/assets/8f9857b9-81e5-401b-891d-8cae195733ba) So，my question is how to increase the number of concurrent connections from 100 to 200 or more？ Thank you。 ### How would you like to use vllm I want to increase the number of concurrent connections from 100 to 200 or more.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Usage]: How to improve concurrent processing capacity usage ### Your current environment vllm version: 0.6.1.post2 When I was testing the performance at 200 concurrent users, I found that vLLM can handle up to 100 requ...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: formance at 200 concurrent users, I found that vLLM can handle up to 100 requests at most. ![Image](https://github.com/user-attachments/assets/941c2fcf-30fd-4e67-a74f-46a43cdfa571) After each request is processed, a new...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: sage ### Your current environment vllm version: 0.6.1.post2 When I was testing the performance at 200 concurrent users, I found that vLLM can handle up to 100 requests at most. ![Image](https://github.com/user-attachmen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
