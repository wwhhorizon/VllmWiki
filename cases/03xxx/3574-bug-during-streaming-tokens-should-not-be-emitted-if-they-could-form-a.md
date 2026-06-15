# vllm-project/vllm#3574: [Bug]: During streaming tokens should not be emitted if they could form a stop sequence

| 字段 | 值 |
| --- | --- |
| Issue | [#3574](https://github.com/vllm-project/vllm/issues/3574) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: During streaming tokens should not be emitted if they could form a stop sequence

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Using mistral 7b, prompt `Here is the English alphabet: ABC`, temperature 0, stop sequence `DEFGHIJ`, during streaming, `DEF`, `G`, `HI` tokens are output (`J` triggers the stop). Expected behavior is no output. Tokens should be buffered when they could form prefix of any stop sequences, and sent out when that condition is cleared.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
