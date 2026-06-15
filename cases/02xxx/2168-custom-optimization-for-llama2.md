# vllm-project/vllm#2168: Custom Optimization for Llama2

| 字段 | 值 |
| --- | --- |
| Issue | [#2168](https://github.com/vllm-project/vllm/issues/2168) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Custom Optimization for Llama2

### Issue 正文摘录

Thank you very much for your work！ I have some questions I would like to consult: ## Is the performance of Ray inferior to that of Torchrun or Deepspeed's distribution? ## If I want to make custom optimizations for the Llama2 architecture, could you provide some suggestions? Thank you very much.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s distribution? ## If I want to make custom optimizations for the Llama2 architecture, could you provide some suggestions? Thank you very much.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Custom Optimization for Llama2 Thank you very much for your work！ I have some questions I would like to consult: ## Is the performance of Ray inferior to that of Torchrun or Deepspeed's distribution? ## If I want to mak...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
