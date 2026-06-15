# vllm-project/vllm#6022: How to use Offline Batched Inference to run multi chat.

| 字段 | 值 |
| --- | --- |
| Issue | [#6022](https://github.com/vllm-project/vllm/issues/6022) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to use Offline Batched Inference to run multi chat.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi, I want to use Offline Batched Inference to run multi chat. every prompt in prompts is as: [ {"role":"system", "content":"You are a helpful assistance."}, {"role":"user", "content":" text"} ], what should i do ?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
