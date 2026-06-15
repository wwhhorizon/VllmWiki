# vllm-project/vllm#1568: [new feature] flash decoding ++

| 字段 | 值 |
| --- | --- |
| Issue | [#1568](https://github.com/vllm-project/vllm/issues/1568) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [new feature] flash decoding ++

### Issue 正文摘录

Recently flashdecoding++ is introduced by below paper. It could boost the decoding efficiency. Would you like to implement that? https://arxiv.org/pdf/2311.01282.pdf Thank you in advance.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [new feature] flash decoding ++ feature request;stale Recently flashdecoding++ is introduced by below paper. It could boost the decoding efficiency. Would you like to implement that? https://arxiv.org/pdf/2311.01282.pdf...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: decoding++ is introduced by below paper. It could boost the decoding efficiency. Would you like to implement that? https://arxiv.org/pdf/2311.01282.pdf Thank you in advance.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
