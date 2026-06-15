# vllm-project/vllm#2474: Using VLLM to Accelerate Chatglm3 with Multiple Cards and Output Errors:tensor-parallel-size 8

| 字段 | 值 |
| --- | --- |
| Issue | [#2474](https://github.com/vllm-project/vllm/issues/2474) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Using VLLM to Accelerate Chatglm3 with Multiple Cards and Output Errors:tensor-parallel-size 8

### Issue 正文摘录

when i set tensor-parallel-size 8, the decode output error: Generate a large number of duplicate error texts ![image](https://github.com/vllm-project/vllm/assets/156979199/ab15555a-a52a-459c-8c5f-8a9cd64abd4a)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: put Errors:tensor-parallel-size 8 when i set tensor-parallel-size 8, the decode output error: Generate a large number of duplicate error texts ![image](https://github.com/vllm-project/vllm/assets/156979199/ab15555a-a52a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
