# vllm-project/vllm#1809: vllm-master（0.2.2）多卡并行推理乱码，单卡推理正常，使用了llama的Muilti-Query推理，请问是什么问题？

| 字段 | 值 |
| --- | --- |
| Issue | [#1809](https://github.com/vllm-project/vllm/issues/1809) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm-master（0.2.2）多卡并行推理乱码，单卡推理正常，使用了llama的Muilti-Query推理，请问是什么问题？

### Issue 正文摘录

vllm：0.2.2 pytorch：2.1.0 cuda：12.1 driver: 525.85.12 使用llama，muilti-query（num_key_value_heads=1）推理，发现单卡推理结果正常，多卡推理结果会有乱码和重复。请问怎么解决？

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 卡并行推理乱码，单卡推理正常，使用了llama的Muilti-Query推理，请问是什么问题？ vllm：0.2.2 pytorch：2.1.0 cuda：12.1 driver: 525.85.12 使用llama，muilti-query（num_key_value_heads=1）推理，发现单卡推理结果正常，多卡推理结果会有乱码和重复。请问怎么解决？
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vllm-master（0.2.2）多卡并行推理乱码，单卡推理正常，使用了llama的Muilti-Query推理，请问是什么问题？ vllm：0.2.2 pytorch：2.1.0 cuda：12.1 driver: 525.85.12 使用llama，muilti-query（num_key_value_heads=1）推理，发现单卡推理结果正常，多卡推理结果会有乱码和重复。请问怎么解决？

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
