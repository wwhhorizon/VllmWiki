# vllm-project/vllm#3055: batching in vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#3055](https://github.com/vllm-project/vllm/issues/3055) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> batching in vllm

### Issue 正文摘录

Team, I was trying to run VLLM with AWQ & FP16 with batch size of 32 & my prompts are approx 1000-2000 tokens. I was running on 1x A100 80GB system & I have observed a strange thing, in the entire batch the first sequence is taking most time to generate response among all the sequence. Please see the below example for batch id 9 where time to complete is around 20 sec for first sequence & remaining sequences are less than 1 sec. Same type of pattern I have observed for rest of batches I ran. ![image](https://github.com/vllm-project/vllm/assets/41502651/d72444eb-9751-4659-9759-103107a90693) Did anyone observed the same pattern while using batches in VLLM or has any idea on why we are getting this pattern ?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: size of 32 & my prompts are approx 1000-2000 tokens. I was running on 1x A100 80GB system & I have observed a strange thing, in the entire batch the first sequence is taking most time to generate response among all the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
