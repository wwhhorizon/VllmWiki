# vllm-project/vllm#7543: [Usage]: Access weight of model with tp=2

| 字段 | 值 |
| --- | --- |
| Issue | [#7543](https://github.com/vllm-project/vllm/issues/7543) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Access weight of model with tp=2

### Issue 正文摘录

### Your current environment vllm 0.5.3.post1 vllm-flash-attn 2.5.9.post1 ### How would you like to use vllm For model w/o distributed setting, we can directly access the model's weight in eager mode like this ``` model.llm_engine.model_executor.driver_worker.model_runner.model ``` However, when we're using the model w tp=2 (distributed setting), we can only access part of the weight via above code. I am wondering if there is a way that we can access the full weight.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Access weight of model with tp=2 usage ### Your current environment vllm 0.5.3.post1 vllm-flash-attn 2.5.9.post1 ### How would you like to use vllm For model w/o distributed setting, we c

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
