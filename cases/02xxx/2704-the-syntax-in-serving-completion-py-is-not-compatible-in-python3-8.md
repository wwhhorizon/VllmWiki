# vllm-project/vllm#2704: the syntax in serving_completion.py is not compatible in python3.8

| 字段 | 值 |
| --- | --- |
| Issue | [#2704](https://github.com/vllm-project/vllm/issues/2704) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> the syntax in serving_completion.py is not compatible in python3.8

### Issue 正文摘录

in #2529 @simon-mo introduce some python typing syntax, which is not compatible in python3.8 like TypeTokenIDs = list[int] in https://github.com/vllm-project/vllm/blob/93b38bea5dd03e1b140ca997dfaadef86f8f1855/vllm/entrypoints/openai/serving_completion.py#L22C1-L22C25 which should be TypeTokenIDs=List[int] in python3.8. could you please fix it?

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
