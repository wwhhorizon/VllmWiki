# vllm-project/vllm#770: first token take long time consuming

| 字段 | 值 |
| --- | --- |
| Issue | [#770](https://github.com/vllm-project/vllm/issues/770) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> first token take long time consuming

### Issue 正文摘录

Dears: During baichuan 13b 's token generation based on vllm , the first token in every single prompt always take long time consuming . Sometimes even more than 60 ms . Is this normal ?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
