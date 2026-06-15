# vllm-project/vllm#2897: Is there a function where it iterates over the tokens from the prompt?

| 字段 | 值 |
| --- | --- |
| Issue | [#2897](https://github.com/vllm-project/vllm/issues/2897) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is there a function where it iterates over the tokens from the prompt?

### Issue 正文摘录

My question is the same as the title, but I am searching for the part where the model is going through the prompt's tokens. Moreover, I am unsure how it generates tokens from the input sequence. It seems like most functions are dealing with the output already generated.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tokens from the prompt? My question is the same as the title, but I am searching for the part where the model is going through the prompt's tokens. Moreover, I am unsure how it generates tokens from the input sequence....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tion is the same as the title, but I am searching for the part where the model is going through the prompt's tokens. Moreover, I am unsure how it generates tokens from the input sequence. It seems like most functions ar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
