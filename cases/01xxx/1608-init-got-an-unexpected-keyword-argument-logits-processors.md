# vllm-project/vllm#1608: __init__() got an unexpected keyword argument 'logits_processors'

| 字段 | 值 |
| --- | --- |
| Issue | [#1608](https://github.com/vllm-project/vllm/issues/1608) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> __init__() got an unexpected keyword argument 'logits_processors'

### Issue 正文摘录

![image](https://github.com/vllm-project/vllm/assets/56470984/ba7f29cb-26d0-49f6-8a09-87694f20916f) ![image](https://github.com/vllm-project/vllm/assets/56470984/00e828e2-bed4-4653-8a41-5788f880890a) Why does this parameter appear to be missing during operation?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
