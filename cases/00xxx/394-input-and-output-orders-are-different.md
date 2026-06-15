# vllm-project/vllm#394: Input and output orders are different

| 字段 | 值 |
| --- | --- |
| Issue | [#394](https://github.com/vllm-project/vllm/issues/394) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Input and output orders are different

### Issue 正文摘录

I was trying to do batch inference by feeding a list of texts into `llm.generate()`. But I found that the outputs have different orders from examples in the input list. For example, the result for the first example in the input list may be the second in the output list. Anything suggestions that I may have done something wrong? Thanks!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
