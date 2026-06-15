# vllm-project/vllm#2742: When using tp =2 to inference model in greedy mode  and vllm 0.3 , results are random

| 字段 | 值 |
| --- | --- |
| Issue | [#2742](https://github.com/vllm-project/vllm/issues/2742) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> When using tp =2 to inference model in greedy mode  and vllm 0.3 , results are random

### Issue 正文摘录

When using tp =2 to inference model in greedy model and vllm 0.3 , the results are random, not same. But when I use --disable-custom-all-reduce, it's ok. My model structure is same to llama. I don't know why ?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: When using tp =2 to inference model in greedy mode and vllm 0.3 , results are random stale When using tp =2 to inference model in greedy model and vllm 0.3 , the results are random, not same. But when I use --disable-cu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: =2 to inference model in greedy mode and vllm 0.3 , results are random stale When using tp =2 to inference model in greedy model and vllm 0.3 , the results are random, not same. But when I use --disable-custom-all-reduc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
