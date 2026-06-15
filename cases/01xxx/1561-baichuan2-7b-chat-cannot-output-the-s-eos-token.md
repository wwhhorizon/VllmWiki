# vllm-project/vllm#1561: Baichuan2-7b-chat cannot output the </s> eos token.

| 字段 | 值 |
| --- | --- |
| Issue | [#1561](https://github.com/vllm-project/vllm/issues/1561) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Baichuan2-7b-chat cannot output the </s> eos token.

### Issue 正文摘录

My test code is `example/offline_inference.py`, the input prompt is: `" How are you? "`. The output of baichuan2-7b-chat is ``` I am fine thank you :) How about yourself? How are you doing today/now? How's everything going/going well/going well/going well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing well/doing ``` But the output of baichuan2-13b-chat is OK: ``` I'm doing well, thank you for asking. How about you? ``` I am sure that...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: doing well, thank you for asking. How about you? ``` I am sure that 7b model uses the ROPE and 13B model uses the ALIBI. The previous part of output looks correct. The problem seems like cannot output the eos token. Doe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Baichuan2-7b-chat cannot output the </s> eos token. My test code is `example/offline_inference.py`, the input prompt is: `" How are you? "`. The output of baichuan2-7b-chat is ``` I am fine thank you :) How about yourse...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
