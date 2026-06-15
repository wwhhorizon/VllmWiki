# vllm-project/vllm#2214: parameter "logprob": the token with highest score is not the one chosen to filled in answer

| 字段 | 值 |
| --- | --- |
| Issue | [#2214](https://github.com/vllm-project/vllm/issues/2214) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> parameter "logprob": the token with highest score is not the one chosen to filled in answer

### Issue 正文摘录

![image](https://github.com/vllm-project/vllm/assets/34512704/88e00b63-f947-494b-85d7-6deb3dee6558) as show in picture, 151749 with score -0.06xxx and 101158 with -3.25 are the token in answer(token_ids)，but in the position of 151749, the 151750 has smaller score and in verse for 101158.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: token in answer(token_ids)，but in the position of 151749, the 151750 has smaller score and in verse for 101158.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
