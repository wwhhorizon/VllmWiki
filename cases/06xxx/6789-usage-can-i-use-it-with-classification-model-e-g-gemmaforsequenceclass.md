# vllm-project/vllm#6789: [Usage]: can I use it with classification model (e.g. GemmaForSequenceClassification) ?

| 字段 | 值 |
| --- | --- |
| Issue | [#6789](https://github.com/vllm-project/vllm/issues/6789) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: can I use it with classification model (e.g. GemmaForSequenceClassification) ?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm can I use it with classification model (e.g. GemmaForSequenceClassification) ?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: can I use it with classification model (e.g. GemmaForSequenceClassification) ? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm can I...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: can I use it with classification model (e.g. GemmaForSequenceClassification) ? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm can I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: with classification model (e.g. GemmaForSequenceClassification) ? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm can I use it with classific...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
