# vllm-project/vllm#3979: [Usage]: Vllm inference slower for LoRA models

| 字段 | 值 |
| --- | --- |
| Issue | [#3979](https://github.com/vllm-project/vllm/issues/3979) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Vllm inference slower for LoRA models

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm when running LoRA trained models using Vllm see lower inference speed when compared to Non-LoRA trained models. Is there anything causing this ?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Vllm inference slower for LoRA models usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm when running LoRA trained models using Vllm see lowe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
