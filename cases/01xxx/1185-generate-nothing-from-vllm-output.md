# vllm-project/vllm#1185: Generate nothing from VLLM output

| 字段 | 值 |
| --- | --- |
| Issue | [#1185](https://github.com/vllm-project/vllm/issues/1185) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 35; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Generate nothing from VLLM output

### Issue 正文摘录

When I run batch inferences, sometimes, the output from vLLM is empty, meaning prediction is empty. Could we make it at least it generate one token? The output is empty is also strange.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
