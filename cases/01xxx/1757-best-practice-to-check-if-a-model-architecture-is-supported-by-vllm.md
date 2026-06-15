# vllm-project/vllm#1757: Best practice to check if a model architecture is supported by VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#1757](https://github.com/vllm-project/vllm/issues/1757) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Best practice to check if a model architecture is supported by VLLM

### Issue 正文摘录

Hi vllm team, I want to check if an input model_name_or_path's architecture is supported by vllm, if not I will default to generate with HF. Can you advise me what is the best practice to do this?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Best practice to check if a model architecture is supported by VLLM Hi vllm team, I want to check if an input model_name_or_path's architecture is supported by vllm, if not I will default to generate with HF. Can you ad...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Best practice to check if a model architecture is supported by VLLM Hi vllm team, I want to check if an input model_name_or_path's architecture is supported by vllm, if not I will default to generate with HF. Can you ad...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
