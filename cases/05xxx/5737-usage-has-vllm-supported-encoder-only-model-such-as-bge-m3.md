# vllm-project/vllm#5737: [Usage]: has vllm supported encoder-only model such as bge-m3?

| 字段 | 值 |
| --- | --- |
| Issue | [#5737](https://github.com/vllm-project/vllm/issues/5737) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: has vllm supported encoder-only model such as bge-m3?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I saw an issue here: https://github.com/vllm-project/vllm/pull/3187/files ![image](https://github.com/vllm-project/vllm/assets/167943259/93d820cf-678e-480c-89a5-f858b360092e) I want to know has vllm supported embedding model in RAG? such as BAAI/bge-m3. and how to use it?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: has vllm supported encoder-only model such as bge-m3? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I saw an issue here: https://g...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: has vllm supported encoder-only model such as bge-m3? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I saw an issue here: https://g...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
