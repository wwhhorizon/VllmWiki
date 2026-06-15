# vllm-project/vllm#840: Vicuna-13b model consistently outputs repeatedly in tensor parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#840](https://github.com/vllm-project/vllm/issues/840) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Vicuna-13b model consistently outputs repeatedly in tensor parallelism

### Issue 正文摘录

I have two 3090 GPUs on one host, so I tried using a tensor parallel loading model, which ran successfully, but the output kept repeating.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Vicuna-13b model consistently outputs repeatedly in tensor parallelism I have two 3090 GPUs on one host, so I tried using a tensor parallel loading model, which ran successfully, but the output kept repeating.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Vicuna-13b model consistently outputs repeatedly in tensor parallelism I have two 3090 GPUs on one host, so I tried using a tensor parallel loading model, which ran successfully, but the output kept repeating.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
