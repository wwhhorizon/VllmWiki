# vllm-project/vllm#1302: How do you stream tokens with the Python API?

| 字段 | 值 |
| --- | --- |
| Issue | [#1302](https://github.com/vllm-project/vllm/issues/1302) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How do you stream tokens with the Python API?

### Issue 正文摘录

I'd like to be able to do the equivalent of this: ```python for token in llm.prompt("ten names for a pet pelican:"): print(token, end="") ``` I've not been able to figure out how to get back a stream of tokens that I can iterate over as they are produced. I think it's possible because the API server does it - could we get a code example showing how to do this directly using Python?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
