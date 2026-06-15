# vllm-project/vllm#2893: Will Vllm Lora support SGMV in handling multi-Lora request?

| 字段 | 值 |
| --- | --- |
| Issue | [#2893](https://github.com/vllm-project/vllm/issues/2893) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Will Vllm Lora support SGMV in handling multi-Lora request?

### Issue 正文摘录

In the multi-lora feature, vllm refer to the BGMV in punica. Yet in the punica project(https://github.com/punica-ai/punica), the authors said SGMV (Segmented Gather Matrix-Vector Multiplication) is more flexible. Is there a plan to support SGMV in the community?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Will Vllm Lora support SGMV in handling multi-Lora request? In the multi-lora feature, vllm refer to the BGMV in punica. Yet in the punica project(https://github.com/punica-ai/punica), the authors said SGMV (Segmented G...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
