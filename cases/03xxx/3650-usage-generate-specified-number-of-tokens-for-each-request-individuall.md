# vllm-project/vllm#3650: [Usage]: Generate specified number of tokens for each request individually

| 字段 | 值 |
| --- | --- |
| Issue | [#3650](https://github.com/vllm-project/vllm/issues/3650) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Generate specified number of tokens for each request individually

### Issue 正文摘录

### Your current environment VLLM with python 3.9, Ubuntu 20 ### How would you like to use vllm How can I specify the number of generated tokens for each request individually in both online serving mode and offline batching mode? For example, three requests with 100 tokens generated for request 1, 200 for request 2 and 300 for request 3. In both offline and online mode, three requests can be processed in a batch and return the specified number of tokens.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: Generate specified number of tokens for each request individually usage ### Your current environment VLLM with python 3.9, Ubuntu 20 ### How would you like to use vllm How can I specify the number of generated...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Generate specified number of tokens for each request individually usage ### Your current environment VLLM with python 3.9, Ubuntu 20 ### How would you like to use vllm How can I specify the number of generated...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
