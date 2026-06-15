# vllm-project/vllm#71: Dangerous floating point comparison 

| 字段 | 值 |
| --- | --- |
| Issue | [#71](https://github.com/vllm-project/vllm/issues/71) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Dangerous floating point comparison 

### Issue 正文摘录

I noticed that we use conditions like this to check whether it is greedy sampling https://github.com/WoosukKwon/cacheflow/blob/189ae231336857bcc4c6f6157bf7868cdf56fb5f/cacheflow/sampling_params.py#L45 However, I guess this will result in several problems 1. It is not recommended to use `==` for floating point numbers 2. A small temperature will result in inf/nan I typically use something like this https://github.com/lm-sys/FastChat/blob/a94fd259a97128f7f4483ddb760690f467888d84/fastchat/serve/inference.py#L227 @WoosukKwon, @zhuohan123 What do you think? If you are happy, I can change all "==" to "<=".

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ems 1. It is not recommended to use `==` for floating point numbers 2. A small temperature will result in inf/nan I typically use something like this https://github.com/lm-sys/FastChat/blob/a94fd259a97128f7f4483ddb76069...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
