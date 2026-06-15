# vllm-project/vllm#704: why not support llama 7b？

| 字段 | 值 |
| --- | --- |
| Issue | [#704](https://github.com/vllm-project/vllm/issues/704) |
| 状态 | closed |
| 标签 |  |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> why not support llama 7b？

### Issue 正文摘录

Do we have any plan to support llama 7b? I try to support llama 7b, but failed. Maybe dependences mismatch with huggingface ？

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: why not support llama 7b？ Do we have any plan to support llama 7b? I try to support llama 7b, but failed. Maybe dependences mismatch with huggingface ？
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: port llama 7b? I try to support llama 7b, but failed. Maybe dependences mismatch with huggingface ？
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rt llama 7b? I try to support llama 7b, but failed. Maybe dependences mismatch with huggingface ？

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
