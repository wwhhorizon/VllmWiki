# vllm-project/vllm#6825: [Usage]: How to use vLLM on multi-nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#6825](https://github.com/vllm-project/vllm/issues/6825) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use vLLM on multi-nodes

### Issue 正文摘录

### Your current environment n nodes * 8 A100 ### How would you like to use vllm I want to deploy qwen2 model on multi nodes to speed up inference, but large TP may make it not a division of att heads and raise error, and PP is not implemented on qwen2. In fact, several independent parallel models on each node ensemble at one port may help. Is there any way to do that or achieve similar effects.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n nodes * 8 A100 ### How would you like to use vllm I want to deploy qwen2 model on multi nodes to speed up inference, but large TP may make it not a division of att heads and raise error, and PP is not implemented on q...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: use vLLM on multi-nodes usage ### Your current environment n nodes * 8 A100 ### How would you like to use vllm I want to deploy qwen2 model on multi nodes to speed up inference, but large TP may make it not a division o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
