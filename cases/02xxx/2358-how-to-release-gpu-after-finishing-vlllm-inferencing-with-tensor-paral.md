# vllm-project/vllm#2358: How to release gpu after finishing vlllm inferencing with tensor parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#2358](https://github.com/vllm-project/vllm/issues/2358) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to release gpu after finishing vlllm inferencing with tensor parallel

### Issue 正文摘录

When vllm uses tensor parallel, it will create ray cluster. Is there a way to tear down the cluster? In my case, I run a job with tensor parallel, and I need to repeat the similar process. However, it cannot create the cluster in the 2nd job. It looks like the gpus are still not released from the cluster in the 1st job.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: How to release gpu after finishing vlllm inferencing with tensor parallel When vllm uses tensor parallel, it will create ray cluster. Is there a way to tear down the cluster? In my case, I run a job with tensor parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
